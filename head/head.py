import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

class Const:
    scale = 1.
    thick = 0.1
    edges_outer = [(0.37,2.07),(0.53,1.99),(0.72,1.87),(0.95,1.64),(1.16,1.27),(1.35,0.48),(1.39,0.17),(1.40,-0.26),(1.39,-0.84),(1.12,-3.02),(0.60,-3.02),(0.58,-1.62),(0.14,-1.26),(-0.30,-1.61),(-0.30,-3.01),(-0.90,-3.01),(-0.90,-1.31),(-0.74,-1.23),(-0.63,-1.08),(-0.57,-0.89),(-0.52,0.26),(-0.38,0.24),(-0.25,0.27),(-0.15,0.35),(-0.13,0.49),(-0.16,0.68),(-0.26,0.80),(-0.40,0.85),(-0.55,0.81),(-0.73,1.10),(0.03,1.55),(0.37,1.12),(0.37,0.58),(0.13,0.33),(0.28,0.14),(0.61,0.48),(0.61,1.24),(0.37,1.51)]
    center_outer = edges_util.center(edges_outer)
    edges_face_upper = [(0.10,1.65),(0.10,1.06),(-0.34,1.06),(-0.34,1.65)]
    center_face_upper = edges_util.center(edges_face_upper)
    edges_face_lower = [(-0.45,1.52),(-0.17,1.45),(-0.17,1.21),(-0.45,1.25),(-0.70,1.36),(-0.65,1.62)]
    center_face_lower = edges_util.center(edges_face_lower)
    edges_horn = [(1.04,1.37),(1.10,1.32),(1.27,1.20),(2.31,1.02),(2.60,0.65),(1.18,0.65)]
    center_horn = edges_util.center(edges_horn)

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    geta_1 = sw.rotate(-np.pi/2).void()
    geta_2 = sw.parent(geta_1).move_z_back(Const.thick/2)
    
    outer = sw.parent(geta_2).void(Const.thick)
    face_upper = sw.parent(geta_2).void(Const.thick)
    face_lower = sw.parent(geta_2).void(Const.thick)
    horn = sw.parent(geta_2).void(Const.thick)

    outer.add_ribs(edges=Const.edges_outer)
    outer.add_ribs(positions=[-0.01, 1.01], edges=[Const.center_outer])
    outer.order_ribs()

    face_upper.add_ribs(edges=Const.edges_face_upper)
    face_upper.add_ribs(positions=[-0.01, 1.01], edges=[Const.center_face_upper])
    face_upper.order_ribs()

    face_lower.add_ribs(edges=Const.edges_face_lower)
    face_lower.add_ribs(positions=[-0.01, 1.01], edges=[Const.center_face_lower])
    face_lower.order_ribs()

    horn.add_ribs(edges=Const.edges_horn)
    horn.add_ribs(positions=[-0.01, 1.01], edges=[Const.center_horn])
    horn.order_ribs()

    sw.generate_stl_binary(path, fname, concatinated=False)

if __name__ == "__main__":
    main()