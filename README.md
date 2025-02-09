# Gmsh_python
Some applications from the Gmsh Python interface. Reference was taken from:  
<https://gitlab.onelab.info/gmsh/gmsh/blob/gmsh_4_13_1/api/gmsh.py>

---

## Defining Gmsh properties  
*(Text below taken from **Section 13** in [Gmsh documentation](https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-application-programming-interface))*

> **How do I define boundary conditions or material properties in Gmsh?**  
> By design, Gmsh does not try to incorporate every possible definition of boundary conditions or material properties—this is a job best left to the solver. Instead, Gmsh provides a simple mechanism to tag groups of elements, and it is up to the solver to interpret these tags as boundary conditions, materials, etc. Associating tags with elements in Gmsh is done by defining physical groups (Physical Points, Physical Curves, Physical Surfaces and Physical Volumes). See the reference manual as well as the tutorials (in particular t1) for a detailed description and some examples.  
>
> The Gmsh API can be used to build sophisticated interactive workflows where the definition of boundary conditions and material properties can be fully tailored to your preferred solver. For an example see `examples/api/prepro.py`.

---

## Example Mesh: Inhomogeneous Compression Problem

![Inhomogeneous compression problem; left: problem description; right: deformed mesh at the limit point (Q2, n_ele = 1125, γ_c = 1.03).](.images/Screenshot 202025-02-09 20184141_Bieber.png)


This figure shows one of the meshes which will be defined in this repository. It illustrates an inhomogeneous compression problem, where you can see the deformation of a rectangular domain under an applied load.  
