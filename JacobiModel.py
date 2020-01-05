import numpy as np

class Jacobi:
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

    def jacobi_func(self,c,x,d):
        # Jacobi
        epsilon = 0.001
        x_d = np.ones(d.shape)
        x_new = x.copy()
        a=1
        while(not(x_d<epsilon).all()):
            x = x_new.copy()
            x_new = c@x+d
            print(a)
            print(x_new)
            a+=1
            x_d = abs(x_new - x)
