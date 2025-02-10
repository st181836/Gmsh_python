import gmsh
import sys



gmsh.initialize()

gmsh.model.add("t1_omitPhysNames") #If not handled, Ikraus cant handle physical groups (or names)

# lc is target mash size
lc = 1e-2


#First elementary entity: Points
gmsh.model.geo.addPoint(0, 0, 0, lc, 1) #Last entry is the tag which has to be unique within each entity
gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(.1, .3, 0, lc, 3)
gmsh.model.geo.addPoint(0, .3, 0, lc)

#Second elementary entity: Lines
gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(3, 2, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)

#Third elementary entity: Surface
gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1) #Loop over lines, last entry is tag
gmsh.model.geo.addPlaneSurface([1], 1)

#Create relevant Gmsh datastructures by the synchonizing CAD entities with the Gmsh model
#It is usually best to minimize synchonization points, because much processing
gmsh.model.geo.synchronize()

#No mesh size specified: Default uniform meshsize is used

# We can then generate a 2D mesh...
gmsh.model.mesh.generate(2)


# ... and save it to disk
gmsh.option.setNumber("Mesh.MshFileVersion", 2.2) # For Ikraus: use version 2 
gmsh.write("t1.msh")

#if no popup we can visualize with GUI
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

# This should be called when you are done using the Gmsh Python API:
gmsh.finalize()