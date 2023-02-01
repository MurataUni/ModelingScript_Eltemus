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

    base_x = MasterConst.Arm.ShoulderArmor.shoulder_armor_base_x
    base_y = MasterConst.Arm.ShoulderArmor.shoulder_armor_base_y
    base_length = MasterConst.Arm.ShoulderArmor.shoulder_armor_base_length

    base = sw.rectangular(base_x, base_y, base_length)

    armor_x = MasterConst.Arm.ShoulderArmor.shoulder_armor_x
    armor_y = MasterConst.Arm.ShoulderArmor.shoulder_armor_y
    armor_thick = MasterConst.Arm.ShoulderArmor.shoulder_armor_thick

    armor_fore_offset =  MasterConst.Arm.ShoulderArmor.shoulder_armer_panel_fore_offset
    armor_back_offset =  MasterConst.Arm.ShoulderArmor.shoulder_armer_panel_back_offset

    armor_fore_geta_1 = sw.parent(base).move_xy((armor_x-base_x)/2, armor_fore_offset)

    armor_fore = sw.parent(armor_fore_geta_1).rectangular(armor_x, armor_y, armor_thick)

    armor_back_geta_1 = sw.parent(base).move_xy((armor_x-base_x)/2, armor_back_offset)
    
    armor_back = sw.parent(armor_back_geta_1).rectangular(armor_x, armor_y, armor_thick)
    
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()