import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from const import Const as MasterConst

class Const:
    pass

def body_to_chest(sw: Shipwright):
    geta_1 = sw.void(MasterConst.Body.module_length)
    return sw.parent(geta_1).rotate_x(MasterConst.Body.body_to_chest_extension)

def body_to_waist(sw: Shipwright):
    geta_1 = sw.rotate(np.pi).void()
    return sw.parent(geta_1).rotate_x(MasterConst.Body.body_to_waist_extension)

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    body = sw.rectangular(MasterConst.Body.x_length, MasterConst.Body.y_length, MasterConst.Body.module_length)
    
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()