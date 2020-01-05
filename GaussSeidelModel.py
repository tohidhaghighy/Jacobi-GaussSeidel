import numpy as np

class GausssSeidel:
    #make object from class
    def __init__(self,matrix):
        self.matrix=matrix

    def makematrix(self,R,C):
        matrix=[]
        for i in range(C):          # A for loop for row entries 
            a =[] 
            for j in range(R):      # A for loop for column entries 
                 a.append(float(input("Enter newNumber row {} column {} ".format(i,j)))) 
            matrix.append(a) 
        return np.array(matrix) 

    def gauss_func(self,c,x,d):
        # Gauss–Seidel
        epsilon = 0.001
        x_d = np.ones(d.shape)
        x_new = x.copy()
        a=1
        while(not(x_d<epsilon).all()):
            x = x_new.copy()
            x_new = x.copy()
            for r in range(x.shape[0]):
                x_new[r] = c[r,:] @ x_new + d[r]
            print(a)
            a+=1
            print(x_new)
            x_d = abs(x_new - x)
