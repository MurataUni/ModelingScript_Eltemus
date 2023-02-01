import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-3]))
from const import Const as MasterConst

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    sw.rectangular(MasterConst.Arm.Finger.finger_3_width, MasterConst.Arm.Finger.finger_3_height, MasterConst.Arm.Finger.finger_3_length)

    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()