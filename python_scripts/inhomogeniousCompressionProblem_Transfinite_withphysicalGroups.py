
import gmsh
import sys

# Initialize Gmsh
gmsh.initialize()

# Create a new model
gmsh.model.add("inhomogeniousCompressionproblem_Transfinite_withPhysicalGroups")

# Let's create a simple rectangular geometry:
length = 20 #length of the whole domain
height = 10 #height of the whole domain
height_refinement = 10/3 #height of the refinement box
length_refinement = 10 #length of the refinement box
num_of_ele_x = 30
num_of_ele_y = 15
size_ele_x = length/num_of_ele_x
size_ele_y = height/num_of_ele_y
lc = 2.0


gmsh.model.geo.addPoint(0.0, 0.0, 0, lc, 1)
gmsh.model.geo.addPoint(length, 0.0, 0, lc, 2)
gmsh.model.geo.addPoint(length, height, 0, lc, 3)
gmsh.model.geo.addPoint(0, height, 0, lc, 4)

# This is where the refinement happens
gmsh.model.geo.addPoint(size_ele_x*5, 10-size_ele_y*5, 0,lc, 5)
gmsh.model.geo.addPoint(10/3+10, height-10/3, 0, lc, 6)
gmsh.model.geo.addPoint(10/3+10, height, 0, lc/4, 7)
gmsh.model.geo.addPoint(10/3, height, 0, lc, 8)

#This is to have the same number of elements on the opposing sides
gmsh.model.geo.addPoint(size_ele_x*4, 0, 0, lc, 9)
gmsh.model.geo.addPoint(20-size_ele_x*9, 0, 0, lc, 10)
gmsh.model.geo.addPoint(length, size_ele_y*9, 0, lc, 11)
gmsh.model.geo.addPoint(0, size_ele_y*9, 0, lc, 12)


#Number of elements left from the refinement: 4 right from refinement: 9, under the refinement: 9
gmsh.model.geo.addPoint(size_ele_x*4, size_ele_y*9, 0, lc, 15)
gmsh.model.geo.addPoint(20-size_ele_x*9, size_ele_y*9, 0, lc, 16)
gmsh.model.geo.addPoint(20-size_ele_x*9, 10, 0, lc, 17)
gmsh.model.geo.addPoint(size_ele_x*4, 10, 0, lc, 18)

#gmsh.model.geo.addPoint(size_ele_x*4, 10*size_ele_y, 0, lc, 19)
#gmsh.model.geo.addLine(19, 5, 26) #test
#gmsh.model.geo.addLine(18, 19, 27) #test

gmsh.model.geo.addLine(1, 9, 1) #Outer boundary 1
gmsh.model.geo.addLine(9, 15, 21)
gmsh.model.geo.addLine(15, 12, 22)

gmsh.model.geo.addLine(9, 10, 2) #Outer boundary 2
gmsh.model.geo.addLine(10, 16, 23)
gmsh.model.geo.addLine(15, 9, 24)

gmsh.model.geo.addLine(10, 2, 3) #Outer boundary 3
gmsh.model.geo.addLine(2, 11, 4) #Outer boundary 4
gmsh.model.geo.addLine(16, 11, 25)


gmsh.model.geo.addLine(11, 3, 5) #Outer boundary 5
gmsh.model.geo.addLine(3, 17, 6) #Outer boundary 6 
gmsh.model.geo.addLine(7, 8, 7) #Outer boundary 8

gmsh.model.geo.addLine(18, 4, 8)
gmsh.model.geo.addLine(4, 12, 9)
gmsh.model.geo.addLine(12, 1, 10)


#Outer boundary of refinement box
gmsh.model.geo.addLine(5, 6, 12)
gmsh.model.geo.addLine(6, 7, 13)
gmsh.model.geo.addLine(8, 5, 14)

#Padding between the refinement box and the outer boundary
gmsh.model.geo.addLine(15, 16, 16)
gmsh.model.geo.addLine(16, 17, 17)
gmsh.model.geo.addLine(17, 7, 18) #Outer boundary 7
gmsh.model.geo.addLine(8, 18, 19)
gmsh.model.geo.addLine(18, 15, 20)

#whole boundary
#gmsh.model.geo.addCurveLoop([1, 2, 3, 4, 5, 6, -13, -12, -14, 8, 9, 10], 5)
#gmsh.model.geo.addPlaneSurface([5], 7)
#left bottom
gmsh.model.geo.addCurveLoop([1, 21, 22, 10], 9)
gmsh.model.geo.addPlaneSurface([9], 9)
#middle bottom
gmsh.model.geo.addCurveLoop([2, 23, -16, -21], 10)
gmsh.model.geo.addPlaneSurface([10], 10)
#right bottom
gmsh.model.geo.addCurveLoop([3, 4, -25, -23], 11)
gmsh.model.geo.addPlaneSurface([11], 11)
#right top
gmsh.model.geo.addCurveLoop([25, 5, 6, -17], 12)
gmsh.model.geo.addPlaneSurface([12], 12)
#left top
gmsh.model.geo.addCurveLoop([-22, -20, 8, 9], 13)
gmsh.model.geo.addPlaneSurface([13], 13)

#refinement box
gmsh.model.geo.addCurveLoop([12, 13, 7, 14], 6)
gmsh.model.geo.addPlaneSurface([6], 8)

#padding
gmsh.model.geo.addCurveLoop([16, 17, 18, -13, -12, -14, 19, 20], 7)
gmsh.model.geo.addPlaneSurface([7], 7)
gmsh.model.geo.mesh.setRecombine(2, 7) 



#padding
#gmsh.model.geo.mesh.setTransfiniteCurve(16, 18)  #horizontal bottom
#gmsh.model.geo.mesh.setTransfiniteCurve(12, 15*3+1) #vertical right


# Structured mesh in refinement box
gmsh.model.geo.mesh.setTransfiniteCurve(7, 15*3+1)  #horizontal bottom
gmsh.model.geo.mesh.setTransfiniteCurve(13, 5*3+1) #vertical right
gmsh.model.geo.mesh.setTransfiniteCurve(12, 15*3+1) #horizontal top
gmsh.model.geo.mesh.setTransfiniteCurve(14, 5*3+1) #vertical left

gmsh.model.geo.mesh.setTransfiniteSurface(8)
gmsh.model.geo.mesh.setRecombine(2, 8)  # Ensure quadrilateral elements


# Structured mesh lines left bottom
gmsh.model.geo.mesh.setTransfiniteCurve(1, 5)
gmsh.model.geo.mesh.setTransfiniteCurve(21, 10)
gmsh.model.geo.mesh.setTransfiniteCurve(22, 5)
gmsh.model.geo.mesh.setTransfiniteCurve(10, 10)

gmsh.model.geo.mesh.setTransfiniteSurface(9)
gmsh.model.geo.mesh.setRecombine(2, 9)  


# Structured mesh lines middle bottom
gmsh.model.geo.mesh.setTransfiniteCurve(2, 18)
gmsh.model.geo.mesh.setTransfiniteCurve(23, 10)
gmsh.model.geo.mesh.setTransfiniteCurve(16, 18)
gmsh.model.geo.mesh.setTransfiniteCurve(21, 10)

gmsh.model.geo.mesh.setTransfiniteSurface(10)
gmsh.model.geo.mesh.setRecombine(2, 10)  

#Structured mesh lines right bottom
gmsh.model.geo.mesh.setTransfiniteCurve(3, 10)
gmsh.model.geo.mesh.setTransfiniteCurve(4, 10)
gmsh.model.geo.mesh.setTransfiniteCurve(25, 10)
gmsh.model.geo.mesh.setTransfiniteCurve(23, 10)

gmsh.model.geo.mesh.setTransfiniteSurface(11)
gmsh.model.geo.mesh.setRecombine(2, 11)  

#Structured mesh lines right top
gmsh.model.geo.mesh.setTransfiniteCurve(25, 10)
gmsh.model.geo.mesh.setTransfiniteCurve(5, 7)
gmsh.model.geo.mesh.setTransfiniteCurve(6, 10)
gmsh.model.geo.mesh.setTransfiniteCurve(17, 7)

gmsh.model.geo.mesh.setTransfiniteSurface(12)
gmsh.model.geo.mesh.setRecombine(2, 12)  

#Structured mesh lines left top
gmsh.model.geo.mesh.setTransfiniteCurve(22, 5)
gmsh.model.geo.mesh.setTransfiniteCurve(20, 7)
gmsh.model.geo.mesh.setTransfiniteCurve(8, 5)
gmsh.model.geo.mesh.setTransfiniteCurve(9, 7)

gmsh.model.geo.mesh.setTransfiniteSurface(13)
gmsh.model.geo.mesh.setRecombine(2, 13)


#test
gmsh.model.geo.mesh.setTransfiniteCurve(27, 6)
gmsh.model.geo.mesh.setTransfiniteCurve(19, 1)
gmsh.model.geo.mesh.setTransfiniteCurve(26, 1)

#gmsh.model.geo.addCurveLoop([26, -14, 19, 27], 14)
#gmsh.model.geo.addPlaneSurface([14], 14)
#gmsh.model.geo.mesh.setRecombine(2, 14)  # Ensure quadrilateral elements
# This will prevent over-refinement due to small mesh sizes on the boundary.

# Finally, while the default "Frontal-Delaunay" 2D meshing algorithm
# (Mesh.Algorithm = 6) usually leads to the highest quality meshes, the
# "Delaunay" algorithm (Mesh.Algorithm = 5) will handle complex mesh size fields
# better - in particular size fields with large element size gradients:

#gmsh.option.setNumber("Mesh.Algorithm", 5)

gmsh.model.geo.synchronize()

# Finally, we can add some comments by creating a post-processing view
# containing some strings:
nmBC = gmsh.view.add("comments")

#Annotations and groups for Neumann BC
gmsh.view.addListDataString(nmBC,[10/3, height+0.2, 0], ["|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | usw."],["Align", "Left", "Font", "Helvetica"])
gmsh.view.addListDataString(nmBC,[10/3, height, 0], ["v v v v v v  v v v v v v  v v v v v v  v v v v v v  v v v v v v  v v"],["Align", "Left", "Font", "Helvetica"])
gmsh.model.addPhysicalGroup(1, [7], name="Neumann_BC")

gmsh.view.addListDataString(nmBC,[0, -0.1, 0], ["o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o usw."],["Align", "Left", "Font", "Helvetica"])
gmsh.model.addPhysicalGroup(1, [1, 2, 3], name="Dirichlet_BC")
# Generate the mesh
gmsh.model.mesh.generate(2)

# Write the mesh to a file
gmsh.write("inhomogeniousCompressionProblem_Transfinite_withPhysicalGroups.msh")

# Launch the GUI to see the results:
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

# Finalize Gmsh
gmsh.finalize()