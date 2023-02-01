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
    arm_r_path = os.path.join(os.sep.join(path.split(os.sep)[:-2]), 'arm_r')
    print(arm_r_path)
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    sw.load_submodule(os.path.join(arm_r_path, 'shoulder_adapter'), force_load_merged_stl=True, vertex_matching=False)
    sw.deformation_all(lambda x,y,z: (-x,y,z))
    for ship in sw.dock.ships:
        if ship.is_monocoque():
            for triangle in ship.monocoque_shell.triangles:
                triangle.inverse()
    
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()