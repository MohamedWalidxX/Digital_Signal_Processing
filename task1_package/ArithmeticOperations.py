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


def readFile_returnMinMax(path):
    max_y = float('-inf')
    min_y = float('inf')

    # Step 2: Read the file and find max and min values
    with open(path, 'r') as file:
        lines = file.readlines()[3:]
        for line in lines:
            x, y = map(float, line.strip().split())
            max_y = max(max_y, y)
            min_y = min(min_y, y)
    return min_y, max_y


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
    y_plot = abs(np.subtract(y1, y2))
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
    y1 = np.multiply(y1, y1)
    draw_signal2(x1, y1)


def shift_signal(path, shiftAmount):
    x1, y1 = readFile_returnArray(path)
    x1 = np.array(x1) - shiftAmount
    draw_signal2(x1, y1)


def normalize(path, a, b):
    # Read the signal file
    x, y = readFile_returnArray(path)

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
    x, y = readFile_returnArray(path)

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


def quantize_signal(file_path, levels, isConverted):
    if isConverted == 0:
        levels = 2 ** levels
    x, y = readFile_returnArray(file_path)
    mini, maxi = readFile_returnMinMax(file_path)
    # Calculate delta
    delta = (maxi - mini) / levels

    # Step 3: Create an array of pairs
    quantization_levels = []

    # Step 4: Fill the pairs
    current_value = mini
    for i in range(levels):
        quantization_levels.append((current_value, current_value + delta))
        current_value += delta

    # Step 5: Create a list of averages
    averages = [(pair[0] + pair[1]) / 2 for pair in quantization_levels]
    quantized_y = []
    group_of_Sample = []
    encoded_group_of_samples = []
    error_sum = 0
    for i in range(len(y)):
        miniDistanceAvg = 2e9
        group = -1
        for j in range(len(averages)):
            if abs(y[i] - averages[j]) < miniDistanceAvg:
                group = j
                miniDistanceAvg = abs(y[i] - averages[j])
        quantized_y.append(averages[group])
        group_of_Sample.append(group)
        encoded_group_of_samples.append(bin(group)[2:])
        sample_error = y[i] - averages[group]
        error_sum += sample_error ** 2

    print(quantized_y)
    print(encoded_group_of_samples)
    print(error_sum / len(y))
    draw_signal2(x, quantized_y)
    return error_sum / len(y), encoded_group_of_samples, quantized_y



def discrete_fourier_transform(input_file, fs):
    N = len(samples)
    amplitudes = []
    phases = []

    for k in range(N):
        real_part = 0
        imag_part = 0

        for n in range(N):
            angle = 2 * np.pi * k * n / N
            real_part += samples[n] * np.cos(angle)
            imag_part -= samples[n] * np.sin(angle)

        amplitude = np.sqrt(real_part ** 2 + imag_part ** 2)
        phase = np.degrees(np.arctan2(imag_part, real_part))

        amplitudes.append(amplitude)
        phases.append(phase)

    return amplitudes, phases


# Example usage:
samples = [0, 1, 2, 3]
amplitudes, phases = discrete_fourier_transform(samples)
print("Amplitudes:", amplitudes)
print("Phases (in degrees):", phases)


def inverse_discrete_fourier_transform(real, imaginary):
    print("Not implemented yet")
def modify_component(idx,amplitude,phase):
    print("Not implemented yet")