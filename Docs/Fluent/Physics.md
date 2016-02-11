# CFD Problem's Physics & Theory

**In developing CFD simulations understanding the problem's general physics and fundamental theory is extremely valuable and important. This would provide us the foundation for implementation and later validation of our CFD simulation. Understanding the theory would provide us knowledge to decide about the CFD domain scales, required boundary conditions and general form for numerical results. Let's review the fundamental physics and theory of the "Laminar Flow in a Circular pipe":**

In order to introduce the general physics of the flow in a circular pipe start with the general Navier-Stokes equation as follows:

<img src="./Images/lex-smits-8.2.png" width="200">

Assume a streamwise flow (2D), laminar and steady flow in the pipe. Then the general Navier-Stokes equation will be simplified to:

<img src="./Images/lex-smits-8.3.png" width="200">

In order to solve the above equation, to obtain the general velocity profile and pressure drop across the pipe we consider:

<img src="./Images/lex-smits-8.13.png" width="200">

<img src="./Images/lex-smits-8.14.png" width="200">

Integrating the fourth equation would result into the general velocity profiles with two constants C1 and C2. Applying the no slip boundary conditions as follows:

[insert equation for so slip B.C.],
[insert equation for symmetry B.C.],

would lead into a determined system of two equations and two unknowns and gives values for C1 and C2. Hence, the general form of velocity profile will be as follows:

<img src="./Images/lex-smits-8.15.png" width="200">

In this equation K' is the only undefined variable. Considering the average velocity across the cross section of the duct one can write:

<img src="./Images/lex-smits-8.16.png" width="200">

As a result of this algebraic manipulation the general form of velocity profile and pressure gradient across the pipe will be as follows:

<img src="./Images/lex-smits-8.18.png" width="200">

<img src="./Images/lex-smits-8.17.png" width="200">

> For more details on the physics, theory and equation derivation please see chapter 8 of "A Physical Introduction to Fluid Mechanics by Alexander J. Smits" 2nd edition. [Download Book Here!](http://www.efluids.com/efluids/books/efluids_books.htm)
