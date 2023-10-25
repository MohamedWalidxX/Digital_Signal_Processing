import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import sino_waves as si
import cosine_wave as cs
from tkinter import messagebox
from draw import draw_signal2
from tkinter import *


def equalize_arrays(arr1, arr2):
    condition = 0  # which is the smallest variable
    if len(arr1) < len(arr2):
        arr1.extend([0] * (len(arr2) - len(arr1)))
        condition = 1
    elif len(arr2) < len(arr1):
        arr2.extend([0] * (len(arr1) - len(arr2)))
        condition = 2
    return arr1, arr2, condition


def readFile_returnArray(path):
    x_values = []
    y_values = []
    # Read the data from the file, skipping the first three lines
    with open(path, "r") as file:
        lines = file.readlines()[3:]  # Skip the first three lines
        for line in lines:
            x, y = map(float, line.strip().split())
            x_values.append(x)
            y_values.append(y)
    return x_values, y_values


def addSignals(path1, path2):
    x1, y1 = readFile_returnArray(path1)
    x2, y2 = readFile_returnArray(path2)
    y1, y2, condition = equalize_arrays(y1, y2)
    y_plot = np.add(y1, y2)
    if condition == 1:
        draw_signal2(x2, y_plot)
    else:
        draw_signal2(x1, y_plot)


def subtractSignals(path1, path2):
    x1, y1 = readFile_returnArray(path1)
    x2, y2 = readFile_returnArray(path2)
    y1, y2, condition = equalize_arrays(y1, y2)  # extend the samllest array with zeroes
    y_plot = abs(np.subtract(y1,y2))
    if condition == 1:
        draw_signal2(x2, y_plot)
    else:
        draw_signal2(x1, y_plot)


def multiplySignal(path, constNum):
    x1, y1 = readFile_returnArray(path)
    y1 = np.array(y1) * constNum
    draw_signal2(x1, y1)

def square_signal(path):
    x1, y1 = readFile_returnArray(path)
    y1 = np.multiply(y1,y1)
    draw_signal2(x1, y1)

def shift_signal(path, shiftAmount):
    x1, y1 = readFile_returnArray(path)
    x1 = np.array(x1) - shiftAmount
    draw_signal2(x1, y1)

def normalize(path, a, b):
    # Read the signal file
    x,y = readFile_returnArray(path)

    # Extract x and y values from the signal file


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


def accumulate(path):
    # Read the signal file
    x , y =readFile_returnArray(path)

    # Extract y values from the signal file


    # Calculate the accumulated sum
    accumulated_y = np.cumsum(y)

    # Plot the accumulated sum
    plt.plot(accumulated_y)
    plt.xlabel('n')
    plt.ylabel('Accumulated y')
    plt.title('Accumulated Sum of Signal')
    plt.show()

    return accumulated_y
