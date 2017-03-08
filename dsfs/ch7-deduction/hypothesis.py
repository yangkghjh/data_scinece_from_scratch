#encoding:utf-8
from __future__ import division 

# 抛硬币
def normal_approximation_to_binomial(n, p):
    mu = p * n
    sigma - math.sqrt(p * (1 - p) * n)
    return mu, sigma

