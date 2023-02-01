import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from const import Const as MasterConst

def thigh_to_shin(sw: Shipwright):
    geta_1 = sw.void(MasterConst.Leg.Thigh.length)
    return sw.parent(geta_1).rotate_x(MasterConst.Leg.Right.shin_flexion)

def shin_to_foot(sw: Shipwright):
    geta_1 = sw.void(MasterConst.Leg.Shin.length)
    geta_2 = sw.parent(geta_1).rotate(MasterConst.Leg.Right.foot_radial_flexion).void()
    geta_3 = sw.parent(geta_2).rotate_x(MasterConst.Leg.Right.foot_palmar_flexion)
    return sw.parent(geta_3).rotate(0., MasterConst.Leg.Right.foot_rotation_outer).void()

def modeling_leg_r(sw: Shipwright, path):
    thigh = sw.load_submodule(os.path.join(path, 'thigh'), force_load_merged_stl=True, vertex_matching=False)

    shin = sw.parent(thigh_to_shin(sw.parent(thigh, 0)))\
        .load_submodule(os.path.join(path, 'shin'), force_load_merged_stl=True, vertex_matching=False)
    
    foot = sw.parent(shin_to_foot(sw.parent(shin, 0.)))\
        .load_submodule(os.path.join(path, 'foot'), force_load_merged_stl=True, vertex_matching=False)

    return [thigh, shin, foot]

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    modeling_leg_r(sw, path)
    
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()