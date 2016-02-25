# CFD Simulation Case Setup

**The created CFD domain is now read into the CFD package of interest to set the CFD simulation up. It should be noted that the current tutorial has a significant difference compared to other available CFD tutorials online! This tutorial is structured and developed based on a generic and methodological approach to set up a CFD simulation. The first principals and reasonings for each setting is discussed at each step. Potential alterations and modifications to perform similar analysis are also addressed and discussed. Hence, in the end user will have the capability of applying potential modifications, improvements or extending the application of the current CFD simulation to a more complex problem of interest in the end of the tutorial, rather than having a one time successful run of a specific simulation with specific and strictly pre-defined boundary conditions.**

> **_In simple words: Current tutorial teaches users to fish, rather than giving them a fish._**

## Setting up a CFD simulation has following four steps:  
The summary of the steps to take for CFD simulation setup for problem of laminar flow in a circular pipe are as follows:

 1-  `/define/models/steady`   
 2-  `/define/models/solver/pressure-based`    
 3-  `/define/models/viscous/laminar`    
 4-  `/define/material/change-create`    
 5-  `/define/boundary-conditions/fluid`   
 6-  `/define/boundary-conditions/velocity-inlet`    
 7-  `/define/boundary-conditions/pressure-outlet`   
 8-  `/define/boundary-conditions/wall`    
 9-  `solve/set/discretization-schem`    
 10- `solve/set/under-relaxation`   
 11- `/solve/initialize/compute-defaults/velocity-inlet`    
 12- `solve/iterate`

Following is the step-by-step explanation for each of the above command/setting procedure. It should be noted that the path for defining conditions and other settings that are provided in `command line` format. Users can access exact same settings and options by following the provided path via the tree of progress or pull down menu in ANSYS FLUENT.

1. ###### Setup Model/s:   
According to the physics of the flow field user will select required model/s to simulate the flow.

2. ###### Setup Working Fluid/s & Solid/s:   
User will define the physical and thermodynamical properties of the working fluid/s and solid/s in the problem.    

3. ###### Setup Boundary & Zone Conditions:    
Solving the governing equations of the flow (i.e. system of partial differential equations) requires well-defined boundary conditions within the CFD domain. These conditions are selected and defined in this step.

4. ###### Setup Solution Methods:    
In CFD simulations the governing equations of the flow are solve numerically. Based on the physics of the problem appropriate numerical schemes and solution methods are selected at this step.

 In the following section the details for the above four steps for the CFD simulation setup for **Laminar Flow in Circular Pipe** are explained in great details. It should be noted that the path for defining conditions and other settings are provided in `command line` format. Users can access exact same settings and options by following the provided path via the tree of progress or pull down menu in ANSYS FLUENT:

**1. Setup Model/s:**
* The current flow field of interest in majority of applications is steady. Meaning that the an almost constant and uniform flow will enter the pipe and evolves along it. Therefore, the steady model is chosen: `/define/models/steady`. In case the flow rapidly changes with respect to time the Transient model should be chosen in this step.  

* In majority of industrial applications the speed of the flow in pipe is defined in subsonic region. Therefore, variation of density with respect to the pressure can be neglected. As a result of this assumption one can define the working fluid to be incompressible: `/define/models/solver/pressure-based`. In cases that the speed of the flow enters sonic and supersonic regions, the changes in density (i.e. compressibility) of the flow will be an important factor and the solver must be defined as density-based.

* In the current problem the flow is viscous and value of Reynold number based on the diameter of the pipe is 100. Therefore, the flow regime is laminar and the appropriate model for that is selected via :`/define/models/viscous/laminar`. It is important to note that the critical Reynolds number, based on the paper by Osborn Reynolds, is 2300 when the regime of the flow starts to become turbulent. In such cases the model will still be viscous, however the appropriate turbulent model should be selected at this step.

**2. Setup Working Fluid/s & Solid/s:**  
* The working material is chosen to be Air for this problem `/define/material/change-create`. In most of the CFD packages, air is defined is the default working fluid. However, it can be modified through this menu using the pre-defined materials or defining a new material with unique physical and thermodynamical properties.

**3. Setup Boundary and Zone Conditions:**    
* In this problem the entire CFD domain is filled with the working fluid (i.e. Air). This working fluid is selected form the defined material/s in the previous step:`/define/boundary-conditions/fluid`. Select Air from the available lists of materials.

* The flow enters from the inlet face of the CFD domain with constant velocity of 0.01 [m/s] in x-direction. User sets the inlet face to a velocity-inlet condition by defining the direction and magnitude of the velocity: `/define/boundary-conditions/velocity-inlet`.
In cases where the incoming velocity into the CFD domain is not uniform one can define the incoming velocity with the pre-defined directions or generate a User Define Function (UDF) to describe the velocity profile of interest.

* The flow exits the pipe from the outlet face and it's pressure will be equal to atmospheric pressure. `/define/boundary-conditions/pressure-outlet`. It is assumed that gauge pressure at this face is equal to 0. If in the problem of interest, there exist a specific pressure difference between the inlet and outlet, that magnitude can be defined in inlet and the outlet of the pipe.

* The flow is bounded by pipe's walls and interact with them based on the no-slip boundary condition. User assign the no-slip boundary condition to the wall faces of the CFD domain: `/define/boundary-conditions/wall`. If the shear forces and formed boundary layer becomes important in this region user should either provide required mesh resolution to capture the phenomena or set this boundary to free slip condition such that fluid elements would not interact with wall region.

**4. Setup Solution methods:**   
In this step, it is highly recommended to use the default options and settings, unless based on physics of the problem the user is aware of any specific choices. Upon non-smooth convergence and potential divergence of the CFD simulation user can modify and examine various solution methods. To modify the solution methods and controls use the following commands respectively:

`solve/set/discretization-schem`

`solve/set/under-relaxation`

Now all boundary conditions and settings for the CFD simulation are defined. User can **initialize** the solution through an educated guess to start the iteration process: `/solve/initialize/compute-defaults/velocity-inlet`
Solution initialization would incept the flow field variables, such as velocity and pressure, based on the defined values by user. For the current problem the CFD domain is recommended to be initialize by values of velocity and pressure at the pipe's inlet.

Iteration process for solving the flow field governing equation now shall start till converged solution is obtained:`solve/iterate`. A general rule of thumb for converged solution is to have continuity residuals of 10-3. More details about commenting on validity of solution and convergence criteria will be discussed in next section.
