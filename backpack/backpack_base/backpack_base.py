import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from const import Const as MasterConst

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    base_x = MasterConst.Backpack.base_x
    base_y = MasterConst.Backpack.base_y
    base_thick = MasterConst.Backpack.base_thick

    base = sw.rectangular(base_x, base_y, base_thick)

    upper_panel_x = MasterConst.Backpack.upper_panel_x
    upper_panel_y = MasterConst.Backpack.upper_panel_y
    upper_panel_length = MasterConst.Backpack.upper_panel_length

    upper_panel_geta_1 = sw.parent(base).move_y(MasterConst.Backpack.upper_panel_offset_y)
    upper_panel = sw.parent(upper_panel_geta_1).rectangular(upper_panel_x, upper_panel_y, upper_panel_length)
    
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()