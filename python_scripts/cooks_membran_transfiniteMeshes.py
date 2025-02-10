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

gmsh.model.add("cooks_membrane_transfiniteMeshes") #In this example without transfinite meshes

lc = 1e-2
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



# The `setTransfiniteCurve()' meshing constraints explicitly specifies the
# location of the nodes on the curve. For example, the following command forces
# 20 uniformly placed nodes on curve 2 (including the nodes on the two end
# points):

#The optional argument ‘Using Progression expression’ instructs the transfinite algorithm to 
# distribute the nodes following a geometric progression (Progression 2 meaning for example that 
# each line element in the series will be twice as long as the preceding one)

n_ele_x = 5
n_ele_y = 6

gmsh.model.geo.mesh.setTransfiniteCurve(1, n_ele_y, "Progression", 1)
gmsh.model.geo.mesh.setTransfiniteCurve(2, n_ele_x, "Progression", 1)
gmsh.model.geo.mesh.setTransfiniteCurve(3, n_ele_y, "Progression", 1)
gmsh.model.geo.mesh.setTransfiniteCurve(4, n_ele_x, "Progression", 1)

gmsh.model.geo.mesh.setTransfiniteSurface(1, "Left") #Setting corner Tags [] is mandatory if more than 4 corners are available

#Now we have quads instead of triangles
## mesh:
#gmsh.option.setNumber("Mesh.Smoothing", 20)

gmsh.model.geo.mesh.setRecombine(2, 1)

# Finally we apply an elliptic smoother to the grid to have a more regular

#Create relevant Gmsh datastructures by the synchonizing CAD entities with the Gmsh model
#It is usually best to minimize synchonization points, because much processing
gmsh.model.geo.synchronize()

#No mesh size specified: Default uniform meshsize is used

# We can then generate a 2D mesh...
gmsh.model.mesh.generate(2)


# ... and save it to disk
gmsh.option.setNumber("Mesh.MshFileVersion", 2.2) # For Ikraus: use version 2 
gmsh.write("cooks_membrane_transfiniteMeshes.msh")

#if no popup we can visualize with GUI
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

# This should be called when you are done using the Gmsh Python API:
gmsh.finalize()
