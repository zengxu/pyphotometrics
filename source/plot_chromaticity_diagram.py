# __author__ = 'Zeng, Xu'
# Using utf-8

import numpy as np
import matplotlib.pyplot as plt
import parameters

length = len(parameters.x_bar)
X = np.zeros(length)
Y = np.zeros(length)
Z = np.zeros(length)
x = np.zeros(length)
y = np.zeros(length)
for i in (0, length):
    X[i] = parameters.x_bar[i]
    Y[i] = parameters.y_bar[i]
    Z[i] = parameters.z_bar[i]
    x[i] = X[i]/(X[i]+Y[i]+Z[i])
    y[i] = Y[i]/(X[i]+Y[i]+Z[i])

print(length)



