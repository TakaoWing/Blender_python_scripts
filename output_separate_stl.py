import bpy
from pathlib import Path
import sys

for item in bpy.data.objects:
    bpy.data.objects.remove(item)

bpy.ops.import_mesh.stl(filepath="/content/input.stl")

bpy.ops.object.select_all(action='SELECT')

bpy.ops.mesh.separate(type="LOOSE")

bpy.ops.object.select_all(action='DESELECT')

context = bpy.context
scene = context.scene
viewlayer = context.view_layer


obs = [o for o in scene.objects if o.type == 'MESH']   

path = Path("/content/output/")
for ob in obs:
    viewlayer.objects.active = ob
    ob.select_set(True)
    stl_path = path / f"{ob.name}.stl"
    bpy.ops.export_mesh.stl(
            filepath=str(stl_path),
            use_selection=True)
    ob.select_set(False)