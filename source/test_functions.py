# __author__ = 'Zeng, Xu'
# using utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import parameters

plt.plot(parameters.wavelength, parameters.r_bar)
plt.plot(parameters.wavelength, parameters.g_bar)
plt.plot(parameters.wavelength, parameters.b_bar)
plt.show()


plt.plot(parameters.wavelength, parameters.x_bar)
plt.plot(parameters.wavelength, parameters.y_bar)
plt.plot(parameters.wavelength, parameters.z_bar)
plt.show()
