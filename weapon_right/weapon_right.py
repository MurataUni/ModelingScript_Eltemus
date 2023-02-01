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
    grip_length = MasterConst.Arm.Hand.hand_width*1.8
    grip_geta_1 = sw.rotate(np.pi*(9-1.5)/18).void()
    grip_geta_2 = sw.parent(grip_geta_1).move_z_back(grip_length/2)
    grip = sw.parent(grip_geta_2).rectangular(grip_x, grip_y, grip_length)
    
    barrel_x = 1.2
    barrel_y = 0.8
    barrel_length = 6.
    barrel_geta_1 = sw.parent(grip).rotate(-np.pi*(9-1.5)/18).void()
    barrel_geta_2 = sw.parent(barrel_geta_1).move_x(barrel_x/2)
    barrel_geta_3 = sw.parent(barrel_geta_2).move_z_back(1.)
    barrel = sw.parent(barrel_geta_3).rectangular(barrel_x, barrel_y, barrel_length)

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()