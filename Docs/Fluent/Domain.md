# CFD Domain's Creation & Discretization

** After review of the physics and theory behind the problem of interest, to simulate and study the flow field a CFD/Computational domain will be created and discretized into small finite elements/volumes. The flow field's governing equations are solved numerically inside the discretized elements/volumes via an iterative process till a converged solution inside the CFD domain is obtained. This section explains the process of creation and discretization of CFD domain for the problem of interest. **

The CFD domain for the laminar flow in a circular pipe is a finite cylinder with a circular cross section as shown in figure 1. The dimensions of this pipe such as the length and diameter depends on the problem definition. For this specific problem the ratio of length to diameter is equal to 50 (i.e. L = 5 [m] , D = 0.1 [m]). This ratio guarantees that the CFD domain will not have large number of mesh elements, however it will have the appropriate length to simulate various aspects of the flow field as it evolves from the inlet to the outlet of the pipe (positive x direction).

<img src="./Images/CFD_domain_full.png" width="500">

After the CFD domain is created, it should be discretized. The discretization of a CFD domain is the process of "chopping" the domain into small finite elements and/or volumes, wherein the flow field's governing equations will be solved numerically. Discretization of the domain into geometrically well defined finite elements and/or volumes leads to smoother and more promising numerical solution. Furthermore, based on the problem's complexity, physical or geometrical, controllability of the mesh resolution within the domain becomes very important. In this problem in order to increase the level of controllability of the mesh the cylinder was divided into four identical sub-sections, as shown in figure 1, that will be meshed using identical meshing strategy.

Producing a high quality 3D mesh, first requires high quality and geometrically well defined surface mesh elements. Therefore, discretization process for this problems starts with creation of finite surface mesh elements at the pipe inlet face. Boarder lines for each quarter of the inlet face are divided into 10 mesh elements as shown on right hand side of figure 2. Then, the surfaces are meshed using appropriate meshing algoritem of choice as shown on left hand side of figure 2.

<img src="./Images/CFD_domain_inlet_linemesh.png" width="235"> <img src="./Images/CFD_domain_inlet_facemesh.png" width="235">

It is important to highlight that the current meshing strategy, dividing the CFD domain into four sub-sections, would provide us full controllability on mesh resolution close to the pipe's walls or center. Upon mesh refinement requirement it is sufficient to concentrate more nodes on the surface edges close to the region of interest (the detail of these strategies will be discussed for other simulations as required).

At this stage the surface discretization is performed along the length of the channel, on the two perpendicular surfaces in the center of channel. The distribution of mesh element is uniform and 500 mesh elements are created along each length. Right and left hand sides of figure 2 visualizes the line and surface mesh elements on the center plane.

<img src="./Images/CFD_domain_center_linemesh.png" width="235">
<img src="./Images/CFD_domain_center_facemesh.png" width="235">

At this stage the surface meshes at the inlet surface can be extruded along the pipe length mesh elements to create the finite volume mesh elements as visualized in right side of figure 3. Repeating this process for the remaining three volumes would result into discretization of the entire CFD domain into finite volume mesh elements shown on left side of figure 3.

<img src="./Images/CFD_domain_halve_vol_mesh.png" width="235">
<img src="./Images/CFD_domain_cut_vol_mesh.png" width="235">

In this stage the CFD domain is completely discretized and ready to be setup for a CFD simulation. The CFD simulation setup will be discussed in the following section.  

> The complete mesh file (.msh) can be downloaded here [Download Mesh Here!](link)
