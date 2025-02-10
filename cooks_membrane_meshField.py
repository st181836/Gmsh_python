#Gmsh project created on Wed Jun 15 11:47:52 2022

# ------------------------------------------------------------------------------
#
#  Gmsh Python Ikraus Example Geometry 08: Cooks Membrane default meshing
#
#  To set up patch test
#
# ------------------------------------------------------------------------------

# The Python API is entirely defined in the `gmsh.py' module (which contains the
# full documentation of all the functions in the API):

import gmsh
import sys

gmsh.initialize()

gmsh.model.add("cooks_membrane_meshField") #In this example without transfinite meshes

lc = 2
gmsh.model.geo.addPoint(0, 0, 0, 1)
gmsh.model.geo.addPoint(0, 44, 0, 2)
gmsh.model.geo.addPoint(48, 60, 0, 3)
gmsh.model.geo.addPoint(48, 44, 0, 4)

gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)

gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)

gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.synchronize()


#Meshsize depending on the distance
# gmsh.model.mesh.field.add("Distance", 1)
# gmsh.model.mesh.field.setNumbers(1, "CurvesList", [2])
# gmsh.model.mesh.field.setNumbers(1, "PointsList", [4])

# gmsh.model.mesh.field.setNumber(1, "Sampling", 100)

#Meshsize
# gmsh.model.mesh.field.add("Threshold", 2)
# gmsh.model.mesh.field.setNumber(2, "InField", 2)
# gmsh.model.mesh.field.setNumber(2, "SizeMin", lc / 30)
# gmsh.model.mesh.field.setNumber(2, "SizeMax", lc)
# gmsh.model.mesh.field.setNumber(2, "DistMin", 0.15)
# gmsh.model.mesh.field.setNumber(2, "DistMax", 2)


# Let's use the minimum of all the fields as the mesh size field:
gmsh.model.mesh.field.add("Min", 7)
gmsh.model.mesh.field.setNumbers(7, "FieldsList", [2, 3, 5, 6])

gmsh.model.mesh.field.setAsBackgroundMesh(7)

# The API also allows to set a global mesh size callback, which is called each
# time the mesh size is queried
def meshSizeCallback(dim, tag, x, y, z, lc):
    return min(lc, 2 * x + 1)

gmsh.model.mesh.setSizeCallback(meshSizeCallback)
gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 0)

gmsh.model.mesh.generate(2)

gmsh.option.setNumber("Mesh.MshFileVersion", 2.2) # For Ikraus: use version 2 
gmsh.write("cooks_membrane_meshField.msh")

#if no popup we can visualize with GUI
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

# This should be called when you are done using the Gmsh Python API:
gmsh.finalize()
