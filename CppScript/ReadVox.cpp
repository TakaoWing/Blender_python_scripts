//
// VOX形式読み込み
// SOURCE https://github.com/ephtracy/voxel-model/blob/master/MagicaVoxel-file-format-vox.txt
//
#include <iostream>
#include <fstream>
#include <vector>
#include <cassert>
#include <sstream>

using namespace std;

// VOX形式かどうか調べる
bool checkVox(ifstream &fin, ostringstream* stream)
{
    char id[4];
    int version;

    fin.read(id, 4);
    fin.read((char *)&version, 4);

    auto chunk_id = string(id, 4);
    *stream << chunk_id << ", " << version << "\n";

    return chunk_id == "VOX ";
}

int main(int argc, char *argv[])
{
    ostringstream stream;
    auto path = argv[1];

    // バイナリ形式でファイルを開く
    auto fin = ifstream(path, ios::binary);
    assert(fin);

    auto vox = checkVox(fin,&stream);
    assert(vox);

    // VOXデータはチャンク方式でデータが格納されている
    while (!fin.eof())
    {
        char id[4];
        int chunk_size;
        int child_size;

        // ヘッダ部を読み込む
        fin.read(id, 4);
        fin.read((char *)&chunk_size, 4);
        fin.read((char *)&child_size, 4);
        auto chunk_id = string(id, 4);

        stream << chunk_id << ": " << chunk_size << ", " << child_size << "\n";
        if (chunk_id == "SIZE")
        {
            // サイズ
            int x;
            int y;
            int z;

            fin.read((char *)&x, 4);
            fin.read((char *)&y, 4);
            fin.read((char *)&z, 4);

            stream << x << ", " << y << ", " << z << "\n";
        }
        else if (chunk_id == "XYZI")
        {
            // 配置されたボクセル
            // x, y, z, color
            int num;
            fin.read((char *)&num, 4);
            for (int i = 0; i < num; ++i)
            {
                char data[4];
                fin.read(data, 4);
                stream << int(data[0]) << ", " << int(data[1]) << ", " << int(data[2]) << ", (" << int(data[3]) << ")\n";
            }
        }
        else if (chunk_id == "RGBA")
        {
            // 色。256色固定(r, g, b, a)
            for (int i = 0; i < 256; ++i)
            {
                char data[4];
                fin.read(data, 4);
            }
        }
        else
        {
            // 上記以外のチャンクはスキップ
            fin.seekg(chunk_size, ios::cur);
        }
    }

    ofstream ofs("vox.csv",ios_base::app);
    if(!ofs){
        cerr << "error" << endl;
    }
    ofs << stream.str() << endl;
    ofs.close();
}