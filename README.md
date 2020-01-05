# Jacobi-GaussSeidel
Jacobi Model &amp; Gauss Seidel Model &amp; Successive Over Relaxation

* Iterative Methods for Linear System of Equations

In computational mathematics, an iterative method is a mathematical procedure that uses an initial guess to generate a sequence of improving approximate solutions for a class of problems, in which the n-th approximation is derived from the previous ones. A specific implementation of an iterative method, including the termination criteria, is an algorithm of the iterative method. An iterative method is called convergent if the corresponding sequence converges for given initial approximations. A mathematically rigorous convergence analysis of an iterative method is usually performed; however, heuristic-based iterative methods are also common.

In contrast, direct methods attempt to solve the problem by a finite sequence of operations. In the absence of rounding errors, direct methods would deliver an exact solution (like solving a linear system of equations A x = b {\displaystyle A\mathbf {x} =\mathbf {b} } A\mathbf {x} =\mathbf {b} by Gaussian elimination). Iterative methods are often the only choice for nonlinear equations. However, iterative methods are often useful even for linear problems involving many variables (sometimes of the order of millions), where direct methods would be prohibitively expensive (and in some cases impossible) even with the best available computing power


* Jacobi Model
 
 when we want to know AX=B -----> x=Cx+D
 
 In numerical linear algebra, the Jacobi method is an iterative algorithm for determining the solutions of a strictly diagonally dominant system of linear equations. Each diagonal element is solved for, and an approximate value is plugged in. The process is then iterated until it converges. This algorithm is a stripped-down version of the Jacobi transformation method of matrix diagonalization. The method is named after Carl Gustav Jacob Jacobi. 
 
 * Guass Seidel Model
 
 In numerical linear algebra, the Gauss–Seidel method, also known as the Liebmann method or the method of successive displacement, is an iterative method used to solve a linear system of equations. It is named after the German mathematicians Carl Friedrich Gauss and Philipp Ludwig von Seidel, and is similar to the Jacobi method. Though it can be applied to any matrix with non-zero elements on the diagonals, convergence is only guaranteed if the matrix is either diagonally dominant, or symmetric and positive definite. It was only mentioned in a private letter from Gauss to his student Gerling in 1823.[1] A publication was not delivered before 1874 by Seidel

