# __author__ = '310038541'
# Using utf-8

import numpy as np

import parameters


def spd2xy(spd):
    wavelength = spd[:, 0]
    power = spd[:, 1]
    interp_spd = np.interp(parameters.wavelength, wavelength, power)
    length = len(parameters.wavelength)
    X = np.zeros(length)
    Y = np.zeros(length)
    Z = np.zeros(length)

    for i in (0, length):
        X[i] = interp_spd[i] * parameters.x_bar[i]
        Y[i] = interp_spd[i] * parameters.y_bar[i]
        Z[i] = interp_spd[i] * parameters.z_bar[i]

    sum_X = sum(X)
    sum_Y = sum(Y)
    sum_Z = sum(Z)

    x = sum_X / (sum_X + sum_Y + sum_Z)
    y = sum_Y / (sum_X + sum_Y + sum_Z)

    return x, y