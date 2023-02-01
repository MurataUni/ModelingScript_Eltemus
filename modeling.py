import sys
sys.dont_write_bytecode = True

import os
import numpy as np

from harbor3d import Dock, Shipwright
from const import Const as MasterConst

from body.body import body_to_chest, body_to_waist
from chest.chest import chest_to_neck, chest_to_right_arm, chest_to_left_arm, chest_to_backpack
from neck.neck import neck_to_head
from waist.waist import waist_to_leg_r, waist_to_leg_l
from arm_r.arm_r import modeling_arm_r, hand_to_right_weapon
from arm_l.arm_l import modeling_arm_l, hand_to_left_weapon
from backpack.backpack import modeling_backpack
from leg_r.leg_r import modeling_leg_r
from leg_l.leg_l import modeling_leg_l

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    base = sw.rotate_x(MasterConst.rotate_x)

    body = sw.parent(base)\
        .load_submodule(os.path.join(path, 'body'), force_load_merged_stl=True, vertex_matching=False)

    chest = sw.parent(body_to_chest(sw.parent(body,0.)))\
        .load_submodule(os.path.join(path, 'chest'), force_load_merged_stl=True, vertex_matching=False)

    # Head
    neck = sw.parent(chest_to_neck(sw.parent(chest,0.)))\
        .load_submodule(os.path.join(path, 'neck'), force_load_merged_stl=True, vertex_matching=False)
    
    head = sw.parent(neck_to_head(sw.parent(neck,0.)))\
        .load_submodule(os.path.join(path, 'head'), force_load_merged_stl=True, vertex_matching=False)
    
    # Arm Right
    arm_r_objects = modeling_arm_r(sw.parent(chest_to_right_arm(sw.parent(chest,0.))), os.path.join(path,'arm_r'))

    # Weapon Right
    weapon_right = sw.parent(hand_to_right_weapon(sw.parent(arm_r_objects[-1], 0)))\
        .load_submodule(os.path.join(path, 'weapon_right'), force_load_merged_stl=True, vertex_matching=False)

    # Arm Left
    arm_l_objects = modeling_arm_l(sw.parent(chest_to_left_arm(sw.parent(chest,0.))), os.path.join(path,'arm_l'))

    # Weapon Left
    weapon_left = sw.parent(hand_to_left_weapon(sw.parent(arm_l_objects[-1], 0)))\
        .load_submodule(os.path.join(path, 'weapon_left'), force_load_merged_stl=True, vertex_matching=False)

    # Backpck
    backpack_objects = modeling_backpack(sw.parent(chest_to_backpack(sw.parent(chest,0.))), os.path.join(path, 'backpack'))

    # Waist
    waist = sw.parent(body_to_waist(sw.parent(body,0.)))\
        .load_submodule(os.path.join(path, 'waist'), force_load_merged_stl=True, vertex_matching=False)

    # Leg Right
    leg_r_objects = modeling_leg_r(sw.parent(waist_to_leg_r(sw.parent(waist,0.)), 0.), os.path.join(path, 'leg_r'))

    # Leg Left
    leg_l_objects = modeling_leg_l(sw.parent(waist_to_leg_l(sw.parent(waist,0.)), 0.), os.path.join(path, 'leg_l'))

    sw.scale(MasterConst.scale)
    sw.dock.sanitize_dock(True)
    
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()