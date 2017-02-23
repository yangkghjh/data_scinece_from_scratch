#encoding:utf-8
import math

# 向量相加
def vector_add(v, w):
    return [v_i + w_i
        for v_i, w_i in zip(v, w)]
# 向量相减
def vector_subtract(v, w):
    return [v_i - w_i
        for v_i, w_i in zip(v, w)]
# 多个向量累加
def vector_sum(v, w):
    return reduce(vactor_add, vectors)
# 向量乘标量
def scalar_multiply(c, v):
    return [c *v_i for v_i in v]
# 计算一系列向量的均值
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))
# 点乘
def dot(v, w):
    return sum(v_i * w_i
        for v_i, w_i in zip(v,w))
# 计算一个向量的平方和
def sum_of_squares(v):
    return dot(v, v)
# 计算向量的大小（长度）
def magintude(v):
    return math.sqrt(sum_of_squares(v))
# 计算两个向量距离的平方
def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))
# 计算两个向量的距离，两种等价实现
# def distance(v, w)
#     return math.sqrt(squared_distance(v, w))
def distance(v, w):
    return magintude(squared_distance(v, w))