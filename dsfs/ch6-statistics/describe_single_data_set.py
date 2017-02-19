#encoding:utf-8
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import random
from collections import Counter
from matplotlib import pyplot as plt

num_friends = [random.randint(1,100) for _ in range(100)]
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