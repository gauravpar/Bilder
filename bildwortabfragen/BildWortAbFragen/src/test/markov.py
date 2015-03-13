import  numpy as np
import ghmm

F = ghmm.Float()

A =  [[0.2,0,6,0.2],[0.8, 0.1, 0.1],[0.8, 0.2,0]]
#multivariate gaussian mixture model


B = [ [ [1.0,1.0,0.8][0.56,0.34,0.56,0.12,0.98,0.57]]]

ip=[0.6,0.1,0.3]

SCHMM = ghmm.HMMFromMatrices(F,ghmm.MultivariateGaussianDistribution(F),
A, B, ip)
print SCHMM