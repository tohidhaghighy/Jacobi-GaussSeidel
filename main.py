from GaussSeidelModel import GausssSeidel
from JacobiModel import Jacobi
from SuccessiveOverRelaxiation import SuccessiveORelax
import numpy as np

R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 

jacob=Jacobi([])
gaussseidel=GausssSeidel([])
successoverrelax=SuccessiveORelax([])
matrix=jacob.makematrix(R,C)
#Ax=B   -----> x=Cx+D

#print(matrix)

A = np.array([[ 4., -1., -1.],
       [ 6.,  8.,  0.],
       [-5.,  0., 12.]])

b = np.array([-2, 45, 80])

c = -A/(A.diagonal()).reshape((b.size, -1))
np.fill_diagonal(c, 0)
d = b/A.diagonal()
d = d.reshape((d.size, -1))
x = np.zeros(d.shape)

jacob.jacobi_func(c,x,d)
gaussseidel.gauss_func(c,x,d)
successoverrelax.SuccessOverRelaxiation(c,x,d)






