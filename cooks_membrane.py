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

gmsh.model.add("t1_omitPhysNames") #In this example without transfinite meshes

lc = 10 #Meshsize

gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(0, 44, 0, lc, 2)
gmsh.model.geo.addPoint(48, 60, 0, lc*0.01, 3)
gmsh.model.geo.addPoint(48, 44, 0, lc, 4)

gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)

gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)

gmsh.model.geo.addPlaneSurface([1], 1)



gmsh.model.geo.mesh.setRecombine(2, 1)

#Create relevant Gmsh datastructures by the synchonizing CAD entities with the Gmsh model
#It is usually best to minimize synchonization points, because much processing
gmsh.model.geo.synchronize()

#No mesh size specified: Default uniform meshsize is used

# We can then generate a 2D mesh...
gmsh.model.mesh.generate(2)


# ... and save it to disk
gmsh.option.setNumber("Mesh.MshFileVersion", 2.2) # For Ikraus: use version 2 
gmsh.write("cooks_membrane.msh")

#if no popup we can visualize with GUI
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

# This should be called when you are done using the Gmsh Python API:
gmsh.finalize()
