#encoding:utf-8
from __future__ import division 
import random
# 计算事件 B 和事件 L 的交集“两个孩子都是女孩，并且至少一个孩子是女孩”的概率
# P(B|L) = P(B, L) / P(L) = P(B) / P(L) = 1/4 / 3/4 = 1/3
def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girls = 0
either_girls = 0

random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girls += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girls += 1

print "P(both | older): ", both_girls / older_girls # 0.154 ~ 1/2
print "P(both | either): ", both_girls /either_girls # 0.342 ~ 1/3