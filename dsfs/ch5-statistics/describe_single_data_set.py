#encoding:utf-8
from __future__ import division  
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import random
import math
from collections import Counter
from matplotlib import pyplot as plt
import sys 
sys.path.append('../ch5-linear')
import vector_h 

# 产生数据集
num_friends = [random.randint(1,100) for _ in range(100)]

# 绘制直方图
frineds_counts = Counter(num_friends)
xs = range(101)
ys = [frineds_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Number of frineds")
plt.xlabel("num")
plt.ylabel("frineds")
plt.draw()
plt.savefig("./describe_single_data_set.png")

# 数据集大小
num_points = len(num_friends)
print "Number of data set: %d" %num_points

# 数据集的最大值和最小值
largest_value = max(num_friends)
smallest_value = min(num_friends)
print "Largest value: %d" %largest_value
print "Smallest value: %d" %smallest_value

# 其他位置
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]
print "Second largest value: %d" %second_largest_value
print "Second smallest value: %d" %second_smallest_value

# 均值
def mean(x):
    return sum(x) / len(x)

mean_of_frineds = mean(num_friends)
print "Mean of frineds: %d" %mean_of_frineds

# 中位数
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint

        return (sorted_v[lo] + sorted_v[hi]) / 2

median_of_frineds = median(num_friends)
print "Median of frineds: %d" %median_of_frineds

# 分位数
def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

quantile_10 = quantile(num_friends, 0.10)
quantile_25 = quantile(num_friends, 0.25)
quantile_75 = quantile(num_friends, 0.75)
quantile_90 = quantile(num_friends, 0.90)
print "Quantile 10%%: %d" %quantile_10
print "Quantile 25%%: %d" %quantile_25
print "Quantile 75%%: %d" %quantile_75
print "Quantile 90%%: %d" %quantile_90

# 众数
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
        if count == max_count]

print "Mode:"
print mode(num_friends) 

# 极差
def data_range(x):
    return max(x) - min(x)

frineds_range = data_range(num_friends)
print "Data range: %d" %frineds_range

# 方差
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def sum_of_squarse(x):
    return sum([x_i * x_i for x_i in x])

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squarse(deviations) / (n - 1)

data_variance = variance(num_friends) 
print "Variance: %d" %data_variance

# 标准差
def standard_deviation(x):
    return math.sqrt(variance(x))

data_standard_deviation = standard_deviation(num_friends)
print "Standard deviation: %d" %data_standard_deviation

# 75% 分位数和 25% 分位数之差
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

interquartile_range = interquartile_range(num_friends)
print "Interquartile range: %d" %interquartile_range

# 5.2 相关
# 产生每日在线时长数据集
daily_minutes = [random.randint(1,60) for _ in range(100)]

# 协方差
def covariance(x, y):
    n = len(x)
    return vector_h.dot(de_mean(x), de_mean(y)) / (n - 1)

data_covariance = covariance(num_friends, daily_minutes)
print "Covariance: %d" %data_covariance

# 相关（探查线性相关度，-1 至 1）
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0

data_correlation = correlation(num_friends, daily_minutes)
print "Correlation: %f" %data_correlation

# 排除异常值（假设异常值为第 100 位）
outlier = num_friends.index(100)
num_friends_good = [x
    for i, x in enumerate(num_friends)
    if i != outlier]
daily_minutes_good = [x
    for i, x in enumerate(daily_minutes)
    if i != outlier]

data_correlation = correlation(num_friends_good, daily_minutes_good)
print "Correlation good: %f" %data_correlation