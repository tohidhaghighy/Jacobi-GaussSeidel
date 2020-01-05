import numpy as np

class SuccessiveORelax:
    #make object from class
    def __init__(self,matrix):
        self.matrix=matrix

    def SuccessOverRelaxiation(self,c,x,d):
        epsilon = 0.001
        lam = 1.5
        x_d = np.ones(d.shape)
        x_new = x.copy()
        a = 1
        while(not(x_d<epsilon).all()):
            x = x_new.copy()
            x_new = x.copy()
            for r in range(x.shape[0]):
                x_new[r] = ((1-lam) * x_new[r]) + lam * (c[r,:] @ x_new + d[r])
            print(a)
            a += 1
            print(x_new)
            x_d = abs(x_new - x)