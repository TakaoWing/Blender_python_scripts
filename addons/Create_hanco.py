# -*- coding: utf-8 -*-
import bpy
import time

for ob in bpy.context.scene.objects:
    ob.select_set(False)

bpy.ops.object.select_all(action="SELECT")

bpy.ops.object.delete(use_global=False)

bpy.ops.import_curve.svg(filepath="G:\マイドライブ\クリエーターネームスタンプ-令和2年度卒業生-\みっぽん\SVG\細め.svg", filter_glob='*.svg')

for ob in bpy.context.scene.objects:
    ob.select_set(False)


for item in bpy.context.scene.objects:
    print(item.name)
    item.select_set(True)

    bpy.context.view_layer.objects.active = item

    bpy.ops.object.convert(target="MESH")
    
    item.select_set(False)
    
for ob in bpy.context.scene.objects:
    ob.select_set(True)

bpy.ops.object.booltool_auto_union()
x = 0

for ob in bpy.context.scene.objects:
    ob.select_set(True)
    ob.name = "hanco"
    x = ob.dimensions[0]

size = 13.5 / x

bpy.ops.transform.resize(value=(size, size, 1))

bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='BOUNDS')

bpy.ops.object.mode_set(mode='EDIT')

bpy.ops.mesh.select_all(action='SELECT')

bpy.ops.mesh.extrude_context_move(TRANSFORM_OT_translate={"value":(0, 0, 3)})

bpy.ops.object.mode_set(mode='OBJECT')

bpy.ops.mesh.primitive_cylinder_add(vertices=500, radius=13.5/2, depth=60, enter_editmode=False, align='WORLD', location=(0, 0, 32.9), scale=(1, 1, 1))

for ob in bpy.context.scene.objects:
    ob.select_set(False)

bpy.data.objects["hanco"].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects["hanco"]

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cylinder"]
bpy.context.object.modifiers["Boolean"].use_self = True
bpy.ops.object.modifier_apply(modifier="Boolean")

bpy.data.objects["hanco"].select_set(False)
bpy.data.objects["Cylinder"].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects["Cylinder"]

bpy.ops.object.delete(use_global=False)

