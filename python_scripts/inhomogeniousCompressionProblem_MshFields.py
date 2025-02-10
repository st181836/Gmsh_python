
import gmsh
import sys

# Initialize Gmsh
gmsh.initialize()

# Create a new model
gmsh.model.add("inhomogeniousCompressionProblem_withMeshFields")

# Let's create a simple rectangular geometry:
lc = 1
gmsh.model.geo.addPoint(0.0, 0.0, 0, lc, 1)
gmsh.model.geo.addPoint(20, 0.0, 0, lc, 2)
gmsh.model.geo.addPoint(20, 10, 0, lc, 3)
gmsh.model.geo.addPoint(0, 10, 0, lc, 4)


gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)

gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 5)
gmsh.model.geo.addPlaneSurface([5], 6)




gmsh.model.geo.mesh.setRecombine(2, 6)  # Ensure quadrilateral elements
# Set transfinite lines





# We could also use a `Box' field to impose a step change in element sizes
# inside a box
gmsh.model.mesh.field.add("Box", 2)
gmsh.model.mesh.field.setNumber(2, "VIn", lc / 3)
gmsh.model.mesh.field.setNumber(2, "VOut", lc)

#This defines the field in which the mesh size changes in one step   
refinebox_start = 10/3
gmsh.model.mesh.field.setNumber(2, "XMin", refinebox_start)
gmsh.model.mesh.field.setNumber(2, "XMax", refinebox_start+10)
gmsh.model.mesh.field.setNumber(2, "YMin", 10-refinebox_start)
gmsh.model.mesh.field.setNumber(2, "YMax", 10)
gmsh.model.mesh.field.setNumber(2, "Thickness", 0.3)

# Let's use the minimum of all the fields as the mesh size field:
gmsh.model.mesh.field.add("Min", 3)
gmsh.model.mesh.field.setNumbers(3, "FieldsList", [1,2])

gmsh.model.mesh.field.setAsBackgroundMesh(2)



gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 0)




# This will prevent over-refinement due to small mesh sizes on the boundary.

# Finally, while the default "Frontal-Delaunay" 2D meshing algorithm
# (Mesh.Algorithm = 6) usually leads to the highest quality meshes, the
# "Delaunay" algorithm (Mesh.Algorithm = 5) will handle complex mesh size fields
# better - in particular size fields with large element size gradients:

#gmsh.option.setNumber("Mesh.Algorithm", 5)

gmsh.model.geo.synchronize()

# Generate the mesh
gmsh.model.mesh.generate(2)

# Write the mesh to a file
gmsh.write("inhomogeniousCompressionProblem_withMeshFields.msh")

# Launch the GUI to see the results:
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

# Finalize Gmsh
gmsh.finalize()