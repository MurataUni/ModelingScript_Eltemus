import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from const import Const as MasterConst

def backpack_to_side_panel_center(sw: Shipwright):
    geta_1 = sw.void(MasterConst.Backpack.base_thick + MasterConst.Backpack.SidePanel.position_z_offset)
    return sw.parent(geta_1).move_y(MasterConst.Backpack.SidePanel.position_y_offset)

def backpack_to_right_panel(sw: Shipwright):
    center = backpack_to_side_panel_center(sw)
    geta_1 = sw.parent(center).move_x(-MasterConst.Backpack.SidePanel.position_x_offset_right)
    return sw.parent(geta_1).rotate(MasterConst.Backpack.Right.rotate_y,MasterConst.Backpack.Right.rotate_z).void()

def backpack_to_left_panel(sw: Shipwright):
    center = backpack_to_side_panel_center(sw)
    geta_1 = sw.parent(center).move_x(MasterConst.Backpack.SidePanel.position_x_offset_right)
    return sw.parent(geta_1).rotate(MasterConst.Backpack.Left.rotate_y,MasterConst.Backpack.Left.rotate_z).void()

def modeling_backpack(sw: Shipwright, path):
    base = sw.load_submodule(os.path.join(path, 'backpack_base'), force_load_merged_stl=True, vertex_matching=False)

    right_panel = sw.parent(backpack_to_right_panel(sw.parent(base, 0)))\
        .load_submodule(os.path.join(path, 'side_panel'), force_load_merged_stl=True, vertex_matching=False)
    
    left_panel = sw.parent(backpack_to_left_panel(sw.parent(base, 0)))\
        .load_submodule(os.path.join(path, 'side_panel'), force_load_merged_stl=True, vertex_matching=False)
    return [base, right_panel, left_panel]

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    modeling_backpack(sw, path)
    
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()