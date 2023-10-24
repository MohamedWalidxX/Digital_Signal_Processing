import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import sino_waves as si
import cosine_wave as cs
from tkinter import messagebox

from tkinter import *

import numpy as np
import matplotlib.pyplot as plt


def normalize(path, a, b):
    # Read the signal file
    data = np.loadtxt(path)

    # Extract x and y values from the signal file
    x = data[:, 0]
    y = data[:, 1]

    # Calculate the minimum and maximum values of y
    y_min = np.min(y)
    y_max = np.max(y)

    # Normalize the signal
    normalized_y = ((y - y_min) / (y_max - y_min)) * (b - a) + a

    # Plot the normalized signal
    plt.plot(x, normalized_y)
    plt.xlabel('x')
    plt.ylabel('Normalized y')
    plt.title('Normalized Signal')
    plt.show()


import numpy as np
import matplotlib.pyplot as plt


def accumulate(path):
    # Read the signal file
    data = np.loadtxt(path)

    # Extract y values from the signal file
    y = data[:, 1]

    # Calculate the accumulated sum
    accumulated_y = np.cumsum(y)

    # Plot the accumulated sum
    plt.plot(accumulated_y)
    plt.xlabel('n')
    plt.ylabel('Accumulated y')
    plt.title('Accumulated Sum of Signal')
    plt.show()

    return accumulated_y

