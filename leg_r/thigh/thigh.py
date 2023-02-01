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

    width = MasterConst.Leg.Thigh.x_length
    height = MasterConst.Leg.Thigh.y_length
    depth = MasterConst.Leg.Thigh.length
    overrap = MasterConst.Leg.Thigh.overrap

    geta_1 = sw.move_z_back(overrap)
    sw.parent(geta_1).rectangular(width, height, overrap+depth)
    
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()