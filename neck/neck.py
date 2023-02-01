import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from const import Const as MasterConst

class Const:
    overrap_chest = 0.4
    overrap_head = 0.4

def neck_to_head(sw: Shipwright):
    geta_1 = sw.void(MasterConst.Neck.module_length)
    geta_2 = sw.parent(geta_1).rotate(MasterConst.Neck.neck_to_head_side_bend_right, MasterConst.Neck.neck_to_head_rotation_left).void()
    return sw.parent(geta_2).rotate_x(MasterConst.Neck.neck_to_head_addction)

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    geta_1 = sw.move_z_back(Const.overrap_chest)
    neck = sw.parent(geta_1).void(MasterConst.Neck.module_length+Const.overrap_chest+Const.overrap_head)
    neck.add_ribs(edges=[(MasterConst.Neck.x_length/2,MasterConst.Neck.y_length/2),(-MasterConst.Neck.x_length/2,MasterConst.Neck.y_length/2),(-MasterConst.Neck.x_length/2,-MasterConst.Neck.y_length/2),(MasterConst.Neck.x_length/2,-MasterConst.Neck.y_length/2)])
    
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()