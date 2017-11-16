
# big five numbers
import pandas as pd

a = [7.1, 10.6, 11.2, 9.0, 8.5, 10.9, 7.8]

s = pd.Series(a)

s.describe()

lab1 = [2.9, 3.1, 3.1, 3.7, 3.1, 4.2, 3.7, 3.9, 3.1, 3.0, 2.9]
lab2 = [2.7, 3.4, 3.6, 3.2, 4.0, 4.1, 3.8, 3.8, 4.3, 3.4, 3.3]
lab3 = [3.3, 3.3, 3.5, 3.5, 2.8, 2.8, 3.2, 2.8, 3.8, 3.5, 3.8]
lab4 = [3.3, 3.2, 3.4, 2.7, 2.7, 3.3, 2.9, 3.2, 2.9, 2.6, 2.8]
lab5 = [4.1, 4.1, 3.7, 4.2, 3.1, 3.5, 2.8, 3.5, 3.7, 3.5, 3.9]

pd.Series(lab1).describe()
pd.Series(lab2).describe()
pd.Series(lab3).describe()
pd.Series(lab4).describe()
pd.Series(lab5).describe()

d1 = [6, 4, 2]
d2 = [10, 14, 9]
d3 = [9, 12, 6]
d = d1 + d2 + d3

pd.Series(d1).describe()
pd.Series(d2).describe()
pd.Series(d3).describe()
pd.Series(d).describe()

# ANOVA
import statistics as stats
import numpy as np
import pandas as pd
from scipy.stats import f

g1 = [7.3, 8.2, 10.1, 6.0, 9.5]
g2 = [7.1, 10.6, 11.2, 9.0, 8.5, 10.9, 7.8]
g3 = [5.8, 6.5, 8.8, 4.9, 7.9, 8.5, 5.2]
g = g1 + g2 + g3

x1 = stats.mean(g1)
s1 = stats.stdev(g1)
n1 = len(g1)
x2 = stats.mean(g2)
s2 = stats.stdev(g2)
n2 = len(g2)
x3 = stats.mean(g3)
s3 = stats.stdev(g3)
n3 = len(g3)
x = stats.mean(g)

print("x1= {} s1= {}".format(x1, s1))
print("x2= {} s2= {}".format(x2, s2))
print("x3= {} s3= {}".format(x3, s3))
print("x^bar= {}".format(x))

ssg = n1 * (x1 - x)**2 + n2 * (x2 - x)**2 + n3 * (x3 - x)**2
msg = ssg / (3-1)
print("ssg= {} msg= {}".format(ssg, msg))

sse = (n1-1)*s1**2 + (n2-1)*s2**2 + (n3-1)*s3**2
mse = sse / (len(g) - 3)
print("sse= {} mse= {}"x = [80 68 94 72 74 83 56 68 65 75 88].format(sse, mse))

ssto = ssg + sse
print("ssto = {}".format(ssto))
x =
f = msg/mse
# p-val = f.cdf(f, 2, len(g) - 3)
print("f= {}".format(f))



x= [80, 68, 94, 72, 74, 83, 56, 68, 65, 75, 88]
y= [72, 71, 96, 77, 82, 72, 58, 83, 78, 80, 92]

xbar = stats.mean(x)
ybar = stats.mean(y)
print("x_bar= {} y_bar= {}".format(xbar, ybar))

n = len(x)
xerr = [val - xbar for val in x]
yerr = [val - ybar for val in y]

sxx = [val**2 for val in xerr]
syy = [val**2 for val in yerr]
Sxx = sum(sxx)
Syy = sum(syy)

sxy = []
for idx in range(n):
    sxy.append(xerr[idx] * y[idx])

Sxy = sum(sxy)

print("x-x_bar({}) = \n{}".format(sum(xerr), np.array(xerr)))
print("Sxx({:10.4f}) = \n{}".format(Sxx, np.array(sxx)))
print("Sxy({:10.4f}) = \n{}".format(Syy, np.array(sxy)))
print("y-y_bar({}) = \n{}".format(sum(yerr), np.array(yerr)))
print("Syy({:10.4f}) = \n{}".format(Syy, np.array(syy)))


