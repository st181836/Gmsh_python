# This file was written with GitHub Copilot
import gmsh
import sys

# Initialize Gmsh
gmsh.initialize()

# Create a new model
gmsh.model.add("rectangle")

# Define the corner points of the rectangle
length = 20
height = 10
lc = .15
p1 = gmsh.model.geo.addPoint(0, 0, 0, lc)
p2 = gmsh.model.geo.addPoint(length, 0, 0, lc)
p3 = gmsh.model.geo.addPoint(length, height, 0, lc)
p4 = gmsh.model.geo.addPoint(0, height, 0, lc)

# Define the lines between the points
l1 = gmsh.model.geo.addLine(p1, p2)
l2 = gmsh.model.geo.addLine(p2, p3)
l3 = gmsh.model.geo.addLine(p3, p4)
l4 = gmsh.model.geo.addLine(p4, p1)

# Create a curve loop and a plane surface
curve_loop = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])
plane_surface = gmsh.model.geo.addPlaneSurface([curve_loop])

# Set transfinite lines
num_points_length = 20  # Number of points along the length
num_points_height = 10  # Number of points along the height
gmsh.model.geo.mesh.setTransfiniteCurve(l1, num_points_length)
gmsh.model.geo.mesh.setTransfiniteCurve(l2, num_points_height)
gmsh.model.geo.mesh.setTransfiniteCurve(l3, num_points_length)
gmsh.model.geo.mesh.setTransfiniteCurve(l4, num_points_height)

# Set transfinite surface
gmsh.model.geo.mesh.setTransfiniteSurface(plane_surface)
gmsh.model.geo.mesh.setRecombine(2, plane_surface)  # Ensure quadrilateral elements

# Synchronize the CAD kernel with the Gmsh model
gmsh.model.geo.synchronize()



# Generate the mesh
gmsh.model.mesh.generate(2)

# Write the mesh to a file
gmsh.write("rectangle.msh")

# Launch the GUI to see the results:
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

# Finalize Gmsh
gmsh.finalize()