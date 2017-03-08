#encoding:utf-8
from __future__ import division 
import math
import random
from collections import Counter
# 连续分布 uniform distribution

# 使用概率密度函数（probability density function, pdf）来描述连续分布的概率

# 均匀分布的密度函数如下：
def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

# 累计分布函数（cumulative distribution function）用于描述一个随机变量小于等于某个值的概率
def uniform_cdf(x):
    if x < 0 : return 0
    elif x < 1 : return x
    else : return 1

# 正态分布 normal distribuction
def normal_pdf(x, mu = 0, sigma = 1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

def normal_cdf(x, mu = 0, sigma = 1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# 基于二分查找的 cdf 逆运算
def inverse_normal_cdf(p, mu = 0, sigma = 1, tolerance = 0.00001):
    # 如果非标准型，先调整单位使之服从标准型
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance = tolerance)
    
    low_z, low_p = -10.0, 0           # normal_cdf(-10) 接近 0
    hi_z, hi_p = 10.0, 1              # normal_cdf(10)  接近 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2    # 获取中点
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            # midpoint 低，下一步搜索比他大的区域
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint 高，下一步搜索比他小的区域
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z

# 中心极限定理
def bernoulli_trial(p):
    return 1 if random.random() < p else 0
# 伯努利随机变量
def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

# 绘制正态分布和伯努利随机变量的分布
def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]