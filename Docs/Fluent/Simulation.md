# CFD Simulation Case Setup

**The created CFD domain, in previous section, is now read into the CFD package of interest to start the development of the CFD simulation. It should be noted that the current tutorial has a significant difference compared to multiple other available CFD tutorials online! This tutorial is structured and developed based on a generic and methodological approach for setting up a CFD simulation. The physical fundamentals and reasonings for each setting is discussed at each step. Potential alterations and modifications are also presented. Hence, users will have the full capability of applying potential modifications, improvements or extending the application of the current the CFD simulation to more complex problems at the end of the tutorial, rather than having a one time successful run of a specific simulation with specific boundary conditions.**

> **_In simple words: Current tutorial teaches users to fish, rather than giving them a fish._**

## Setting up a CFD simulation has following four steps:  
1. ###### Setup Model/s:   
According to the physics of the flow user will select required model/s to simulate the flow. Each model has it's own settings and inputs.

2. ###### Setup Working Fluid/s & Solid/s:   
User will define the physical and thermodynamical properties of the working fluid/s and solid/s in the problem.    

3. ###### Setup Boundary & Zone Conditions:    
Solving the governing equations of the flow requires well-defined boundary and zone conditions within the CFD domain. These conditions are selected and defined in this step.

4. ###### Setup Solution Methods:    
In CFD simulations the governing equations of the flow are solve numerically. Based on the physics of the problem right numerical schemes and solution methods are selected at this step.

Here is the CFD simulation setup for the problem of **Laminar Flow in Circular Pipe**. It should be noted that the path for defining conditions and other settings are provided in `command line` format. Users can access exact same settings and options by following the provided path via the tree of progress or pull down menu in ANSYS FLUENT:

**1. Setup Model/s:**
* The flow is steady state: `/define/models/steady`.   
* The working fluid is incompressible: `/define/models/solver/pressure-based`.
* The flow is viscous and it's regime is laminar:`/define/models/viscous/laminar`.

**2. Setup Working Fluid/s & Solid/s:**  
* The working material is Air:
`/define/material/change-create`. In this menu user can create or change all required physical and thermodynamical properties of the material/s in the model.  

**3. Setup Boundary and Zone Conditions:**    
* In this problem the entire CFD domain is filled with the working fluid. This working fluid is selected form the defined material/s in the previous step:`/define/boundary-conditions/fluid`. Select Air from the available lists of materials.

* The flow enters to the inlet face of CFD domain with constant velocity of 0.01 [m/s] in x-direction. User sets the inlet face to a velocity-inlet condition by defining the direction and magnitude of the velocity: `/define/boundary-conditions/velocity-inlet`.
In cases where the incoming velocity into the CFD domain is not uniform one can select User Define velocity profiles in this option as well.

* The flow exits the pipe from the outlet face and it's pressure will be equal to atmospheric pressure. `/define/boundary-conditions/pressure-outlet`. It is assumed that gauge pressure at this face is equal to 0.

* The flow is bounded by pipe's walls and interact with it based on the no-slip boundary condition. User assign the no-slip boundary condition to the wall faces of the CFD domain: `/define/boundary-conditions/wall`. If the shear forces and formed boundary layer becomes important in this region user should either provide required mesh resolution to capture the phenomena or set this boundary to slip condition such that fluid elements would not interact with wall region.

**4. Setup Solution methods:**   
In this step, it is highly recommended to use the default options and settings, unless based on physics of the problem the user is aware of any specific choices. Upon non-smooth convergence and potential divergence of the CFD simulation user can modify and examine various solution methods. To modify the solution methods and controls use the following commands respectively:

`solve/set/discretization-schem`

`solve/set/under-relaxation`

Now all boundary conditions and settings for the CFD simulation are defined. User can **initialize** the solution through an educated guess to start the iteration process: `/solve/initialize/compute-defaults/velocity-inlet`
Solution initialization would incept the flow field variables, such as velocity and pressure, based on the defined values by user. For the current problem the CFD domain is recommended to be initialize by values of velocity and pressure at the pipe's inlet.

Iteration process for solving the flow field governing equation now shall start till converged solution is obtained:`solve/iterate`. A general rule of thumb for converged solution is to have continuity residuals of 10-3. More details about commenting on validity of solution and convergence criteria will be discussed in next section.
