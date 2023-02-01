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

    y = MasterConst.Arm.Shoulder.shoulder_adapter_width
    x = MasterConst.Arm.Shoulder.shoulder_adapter_height
    depth = MasterConst.Arm.Shoulder.shoulder_adapter_depth
    overrap = MasterConst.Arm.Shoulder.shoulder_adapter_depth*0.5
    extend = MasterConst.Arm.Shoulder.shoulder_adapter_extend
    geta_1 = sw.move_z_back(overrap)
    sw.parent(geta_1).rectangular(x, y, overrap+depth+extend)
    
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()