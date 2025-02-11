# Gmsh_python
Some applications from the Gmsh Python interface. 

---
## How to start using the Gmsh python API
Follow the steps from the README.txt of the [official tutorial](https://gitlab.onelab.info/gmsh/gmsh/-/tree/master/tutorials/python?ref_type=heads)

All Python tutorials from the documentation can be found here.

---

## Defining Gmsh properties  
*(Text below taken from **Section 13** in [Gmsh documentation](https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-application-programming-interface))*




> **How do I define boundary conditions or material properties in Gmsh?**  
> By design, Gmsh does not try to incorporate every possible definition of boundary conditions or material properties—this is a job best left to the solver. Instead, Gmsh provides a simple mechanism to tag groups of elements, and it is up to the solver to interpret these tags as boundary conditions, materials, etc. Associating tags with elements in Gmsh is done by defining physical groups (Physical Points, Physical Curves, Physical Surfaces and Physical Volumes). See the reference manual as well as the tutorials (in particular t1) for a detailed description and some examples.  
>
> The Gmsh API can be used to build sophisticated interactive workflows where the definition of boundary conditions and material properties can be fully tailored to your preferred solver. For an example see `examples/api/prepro.py`.

---

## Example Mesh: Inhomogeneous Compression Problem

![Inhomogeneous compression problem; left: problem description; right: deformed mesh at the limit point (Q2, n_ele = 1125, γ_c = 1.03).](Images/Screenshot%202025-02-09%20184141_Bieber.png)


This figure shows one of the meshes which will be defined in this repository. It illustrates an inhomogeneous compression problem, where you can see the deformation of a rectangular domain under an applied load.  
Paper: DOI: 10.1002/nme.7224

### Approach 1: Use mesh size field
By defing a box mesh field, a (sudden) step change in element sizes can be imposed. The figure below has 1/3 of the target mesh size inside the refinement box.
![Inhomogeneous compression problem with mesh size fields](Images/inhomoComProblem_usingMeshFields.png)

### Approach 2: Create sectors of structured meshes
When setting a transfinite surface, the number of nodes on the connecting edges need to match. Therefore, it is necessary to subdivide the domain into parts to match the number of nodes on each side. Between the refinement box and the rest of the domain is a padding, that connects the refined edges to the unrefined edges
![Inhomogeneous compression problem with mesh transfinite entities](Images/inhomoComProblem_withTransfiniteCurves.png)
