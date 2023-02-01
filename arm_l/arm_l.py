import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from const import Const as MasterConst

def shoulder_adapter_to_shoulder(sw: Shipwright):
    geta_1 = sw.void(MasterConst.Arm.Shoulder.shoulder_adapter_depth)
    return sw.parent(geta_1).rotate(MasterConst.Arm.Left.shoulder_abduction).void()

def shoulder_adapter_to_shoulder_armor(sw: Shipwright):
    return sw.rotate(MasterConst.Arm.Left.shoulder_armer_abduction).void()

def shoulder_to_upper_arm(sw: Shipwright):
    return sw.rotate(0.,-MasterConst.Arm.Left.upper_arm_rotation_outer).void(MasterConst.Arm.Shoulder.shoulder_depth)

def upper_arm_to_forearm(sw: Shipwright):
    geta_1 = sw.void(MasterConst.Arm.UpperArm.module_length)
    return sw.parent(geta_1).rotate_x(-MasterConst.Arm.Left.forearm_extension)

def forearm_to_hand(sw: Shipwright):
    geta_1 = sw.rotate(0.,-MasterConst.Arm.Left.hand_rotation_outer)\
        .void(MasterConst.Arm.ForeArm.module_length-MasterConst.Arm.Hand.to_forearm_overrap)
    geta_2 = sw.parent(geta_1).rotate(-MasterConst.Arm.Left.hand_radial_flexion).void()
    return sw.parent(geta_2).rotate_x(-MasterConst.Arm.Left.hand_palmar_flexion)

def hand_to_left_weapon(sw: Shipwright):
    geta_1 = sw.void(MasterConst.Arm.Hand.glasp_position_z)
    return sw.parent(geta_1).move_y(MasterConst.Arm.Hand.glasp_position_y)

def modeling_arm_l(sw: Shipwright, path):
    shoulder_adapter = sw.load_submodule(os.path.join(path, 'shoulder_adapter'), force_load_merged_stl=True, vertex_matching=False)

    shoulder_armor = sw.parent(shoulder_adapter_to_shoulder_armor(sw.parent(shoulder_adapter, MasterConst.Arm.ShoulderArmor.shoulder_adapter_position_ratio)))\
        .load_submodule(os.path.join(path, 'shoulder_armor'), force_load_merged_stl=True, vertex_matching=False)

    shoulder = sw.parent(shoulder_adapter_to_shoulder(sw.parent(shoulder_adapter, 0.)))\
        .load_submodule(os.path.join(path, 'shoulder'), force_load_merged_stl=True, vertex_matching=False)
    
    upper_arm = sw.parent(shoulder_to_upper_arm(sw.parent(shoulder, 0.)))\
        .load_submodule(os.path.join(path, 'upper_arm'), force_load_merged_stl=True, vertex_matching=False)
    
    forearm = sw.parent(upper_arm_to_forearm(sw.parent(upper_arm, 0.)))\
        .load_submodule(os.path.join(path, 'forearm'), force_load_merged_stl=True, vertex_matching=False)

    hand = sw.parent(forearm_to_hand(sw.parent(forearm, 0.)))\
        .load_submodule(os.path.join(path, 'hand_l'), force_load_merged_stl=True, vertex_matching=False)
    return [shoulder_adapter,shoulder_armor,shoulder,upper_arm,forearm,hand]

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    modeling_arm_l(sw, path)
    
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()