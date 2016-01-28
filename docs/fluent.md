
A general methodological/scientific approach to develop a CFD simulation case via ANSYS FLUENT for laminar flow in a circular pipe is explained and discussed here.

The four major steps to develop a CFD simulation case for any fluid mechanics consists the following four steps:

1. **CFD Problem's Physics & Theory**
2. **CFD Domain's Creation & Discretization**
3. **CFD Simulation Case Setup**
4. **CFD Results Post-Process**

This wiki includes the explanation of the above-mentioned steps for the problem of Laminar Flow in a Circular Pipe.


### CFD Problem's Physics & Theory

##### In developing CFD simulations understanding the problem's general physics and fundamental theory is extremely valuable and important. This would provide us the foundation for implementation and later validation of our CFD simulation. Understanding the theory would provide us knowledge to decide about the CFD domain scales, required boundary conditions and general form for numerical results. Let's review the fundamental physics and theory of the "Laminar Flow in a Circular pipe":

In order to introduce the general physics of the flow in a circular pipe start with the general Navier-Stokes equation as follows:

<img src="./imgs/lex-smits-8.2.png" width="200">

Assume a streamwise flow (2D), laminar and steady flow in the pipe. Then the general Navier-Stokes equation will be simplified to:

<img src="./imgs/lex-smits-8.3.png" width="200">

In order to solve the above equation, to obtain the general velocity profile and pressure drop across the pipe we consider:

<img src="./imgs/lex-smits-8.13.png" width="200">

<img src="./imgs/lex-smits-8.14.png" width="200">

Integrating the fourth equation would result into the general velocity profiles with two constants C1 and C2. Applying the no slip boundary conditions as follows:

[insert equation for so slip B.C.],
[insert equation for symmetry B.C.],

would lead into a determined system of two equations and two unknowns and gives values for C1 and C2. Hence, the general form of velocity profile will be as follows:

<img src="./imgs/lex-smits-8.15.png" width="200">

In this equation K' is the only undefined variable. Considering the average velocity across the cross section of the duct one can write:

<img src="./imgs/lex-smits-8.16.png" width="200">

As a result of this algebraic manipulation the general form of velocity profile and pressure gradient across the pipe will be as follows:

<img src="./imgs/lex-smits-8.18.png" width="200">

<img src="./imgs/lex-smits-8.17.png" width="200">

> For more details on the physics, theory and equation derivation please see chapter 8 of "A Physical Introduction to Fluid Mechanics by Alexander J. Smits" 2nd edition. [Download Book Here!](http://www.efluids.com/efluids/books/efluids_books.htm)


### CFD Domain's Creation & Discretization

##### After review of the physics and theory behind the problem of interest, to simulate and study the flow field a CFD/Computational domain will be created and discretized into small finite elements/volumes. The flow field's governing equations are solved numerically inside the discretized elements/volumes via an iterative process till a converged solution inside the CFD domain is obtained. This section explains the process of creation and discretization of CFD domain for the problem of interest.

The CFD domain for the laminar flow in a circular pipe is a finite cylinder with a circular cross section as shown in figure 1. The dimensions of this pipe such as the length and diameter depends on the problem definition. For this specific problem the ratio of length to diameter is equal to 50 (i.e. L = 5 [m] , D = 0.1 [m]). This ratio guarantees that the CFD domain will not have large number of mesh elements, however it will have the appropriate length to simulate various aspects of the flow field as it evolves from the inlet to the outlet of the pipe (positive x direction).

<img src="./imgs/CFD_domain_full.png" width="500">

After the CFD domain is created, it should be discretized. The discretization of a CFD domain is the process of "chopping" the domain into small finite elements and/or volumes, wherein the flow field's governing equations will be solved numerically. Discretization of the domain into geometrically well defined finite elements and/or volumes leads to smoother and more promising numerical solution. Furthermore, based on the problem's complexity, physical or geometrical, controllability of the mesh resolution within the domain becomes very important. In this problem in order to increase the level of controllability of the mesh the cylinder was divided into four identical sub-sections, as shown in figure 1, that will be meshed using identical meshing strategy.

Producing a high quality 3D mesh, first requires high quality and geometrically well defined surface mesh elements. Therefore, discretization process for this problems starts with creation of finite surface mesh elements at the pipe inlet face. Boarder lines for each quarter of the inlet face are divided into 10 mesh elements as shown on right hand side of figure 2. Then, the surfaces are meshed using appropriate meshing algoritem of choice as shown on left hand side of figure 2.

<img src="./imgs/CFD_domain_inlet_linemesh.png" width="235"> <img src="./imgs/CFD_domain_inlet_facemesh.png" width="235">

It is important to highlight that the current meshing strategy, dividing the CFD domain into four sub-sections, would provide us full controllability on mesh resolution close to the pipe's walls or center. Upon mesh refinement requirement it is sufficient to concentrate more nodes on the surface edges close to the region of interest (the detail of these strategies will be discussed for other simulations as required).

At this stage the surface discretization is performed along the length of the channel, on the two perpendicular surfaces in the center of channel. The distribution of mesh element is uniform and 500 mesh elements are created along each length. Right and left hand sides of figure 2 visualizes the line and surface mesh elements on the center plane.

<img src="./imgs/CFD_domain_center_linemesh.png" width="235">
<img src="./imgs/CFD_domain_center_facemesh.png" width="235">

At this stage the surface meshes at the inlet surface can be extruded along the pipe length mesh elements to create the finite volume mesh elements as visualized in right side of figure 3. Repeating this process for the remaining three volumes would result into discretization of the entire CFD domain into finite volume mesh elements shown on left side of figure 3.

<img src="./imgs/CFD_domain_halve_vol_mesh.png" width="235">
<img src="./imgs/CFD_domain_cut_vol_mesh.png" width="235">

In this stage the CFD domain is completely discritized and ready to be setup for a CFD simulation. The CFD simulation setup will be discussed in the following section.  

> The complete mesh file (.msh) can be downloaded here [Download Mesh Here!](link)

### CFD Simulation Case Setup
### CFD Results Post-Process
