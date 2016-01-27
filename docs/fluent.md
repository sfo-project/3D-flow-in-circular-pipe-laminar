
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

[insert 8.3 from Lex Smits].

In order to solve the above equation, to obtain the general velocity profile and pressure drop across the pipe we consider:

[insert 8.13 from Lex Smits]
[insert 8.14 from Lex Smits]

Integrating the fourth equation would result into the general velocity profiles with two constants C1 and C2. Applying the no slip boundary conditions as follows:

[insert equation for so slip B.C.],
[insert equation for symmetry B.C.],

would lead into a determined system of two equations and two unknowns and gives values for C1 and C2. Hence, the general form of velocity profile will be as follows:

[insert 8.15 from Lex Smits]

In this equation K' is the only undefined variable. Considering the average velocity across the cross section of the duct one can write:

[insert 8.16 from Lex Smits].

As a result of this algebraic manipulation the general form of velocity profile and pressure gradient across the pipe will be as follows:

[insert 8.18 from Lex Smits].
[insert 8.17 from Lex Smits].

> For more details on the physics, theory and equation derivation please see chapter 8 of "A Physical Introduction to Fluid Mechanics by Alexander J. Smits" 2nd edition. [Download Book Here!](http://www.efluids.com/efluids/books/efluids_books.htm)


### CFD Domain's Creation & Discretization
### CFD Simulation Case Setup
### CFD Results Post-Process
