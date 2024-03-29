import numpy as np
import math
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import sino_waves as si
import cosine_wave as cs
from tkinter import messagebox
from draw import draw_signal2
from tkinter import *
# from inOut.task7.ConvTest import ConvTest
from inOut.task8.CompareSignal import Compare_Signals
from inOut.Convolution.ConvTest import ConvTest


def separate_tuples(list_of_tuples):
    return zip(*list_of_tuples)


def equalize_arrays(arr1, arr2):
    condition = 0  # which is the smallest variable
    if len(arr1) < len(arr2):
        arr1.extend([0] * (len(arr2) - len(arr1)))
        condition = 1
    elif len(arr2) < len(arr1):
        arr2.extend([0] * (len(arr1) - len(arr2)))
        condition = 2
    return arr1, arr2, condition


def readFile_returnDict(path):
    signal_dict = {}
    with open(path, "r") as file:
        lines = file.readlines()[3:]  # Skip the first three lines
        for line in lines:
            x, y = map(float, line.strip().split())
            signal_dict[x] = y
    return signal_dict


def readFile_returnComplexComponents(path):
    x_values = []
    y_values = []
    # Read the data from the file, skipping the first three lines
    with open(path, "r") as file:
        lines = file.readlines()[3:]  # Skip the first three lines
        for line in lines:
            x, y = map(float, line.strip().split())
            x_values.append(x * np.cos(y))
            y_values.append(x * np.sin(y))
    return x_values, y_values


def readFile_returnTuples(path):
    list_of_tuples = []
    with open(path, "r") as file:
        lines = file.readlines()[3:]  # Skip the first three lines
        for line in lines:
            x, y = map(float, line.strip().split())
            list_of_tuples.append((x, y))
    return list_of_tuples


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
    create_file(x1, y1, "shifted.txt")
    draw_signal2(x1, y1)
    return x1, y1


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


def draw_amplitude_phase(amplitudes, phases, fs):
    n = len(amplitudes)
    X = 2 * np.pi / 1 / fs * n
    multiples_of_X = [X * i for i in range(1, n + 1)]
    draw_signal2(multiples_of_X, amplitudes)
    draw_signal2(multiples_of_X, phases)


def create_file(x, y, file_name):
    path = "inOut/task6/"
    path += file_name
    with open(path, 'w') as file:
        # Write the user-chosen numbers
        file.write("{}\n".format(0))  # Replace with your first number
        file.write("{}\n".format(1))  # Replace with your second number

        # Write the size of the amplitudes or phases list
        file.write("{}\n".format(len(x)))

        # Write the amplitudes and phases
        for a, b in zip(x, y):
            file.write("{} {}\n".format(a, b))


def create_file_polar_form(amplitudes, phases):
    path = "inOut/task4/polarForm.txt"
    with open(path, 'w') as file:
        # Write the user-chosen numbers
        file.write("{}\n".format(0))  # Replace with your first number
        file.write("{}\n".format(1))  # Replace with your second number

        # Write the size of the amplitudes or phases list
        file.write("{}\n".format(len(amplitudes)))

        # Write the amplitudes and phases
        for amp, ph in zip(amplitudes, phases):
            file.write("{} {}\n".format(amp, ph))


def discrete_fourier_transform_reader(path, fs, isInverse):
    if isInverse == 0:
        x, y = readFile_returnArray(path)
        return discrete_fourier_transform(y, fs)
    else:
        real_list, imaginary_list = readFile_returnComplexComponents(path)
        return inverse_discrete_fourier_transform(real_list, imaginary_list)


def discrete_fourier_transform(samples, fs):
    N = len(samples)
    amplitudes = []
    phases = []
    real_list = []
    imaginary_list = []
    for k in range(N):
        real_part = 0
        imag_part = 0
        for n in range(N):
            angle = 2 * np.pi * k * n / N
            real_part += samples[n] * np.cos(angle)
            imag_part -= samples[n] * np.sin(angle)

        real_part = round(real_part, 3)
        imag_part = round(imag_part, 3)
        real_list.append(real_part)
        imaginary_list.append(imag_part)
        amplitude = np.sqrt(real_part ** 2 + imag_part ** 2)
        phase_rad = np.arctan2(imag_part, real_part)
        phase_degree = np.degrees(phase_rad)

        amplitudes.append(amplitude)
        phases.append(phase_rad)
    draw_amplitude_phase(amplitudes, phases, fs)
    create_file_polar_form(amplitudes, phases)
    return amplitudes, phases, real_list, imaginary_list


def inverse_discrete_fourier_transform(real, imaginary):
    real2 = []
    imaginary2 = []
    N = len(real)
    for n in range(N):
        sum = 0
        for k in range(N):
            angle = 2 * np.pi * k * n / N
            real_part = np.cos(angle)
            imaginary_part = np.sin(angle)
            real_part = round(real_part, 9)
            imaginary_part = round(imaginary_part, 9)

            sum += real_part * real[k] - imaginary_part * imaginary[k]
        real2.append(round(sum / N, 7))
    return real2


def modify_component(idx, amplitude, phase, amplitudes, phases, path, fs):
    amplitudes, phases = readFile_returnArray(path)
    draw_amplitude_phase(amplitudes, phases, fs)
    amplitudes[idx] = amplitude
    phases[idx] = phase
    draw_amplitude_phase(amplitudes, phases, fs)
    print("AFTER EDIT  AMP: ", amplitudes)
    print("AFTER EDIT  PH: ", phases)
    create_file_polar_form(amplitudes, phases)


def discrete_cosine_transform(path, m):
    x, y = readFile_returnArray(path)
    N = len(y)
    dct_result = np.zeros(N)

    for k in range(N):
        sum_val = 0.0
        for n in range(N):
            angle = (2 * k - 1) * (2 * n - 1) * (np.pi / (4 * N))
            sum_val += y[n] * np.cos(angle)
        dct_result[k] = sum_val * np.sqrt(2 / N)
        dct_result[k] = round(dct_result[k], 5)
    indices = list(range(len(dct_result)))
    draw_signal2(indices, dct_result)
    create_file_dct(dct_result[:m])
    return dct_result


def create_file_dct(chosen_values):
    path = "inOut/task5/coff.txt"
    with open(path, 'w') as file:
        # Write the user-chosen numbers
        file.write("{}\n".format(0))  # Replace with your first number
        file.write("{}\n".format(1))  # Replace with your second number

        # Write the size of the amplitudes or phases list
        file.write("{}\n".format(len(chosen_values)))

        # Write the amplitudes and phases
        for x in zip(chosen_values):
            file.write("{} {}\n".format(0, x[0]))


def remove_dc_component(path):
    x, y = readFile_returnArray(path)
    dc_component = np.mean(x)
    y_new = y - dc_component
    create_file_polar_form(x, y_new)
    return x, y_new


def smooth_signal(path, window_size):
    x, y = readFile_returnArray(path)
    smoothed_signal = []
    for start in range(len(y)):
        end = start + window_size - 1
        if end >= len(y):
            break
        tmp_window = y[start:end + 1]
        # print(type(tmp_window)," ",type(window_size))
        avg = sum(tmp_window) / len(tmp_window)
        smoothed_signal.append(avg)
    return smoothed_signal


def convert_polar_to_complex(amplitudes, phases, dc_remove):
    real_list = []
    imaginary_list = []
    if dc_remove:
        amplitudes[0] = 0
        phases[0] = 0
    for a, p in zip(amplitudes, phases):
        real_num = a * np.cos(p)
        imaginary_num = a * np.sin(p)
        real_list.append(real_num)
        imaginary_list.append(imaginary_num)
    return real_list, imaginary_list


def remove_dc_component_frequency_domain(path, fs):
    x, y = readFile_returnArray(path)
    amplitudes, phases, real_list, imaginary_list = discrete_fourier_transform(y, fs)
    r, i = convert_polar_to_complex(amplitudes, phases, True)
    out = inverse_discrete_fourier_transform(r, i)
    out = np.round(out, 3)
    print("OUT: ", out)
    indices = list(range(len(out)))
    draw_signal2(indices, out)
    return out


def fold_signal(path):
    coordinates = readFile_returnTuples(path)
    for i in range(len(coordinates)):
        coordinates[i] = (-coordinates[i][0], coordinates[i][1])
    coordinates.sort()
    x, y = separate_tuples(coordinates)
    create_file(x, y, "folded.txt")
    draw_signal2(x, y)
    return x, y


def convolve(signal_path, kernel_path):
    convolved_dict = {}
    signal_dict = readFile_returnDict(signal_path)
    kernal_dict = readFile_returnDict(kernel_path)
    signal_len = len(signal_dict)
    kernel_len = len(kernal_dict)
    result_len = signal_len + kernel_len
    signal_min_idx = int(min(signal_dict.keys()))
    signal_max_idx = int(max(signal_dict.keys()))
    kernal_min_idx = int(min(kernal_dict.keys()))
    kernal_max_idx = int(max(kernal_dict.keys()))
    mini_n = int(signal_min_idx + kernal_min_idx)
    maxi_n = int(kernal_max_idx + signal_max_idx)

    for i in range(mini_n, maxi_n + 1):
        sum = 0
        not_first_time = False
        for j in range(signal_min_idx, signal_max_idx + 1):
            if i - j < kernal_min_idx or i - j > kernal_max_idx:
                continue
            sum += signal_dict[j] * kernal_dict[i - j]
        convolved_dict[i] = sum
    indices_list = list(convolved_dict.keys())
    values_list = list(convolved_dict.values())

    return indices_list, values_list


def cross_direct_correlation(signa1_path, signal2_path):
    x1, y1 = readFile_returnArray(signa1_path)
    x2, y2 = readFile_returnArray(signal2_path)
    N = len(y1)
    M = len(y2)
    cross_correlation = []
    squared_signal1_sum = sum(x ** 2 for x in y1)
    squared_signa2_sum = sum(x ** 2 for x in y2)
    NORMALIZATION_CONST = math.sqrt(squared_signal1_sum * squared_signa2_sum) / N
    for tau in range(N):
        res = 0
        for k in range(M):
            res += y1[k] * y2[(k + tau) % M]
        cross_correlation.append(res / N / NORMALIZATION_CONST)

    return cross_correlation


def multiply_lists(list1, list2):
    return [elem1 * elem2 for elem1, elem2 in zip(list1, list2)]


def add_lists(list1, list2):
    return [elem1 + elem2 for elem1, elem2 in zip(list1, list2)]


def fast_convolution(signal1_path, signal2_path):
    x1, y1 = readFile_returnArray(signal1_path)
    x2, y2 = readFile_returnArray(signal2_path)
    mini_n = int(x1[0] + x2[0])
    maxi_n = int(x1[-1] + x2[-1])
    indicies = list(range(mini_n, maxi_n + 1))
    desired_length = len(y1) + len(y2) - 1
    y1_padded = y1 + [0] * (desired_length - len(y1))
    y2_padded = y2 + [0] * (desired_length - len(y2))
    amplitudes1, phases1, real_list1, imaginary_list1 = discrete_fourier_transform(y1_padded, 3)
    amplitudes2, phases2, real_list2, imaginary_list2 = discrete_fourier_transform(y2_padded, 3)
    final_amplitudes = multiply_lists(amplitudes1, amplitudes2)
    final_phases = add_lists(phases1, phases2)
    real, imaginary = convert_polar_to_complex(final_amplitudes, final_phases, 0)
    convolved_signal_output = inverse_discrete_fourier_transform(real, imaginary)
    convolved_signal_output = np.round(convolved_signal_output, 1)
    convolved_signal_output = np.array(convolved_signal_output)
    convolved_signal_output = convolved_signal_output.astype(int)
    convolved_signal_output = convolved_signal_output.tolist()
    ConvTest(indicies, convolved_signal_output)
    return convolved_signal_output


def get_conjugate(imaginary_list):
    return [-elem for elem in imaginary_list]


def get_amplitudes_list(real_list, imaginary_list):
    return [np.sqrt(real_part ** 2 + imaginary_part ** 2) for real_part, imaginary_part in
            zip(real_list, imaginary_list)]


def get_phases_list(real_list, imaginary_list):
    return [np.arctan2(imaginary_part, real_part) for real_part, imaginary_part in zip(real_list, imaginary_list)]


def fast_correlation(signal1_path, signal2_path):
    x1, y1 = readFile_returnArray(signal1_path)
    x2, y2 = readFile_returnArray(signal2_path)
    desired_length = len(y1) + len(y2) - 1
    if (len(y1) != len(y2)):
        y1_padded = y1 + [0] * (desired_length - len(y1))
        y2_padded = y2 + [0] * (desired_length - len(y2))
    else:
        y1_padded = y1
        y2_padded = y2
        desired_length = len(y1)
    amplitudes1, phases1, real_list1, imaginary_list1 = discrete_fourier_transform(y1_padded, 3)
    amplitudes2, phases2, real_list2, imaginary_list2 = discrete_fourier_transform(y2_padded, 3)
    imaginary_list1 = get_conjugate(imaginary_list1)
    amplitudes1 = get_amplitudes_list(real_list1, imaginary_list1)
    phases1 = get_phases_list(real_list1, imaginary_list1)
    final_amplitudes = multiply_lists(amplitudes1, amplitudes2)
    final_phases = add_lists(phases1, phases2)
    real, imaginary = convert_polar_to_complex(final_amplitudes, final_phases, 0)
    correlation_out = inverse_discrete_fourier_transform(real, imaginary)
    correlation_out = np.round(correlation_out, 2)
    correlation_out = np.array(correlation_out) / desired_length
    correlation_out = correlation_out.tolist()
    Compare_Signals("inOut/Fast Correlation/Corr_Output.txt", [], correlation_out)
    return correlation_out


out = fast_correlation("inOut/Fast Correlation/Corr_input signal1.txt", "inOut/Fast Correlation/Corr_input signal2.txt")
print(out)
Compare_Signals("inOut/Fast Correlation/Corr_Output.txt",[],out)

fast_convolution("inOut/Convolution/Input_conv_Sig1.txt", "inOut/Convolution/Input_conv_Sig2.txt")