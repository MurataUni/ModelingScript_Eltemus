import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from const import Const as MasterConst

class Const:
    edges = [(1.50,0.66),(1.50,0.76),(1.50,0.86),(1.50,1.11),(1.50,1.21),(1.49,1.31),(1.47,1.40),(1.45,1.50),(1.42,1.59),(1.39,1.68),(1.35,1.77),(1.30,1.86),(1.25,1.94),(1.19,2.02),(1.13,2.10),(1.06,2.17),(0.99,2.24),(0.91,2.30),(0.83,2.36),(0.75,2.41),(0.66,2.46),(0.57,2.50),(0.48,2.53),(0.39,2.56),(0.29,2.58),(0.20,2.60),(0.10,2.61),(-0.00,2.61),(-0.10,2.61),(-0.20,2.60),(-0.29,2.58),(-0.39,2.56),(-0.48,2.53),(-0.57,2.50),(-0.66,2.46),(-0.75,2.41),(-0.83,2.36),(-0.91,2.30),(-0.99,2.24),(-1.06,2.17),(-1.13,2.10),(-1.19,2.02),(-1.25,1.94),(-1.30,1.86),(-1.35,1.77),(-1.39,1.68),(-1.42,1.59),(-1.45,1.50),(-1.47,1.40),(-1.49,1.31),(-1.50,1.21),(-1.50,1.11),(-1.50,0.86),(-1.50,0.77),(-1.50,0.67),(-1.50,-2.05),(1.50,-2.05)]
    x_range, y_range = edges_util.size(edges)
    x_min, x_max = x_range

def chest_to_neck(sw: Shipwright):
    geta_1 = sw.void(MasterConst.Chest.module_length)
    geta_2 = sw.parent(geta_1).rotate(MasterConst.Chest.chest_to_neck_side_bend_right).void()
    return sw.parent(geta_2).rotate_x(MasterConst.Chest.chest_to_neck_adduction)

def chest_to_right_arm(sw: Shipwright):
    geta_1 = sw.void(MasterConst.Chest.module_length)
    geta_2 = sw.parent(geta_1, MasterConst.Arm.z_position_chest_height_ratio)\
        .move_xy(Const.x_max, MasterConst.Arm.y_position)
    geta_3 = sw.parent(geta_2).rotate(np.pi/2).void()
    return sw.parent(geta_3).rotate(0.,MasterConst.Arm.Right.shoulder_flexion).void()

def chest_to_left_arm(sw:Shipwright):
    geta_1 = sw.void(MasterConst.Chest.module_length)
    geta_2 = sw.parent(geta_1, MasterConst.Arm.z_position_chest_height_ratio)\
        .move_xy(Const.x_min, MasterConst.Arm.y_position)
    geta_3 = sw.parent(geta_2).rotate(np.pi/2, np.pi).void()
    return sw.parent(geta_3).rotate(0.,-MasterConst.Arm.Left.shoulder_flexion).void()

def chest_to_backpack(sw:Shipwright):
    geta_1 = sw.void(MasterConst.Chest.module_length)
    geta_2 = sw.parent(geta_1, MasterConst.Backpack.z_position_chest_height_ratio)\
        .move_y(MasterConst.Backpack.y_position_chest_offset)
    return sw.parent(geta_2).rotate_x(np.pi/2)

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    chest = sw.void(MasterConst.Chest.module_length)
    chest.add_ribs(edges=Const.edges)
    chest.add_ribs([-0.01, 1.01], [(0.,0.)])
    chest.order_ribs()
    
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()