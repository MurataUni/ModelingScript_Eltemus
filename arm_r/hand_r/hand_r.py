import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright, Ship
from harbor3d.util import edges_util
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from const import Const as MasterConst

class Const:
    side_margin_palm = MasterConst.Arm.Hand.hand_width*0.1
    offset_y_finger = -MasterConst.Arm.Hand.hand_height*0.05
    offset_y_thumb = -MasterConst.Arm.Hand.hand_height*0.1
    rad_f_abduction_max = np.pi/36
    rad_f_inner_j = (np.pi*5/18, np.pi/2, np.pi/8)
    rad_f_center_j = (np.pi*5/18, np.pi/2, np.pi/7)
    rad_f_outer_j = (np.pi*5/18, np.pi/2, np.pi/6)
    rad_f_thumb_j = (np.pi*2/18, np.pi*3/18, np.pi/8)
    rad_ft_adduction = np.pi*7/18
    rate_finger_overrap = 0.2

def base_to_palm(sw: Shipwright):
    return sw.void(MasterConst.Arm.Hand.wrist_length)

def palm_to_ft(sw: Shipwright):
    geta_1 = sw.move_xy(MasterConst.Arm.Hand.hand_width/2*0.8, Const.offset_y_thumb)
    geta_2 = sw.parent(geta_1).void(MasterConst.Arm.Hand.hand_length*0.1)
    geta_3 = sw.parent(geta_2).rotate(np.pi/2).void()
    geta_4 = sw.parent(geta_3).rotate_x(Const.rad_ft_adduction)
    return sw.parent(geta_4).rotate(0, -np.pi/2).void()

def palm_to_fbase(sw: Shipwright):
    geta_1 = sw.void(MasterConst.Arm.Hand.hand_length*0.9)
    return sw.parent(geta_1).move_y(Const.offset_y_finger)

def fbase_to_f_inner(sw: Shipwright):
    geta_1 = sw.move_x(MasterConst.Arm.Hand.hand_width/2-Const.side_margin_palm)
    return sw.parent(geta_1).rotate(Const.rad_f_abduction_max).void()

def fbase_to_f_outer(sw: Shipwright):
    geta_1 = sw.move_x(-(MasterConst.Arm.Hand.hand_width/2-Const.side_margin_palm))
    return sw.parent(geta_1).rotate(-Const.rad_f_abduction_max).void()

def finger_1to3(sw: Shipwright, rads:tuple, lens:tuple):
    f_j1 = sw.parent(sw.rotate_x(rads[0])).void(lens[0])
    f_j2 = sw.parent(sw.parent(f_j1).rotate_x(rads[1])).void(lens[1])
    f_j3 = sw.parent(sw.parent(f_j2).rotate_x(rads[2])).void(lens[2])
    return (f_j1, f_j2, f_j3)

def load_finger_1to3(sw: Shipwright, base:Ship, rads:tuple, lens:tuple, paths:tuple):
    f1_j1_base, f1_j2_base, f1_j3_base = finger_1to3(sw.parent(base), rads, lens)
    f1_j1 = sw.parent(f1_j1_base, 0).load_submodule(paths[0], vertex_matching=False)
    f1_j1_base.keel.length = f1_j1.keel.length*(1-Const.rate_finger_overrap)
    f1_j2 = sw.parent(f1_j2_base, 0).load_submodule(paths[1], vertex_matching=False)
    f1_j2_base.keel.length = f1_j2.keel.length*(1-Const.rate_finger_overrap)
    f1_j3 = sw.parent(f1_j3_base, 0).load_submodule(paths[2], vertex_matching=False)

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    wrist_x = MasterConst.Arm.Hand.wrist_width
    wrist_y = MasterConst.Arm.Hand.wrist_height
    wrist_z = MasterConst.Arm.Hand.wrist_length

    wrist = sw.rectangular(wrist_x, wrist_y, wrist_z)

    palm = sw.parent(base_to_palm(sw)).rectangular(MasterConst.Arm.Hand.hand_width, MasterConst.Arm.Hand.hand_height, MasterConst.Arm.Hand.hand_length)

    fbase = palm_to_fbase(sw.parent(palm,0))

    f_inner_base = fbase_to_f_inner(sw.parent(fbase))
    f_inner_lens = (MasterConst.Arm.Finger.finger_1_length, MasterConst.Arm.Finger.finger_1_length, MasterConst.Arm.Finger.finger_3_length)
    f_inner_paths = (os.path.join(path, "finger_1"), os.path.join(path, "finger_1"), os.path.join(path, "finger_3"))
    load_finger_1to3(sw, f_inner_base, Const.rad_f_inner_j, f_inner_lens, f_inner_paths)

    f_center_base = fbase
    f_center_lens = (MasterConst.Arm.Finger.finger_1_length, MasterConst.Arm.Finger.finger_1_length, MasterConst.Arm.Finger.finger_3_length)
    f_center_paths = (os.path.join(path, "finger_wide_1"), os.path.join(path, "finger_wide_1"), os.path.join(path, "finger_wide_3"))
    load_finger_1to3(sw, f_center_base, Const.rad_f_center_j, f_center_lens, f_center_paths)

    f_outer_base = fbase_to_f_outer(sw.parent(fbase))
    f_outer_lens = (MasterConst.Arm.Finger.finger_1_length, MasterConst.Arm.Finger.finger_1_length, MasterConst.Arm.Finger.finger_3_length)
    f_outer_paths = (os.path.join(path, "finger_1"), os.path.join(path, "finger_1"), os.path.join(path, "finger_3"))
    load_finger_1to3(sw, f_outer_base, Const.rad_f_outer_j, f_outer_lens, f_outer_paths)

    ft_base = palm_to_ft(sw.parent(palm,0))
    ft_lens = (MasterConst.Arm.Finger.finger_thumb_1_length, MasterConst.Arm.Finger.finger_thumb_1_length, MasterConst.Arm.Finger.finger_thumb_3_length)
    ft_paths = (os.path.join(path, "thumb_1"), os.path.join(path, "thumb_1"), os.path.join(path, "thumb_3"))
    load_finger_1to3(sw, ft_base, Const.rad_f_thumb_j, ft_lens, ft_paths)

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()