#encoding:utf-8
from __future__ import division 
import sys 
import math
sys.path.append('../ch6-probability')
import continuous_distribution_h as distribution

# 抛硬币
def normal_approximation_to_binomial(n, p):
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# 正态 cdf 是一个变量在一个阈值下的概率
normal_probability_below = distribution.normal_cdf

# 如果它不在阈值以下，就在阈值之上
def normal_probability_above(lo, mu = 0, sigma = 1):
    return 1 - distribution.normal_cdf(lo, mu, sigma)

# 如果它小于 hi 但不比 lo 小，那么它在区间之内
def normal_probability_between(lo, hi, mu = 0, sigma=1):
    return distribution.normal_cdf(hi, mu, sigma) - distribution.normal_cdf(lo, mu, sigma)

# 如果不再区间内，那就在区间外
def normal_probability_outside(lo, hi, mu = 0, sigma = 1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

# 找出非尾区域
def normal_upper_bound(probability, mu = 0, sigma = 1):
    return distribution.inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu = 0, sigma = 1):
    return distribution.inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_side_bounds(probability, mu = 0, sigma = 1):
    tail_probability = (1 - probability) / 2
    # 上界应有在它之上的 tail_probability
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    # 下界应有在它之下的 tail_probability
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound

# 以下验证与对抛硬币符合均匀分布的假设是正确的
# 抛 1000 次硬币，如果关于均匀分布的假设正确，那么近似服从正态分布，均值为 50，标准差为 15.8
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
print "mu_0 =" , mu_0 , " ,sigma_0 =" , sigma_0
# 显著性，避免第一类错误，出于历史原因，容错率一般设为 1-5%，这里我们使用 5%
# 当 X 落在以下区域之外就拒绝原假设
normal_two_side_bounds(0.95, mu_0, sigma_0)

# 基于假设 p 是 0.5 时 95% 的边界
lo, hi =normal_two_side_bounds(0.95, mu_0, sigma_0)

# 基于 p = 0.55 的真实 mu 和 sigma
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# 第 2 类错误意味着我们没有拒绝原假设
# 这会在 X 任然在最初的区间时发生
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability
print "power:", power

# 如果把假设改为抛硬币的结果不会偏重于正面朝上，即 P <= 0.5，这种情况下，使用单边检验
hi = normal_upper_bound(0.95, mu_0, sigma_0)
# 是 526 （< 531，因为在丄尾需要更多的概率）
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability
print "power:", power

# 校验硬币双面是否均匀
def two_sided_p_value(x, mu = 0, sigma = 1):
    if x >= mu:
        # 如果 x 大于均值，tail 表示比 x 大多少
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # 如果 x 小于均值，tail 标识比 x 小多少
        return 2 * normal_probability_below(x, mu, sigma)

# 如果我们希望希望看到结果中有 530 次正面朝上，可以这样计算
print "p_0:", two_sided_p_value(529.5, mu_0, sigma_0)

