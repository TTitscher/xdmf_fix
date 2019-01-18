import os
import tempfile
import warnings
from subprocess import PIPE, Popen
import meshio


def _xdfm_from_geo_string(geo_string, name, dim):
    tmp = tempfile.mkdtemp()
    geo = os.path.join(tmp, name + ".geo")
    msh = os.path.join(tmp, name + ".msh")
    xdmf = os.path.join(tmp, name + ".xdmf")
    
    with open(geo, "w") as f:
        f.write(geo_string)

    gmsh_cmd = ["gmsh", "-" + str(dim), "-order", "2", geo]
    p = Popen(gmsh_cmd, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    assert not err
   
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        meshio.write(xdmf, meshio.read(msh))

    return xdmf


def triangle6():
    return _xdfm_from_geo_string(
        """
SetFactory("OpenCASCADE");
Rectangle(1) = {0, 0, 0, 1, 1, 0};
Physical Surface(1) = {1};
            """,
        "triangle",
        2,
    )


def tet10():
    return _xdfm_from_geo_string(
        """
SetFactory("OpenCASCADE");
Box(1) = {0, 0, 0, 1, 1, 1};
Physical Volume(1) = {1};
            """,
        "tet10",
        3,
    )

if __name__ == "__main__":
    import shutil
    shutil.move(triangle6(), "test_triangle_6.xdmf")
    shutil.move(tet10(), "test_tet_10.xdmf")
