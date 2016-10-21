#!/usr/bin/env python
"""
Created on Fri Oct 14 13:55:03 2016
This Python program is a Jacobi single point iterative solver for a 2-D array. 
We will set the boundary conditions to be constant and then iterate over the sample space
to reach equilibrium. To show this graphically, we will plot a heat map. 
This program is to illustrate the use of 'numpy' and 'matplotlib' libraries. 
Advanced Research Computing Center, University of Wyoming.
"""

# Need to import the numpy and matplotlib library for use
import numpy as np
import matplotlib.pylab as plt

# We need to define a tolerance for our final solution
tol = 1e-06

# We need to define a maximum number of iterations we are willing to do. 
# (so that we don't get stuck in an infinite loop!)
MAX_ITER = 2000

# We cannot set variables as constants in Python so we will use a convenient naming 
# convention that will remind us not to change it. 
CONST_bound_val = 1.0

CONST_initial_guess = 0.0

# To define the size of the sample space (taking a 2-D sqaure matrix)
CONST_size = 4

# Let us now define a square matrix A of size CONST_size*CONST_size that has 
# all elements = CONST_initial_guess
# A_old will contain the starting range of values with boundary conditions
# A_new will contain the range of values as it reaches steady state 
A_old = np.zeros((CONST_size, CONST_size), dtype = float)
A_new = np.zeros((CONST_size, CONST_size), dtype = float)

# REMEMBER: Array indexing in Python starts with 0!

# Since we need a boundary condition to iterate from, we will set all the boundary
# elements in A to be equal to CONST_bound_val
# 1. Setting the elements of the FIRST ROW to be boundary value
A_old[0,:] = CONST_bound_val

# 2. Setting the elements of the LAST ROW 
A_old[CONST_size-1,:] = CONST_bound_val

# 3. Setting the elements of the FIRST COLUMN
A_old[:,0] = CONST_bound_val

# 4. Setting the elements of the LAST COLUMN to the boundary value
A_old[:,CONST_size-1] = CONST_bound_val

# Ensuring that even A_new starts with the same values
A_new = A_old.copy()
B_new = A_new.copy()
B_old = A_old.copy()

# Setting the error to be high enough to start the iterations
err = 1.0

# Starting the iterations with a 'for' loop
print("Starting Jacobi interations on A using slicing...\n")
for iter in range(MAX_ITER): 
# Checking to see if we need to continue with our calculations
	if err >= tol: 
		# In-place computation of simple average of nearest neighbors using slicing
		A_new[1:-1, 1:-1] = 0.25*(A_old[0:-2, 1:-1] + A_old[2:, 1:-1] + A_old[1:-1, 0:-2] + A_old[1:-1, 2:])
		# Computing RMS error by finding the difference and then the square root
		diff = (A_new - A_old).flat
		err = np.sqrt(np.dot(diff, diff))
		# Creating a copy to compute the difference between arrays for error checking
		A_old = A_new.copy()
	else:
		break

# Printing as error message if the desired tolerance is still not reached
if err >= tol: 
	print("The maximum number of iterations has been exceeded before equilibrium was reached")

# Final printing of the solution 
print("The final solution (using slicing) was reached with %d iterations: "%iter)
print(A_new)

err = 1.0

print("Starting Jacobi interations on B using indexing...\n")
for iter in range(MAX_ITER): 
# Checking to see if we need to continue with our calculations
	if err >= tol: 
		# Using element by element indexing to get the average of nearest neighbors
		for i in range(1, CONST_size-1):
			for j in range(1, CONST_size-1):
				B_new[i, j] = 0.25*(B_old[i-1, j] + B_old[i, j-1] + B_old[i+1, j] + B_old[i, j+1])
		# Computing RMS error by finding the difference and then the square root
		diff = (B_new - B_old).flat
		err = np.sqrt(np.dot(diff, diff))
		# Creating a copy to compute the difference between arrays for error checking
		B_old = B_new.copy()
	else:
		break

# Printing as error message if the desired tolerance is still not reached
if err >= tol: 
	print("The maximum number of iterations has been exceeded before equilibrium was reached")

# Final printing of the solution 
print("The final solution (using indexing) was reached with %d iterations: "%iter)
print(B_new)

# Plotting the heatmap
# Choosing the axes size to be between CONST_initial_guess and CONST_bound_val and plotting A_new
im = plt.imshow(A_new, extent = (CONST_initial_guess, CONST_bound_val, CONST_initial_guess, CONST_bound_val)) 
plt.axis('off')
# Show the plot!
# plt.show()
# To save the plot to a .png file that can be viewed later
plt.savefig('heatmap.png')
