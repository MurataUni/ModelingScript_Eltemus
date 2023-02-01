import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from const import Const as MasterConst

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    grip_x = 0.5
    grip_y = 0.3
    grip_length = MasterConst.Arm.Hand.hand_width*2
    grip_geta_1 = sw.rotate(np.pi/2).void()
    grip_geta_2 = sw.parent(grip_geta_1).move_z_back(grip_length/2)
    grip = sw.parent(grip_geta_2).rectangular(grip_x, grip_y, grip_length)
    
    shield_x = 3.
    shield_y = 0.3
    shield_length = 5.
    shield_geta_1 = sw.move_y(1.5)
    shield_geta_2 = sw.parent(shield_geta_1).rotate(np.pi).void()
    shield = sw.parent(shield_geta_2).rectangular(shield_x,shield_y,shield_length)

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()