import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from const import Const as MasterConst

class Const:
    pass

def waist_to_leg_center(sw: Shipwright):
    return sw.void(MasterConst.Waist.CoxaJoint.coxa_joint_z_position)

def waist_to_leg_r(sw: Shipwright):
    geta_1 = sw.parent(waist_to_leg_center(sw)).rotate(-np.pi/2).void(MasterConst.Waist.CoxaJoint.length/2)
    geta_2 = sw.parent(geta_1).rotate(MasterConst.Leg.Right.leg_abduction).void()
    geta_3 = sw.parent(geta_2).rotate_x(MasterConst.Leg.Right.leg_extension)
    return sw.parent(geta_3).rotate(0.,MasterConst.Leg.Right.leg_rotation_outer).void()

def waist_to_leg_l(sw: Shipwright):
    geta_1 = sw.parent(waist_to_leg_center(sw)).rotate(np.pi/2).void(MasterConst.Waist.CoxaJoint.length/2)
    geta_2 = sw.parent(geta_1).rotate(-MasterConst.Leg.Left.leg_abduction).void()
    geta_3 = sw.parent(geta_2).rotate_x(MasterConst.Leg.Left.leg_extension)
    return sw.parent(geta_3).rotate(0.,-MasterConst.Leg.Left.leg_rotation_outer).void()

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    waist_upper = sw.rectangular(MasterConst.Waist.Upper.x_length, MasterConst.Waist.Upper.y_length, MasterConst.Waist.Upper.thick)
    
    waist_lower = sw.parent(waist_upper, 0.1/MasterConst.Waist.Upper.thick)\
        .rectangular(MasterConst.Waist.Lower.x_length, MasterConst.Waist.Lower.y_length, MasterConst.Waist.Lower.thick)

    coxa_length = MasterConst.Waist.CoxaJoint.length
    coxa_radius = MasterConst.Waist.CoxaJoint.coxa_radius
    coxa_geta_1 = waist_to_leg_center(sw.parent(waist_upper, 0.))
    coxa_geta_2 = sw.parent(coxa_geta_1).rotate(-np.pi/2).void(MasterConst.Waist.CoxaJoint.length/2)
    coxa = sw.parent(coxa_geta_2).rotate(np.pi).pole(coxa_length,coxa_radius,2*np.pi,8,True)
    coxa.add_ribs([-0.01,1.01], [(0.,0.)])

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()