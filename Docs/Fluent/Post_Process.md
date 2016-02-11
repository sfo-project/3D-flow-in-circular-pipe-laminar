# CFD Results Post-Process
The last step for the development of a CFD simulation of a problem of interest is to process and examine the validity of the obtained numerical results (a.k.a post-processing step). This process is done starting from general inspection on CFD simulation leading to more detail validation.

The first general rule of thumb to check the convergence of a CFD simulation is to visualize the residuals for key flow variables, such as continuity, velocity and etc.. In order to plot residual values in ANSYS FLUENT do: `plot/residual` and choose the residual values of interest to plot.

<img src="./Images/residuals.png" width="550">

Figure 4 visualizes the residual values of continuity and streamwise velocity versus the number of iterations. The general decreasing trend of residual values confirm that the numerical solution of the conservation/governing equations are converging to specific final values. Usually the residual for the mass decreases with the slower rate compare to other residual values. Therefore, a continuity residual of 10E-3, is the first necessary, but not sufficient, general criteria to confirm the convergence of the CFD simulation in general. In this case this criteria is reached after about 50 iterations and after about 500 iterations the continuity residuals reached value of 10E-12, which is a solid confirmation of CFD simulation convergence.

The second step is to visualize dimensionless form of the important variables within the CFD domain. This step can be problem specific and should be done on an adequate plane of choice. For most of the problems contour of normalized velocity or pressure is on a horizontal or vertical plane at the center of the CFD domain is a good start point.
The path to define an adequate plane is `surface/plane-bounded`. This command will ask for coordinate of three different points within the domain to create the plane. For the current CFD domain to define a vertical plane from inlet to 5D downstream the coordinates will be as follows:

x0 (m) = 0   , y0 (m) = 0 , z0 (m)=  0.05

x1 (m) = 0   , y1 (m) = 0 , z0 (m)= -0.05

x2 (m) = 0.5 , y0 (m) = 0 , z0 (m)= -0.05

Once the plane is created one should define the normalized variable of interest. To define the normalized streamwise velocity, by the inlet velocity we will have `define/custom-field-functions/define`, name your variable (i.e. normalized_streamwise_velocity) and put the following formula `x_velocity/0.01`. This will calculate the normalized streamwise velocity within the CFD domain. At this stage the command `display/contour/normalized_streamwise_velocity` will ask you for a range (i.e. [0,2]) and visualizes the velocity contours for you as shown in figure 6:

<img src="./Images/Velocity_cont.png" width="500" align="middle">

As shown in this figure, the flow enters the domain with normalized velocity of 1. Due to the imposed no slip boundary conditions on the pipe's walls, the velocity instantly decrease to zero at this region. Due to this extreme change of momentum within the vertical direction there is going to be a region at the entrance of the pipe where the flow evolves in the streamwise direction. This specific length is referred to as the entrance length. After the entrance length the velocity profile becomes fully developed and uniform to the end of the channel.
It should also be highlighted that this velocity contour is smooth. The smoothness confirms the validity of created mesh resolution and convergence of the numerical solution. However, this is an additional necessary, but not sufficient criteria for simulation validity and convergence.

After performing the general post-processing steps, the user need to perform more detail oriented post-processing to confirm the general validity of the CFD simulation. This stage can be a state-of-the-art. Comparing the numerical results against the theory (discussed earlier) or any other available experimental results is the final stage of post-processing. It is extremely important to calculate the correct corresponding numerical variables and compare them against the experimental or other numerical data.

In order to visualize the evolution of the velocity along the flow one should look at the velocity magnitude at different stations downstream the pipe. Since the flow is axi-symmetric each station is defined as a vertical line at different distances downstream the pipe. One can use `surface/line-surface` command to enter the start and end point of each measurment station as shown in the following table, where D is the distance downstream in terms of diameter:

x0 (m) = x*D   , y0 (m) = 0 , z0 (m)=  0.05
x1 (m) = x*D   , y1 (m) = 0 , z1 (m)=  -0.05

Use of `<this command>` would export the velocity values along each pre-defined station into a text file <link here>. Using a simple script (e.g. Python post-processing script) one can compare the numerical and theoretical results as shown in figure:

<img src="./Images/CFD_domain_halve_vol_mesh.png" width="235">

Figure visualize that at X diameter downstream the pipe numerically predicted velocity profile matches the theoretically calculated velocity ones. This confirms the validity of the developed CFD-simulation to predict the flow behavior in a circular pipe.

The post-processing script to written in Python can be downloaded here. As a practice try to figure out how the entrance length of the pipe is predicted using numerical solutions and how well it is compared against theoritical definition of the entrance length?