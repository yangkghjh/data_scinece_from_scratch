#encoding:utf-8
from __future__ import division 
import math
import matplotlib
matplotlib.use('Agg')
from matplotlib.font_manager import *  
from matplotlib import pyplot as plt
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

# 定义自定义字体，文件名从1.b查看系统中文字体中来  
myfont = FontProperties(fname='/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc')  
# 解决负号'-'显示为方块的问题  
matplotlib.rcParams['axes.unicode_minus']=False
# 绘制正态分布的概率密度函数
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma = 1) for x in xs], '-', label = 'mu = 0, sigma = 1')
plt.plot(xs, [normal_pdf(x, sigma = 2) for x in xs], '--', label = 'mu = 0, sigma = 2')
plt.plot(xs, [normal_pdf(x, sigma = 0.5) for x in xs], ':', label = 'mu = 0, sigma = 0.5')
plt.plot(xs, [normal_pdf(x, mu = -1) for x in xs], '-.', label = 'mu = -1, sigma = 1')
plt.legend()
plt.title(u"多个正态分布概率密度函数", fontproperties=myfont)
plt.draw()
plt.savefig("./normal_distribution_pdf.png")
plt.close('all') 

def normal_cdf(x, mu = 0, sigma = 1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# 绘制正态分布的累计分布函数
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma = 1) for x in xs], '-', label = 'mu = 0, sigma = 1')
plt.plot(xs, [normal_cdf(x, sigma = 2) for x in xs], '--', label = 'mu = 0, sigma = 2')
plt.plot(xs, [normal_cdf(x, sigma = 0.5) for x in xs], ':', label = 'mu = 0, sigma = 0.5')
plt.plot(xs, [normal_cdf(x, mu = -1) for x in xs], '-.', label = 'mu = -1, sigma = 1')
plt.legend()
plt.title(u"多个正态分布的累计分布函数", fontproperties=myfont)
plt.draw()
plt.savefig("./normal_distribution_cdf.png")
plt.close('all') 

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

value_0_3 = inverse_normal_cdf(0.3)
print 'p(0.3) = %f' %value_0_3

# 中心极限定理
def bernoulli_trial(p):
    return 1 if random.random() < p else 0
# 伯努利随机变量
def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

# 绘制正态分布和伯努利随机变量的分布
def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]

    # 用条形图绘制二项式分布条形图
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
        [v / num_points for v in histogram.values()],
        0.8,
        color = '0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # 用线形图绘出正态近似
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
    for i in xs]
    plt.plot(xs, ys)
    plt.title(u"伯努利随机变量二项式分布与正态分布近似", fontproperties=myfont)
    plt.draw()
    plt.savefig("./bernoulli_uniform.png")
    plt.close('all')

make_hist(0.75, 100, 10000)