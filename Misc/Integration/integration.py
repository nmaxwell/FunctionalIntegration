

#from scipy import *
import math
import random
#import numpy

def sample(X, n_samples):
    sum1 = 0.
    sum2 = 0.
    for k in range(n_samples):
        x = X()
        sum1 += x
        sum2 += x*x
    
    return sum1/n_samples, math.sqrt((sum2-sum1*sum1/n_samples)/(n_samples*(n_samples-1)))


def mean(X, n_samples):
    return sum((X() for k in range(n_samples)))/n_samples

def std(X, n_samples):

    sum1 = 0.
    sum2 = 0.
    for k in range(n_samples):
        x = X()
        sum1 += x
        sum2 += x*x
        
    return  math.sqrt((sum2-sum1*sum1/n_samples)/(n_samples-1))



X = lambda : random.normalvariate(0,1)
#X = random.random




print( std(X, 100) )

"""
n=1000


results=[]
for k in range(1000):
    exact = 0.5
    xbar,sigm = sample(X, n)
    error = abs(xbar-exact)
    results.append(error <= sigm)

print(sum(results)/1000)

"""

