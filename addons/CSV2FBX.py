# -*- coding: utf-8 -*-
import bpy
import csv

for ob in bpy.context.scene.objects:
    ob.select_set(False)

bpy.ops.object.select_all(action="SELECT")

bpy.ops.object.delete(use_global=False)

vox_csv = []
with open("C:/Users/ics/GitHub/Blender_python_scripts/Resources/vox.csv") as f:
    vox_csv.extend(list(csv.reader(f)))

for row in vox_csv:
    print(row)

vox_positions = vox_csv[5:-2]

_size = 1
for pos in vox_positions:
    _x,_y,_z,_ = pos
    bpy.ops.mesh.primitive_cube_add(size=_size, enter_editmode=False, align='WORLD', location=(int(_x), int(_y), int(_z)), scale=(1, 1, 1))