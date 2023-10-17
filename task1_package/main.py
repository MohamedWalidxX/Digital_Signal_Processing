import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

from tkinter import *


def draw_signal(path, plot_choice):
    # Initialize empty lists to store x and y values
    x_values = []
    y_values = []

    # Read the data from the file, skipping the first three lines
    with open(path, "r") as file:
        lines = file.readlines()[3:]  # Skip the first three lines
        for line in lines:
            x, y = map(float, line.strip().split())
            x_values.append(x)
            y_values.append(y)

    # Choose between discrete and continuous plots
    if plot_choice == 'd':
        # Discrete signal plot with vertical bars
        plt.figure(figsize=(8, 6))
        plt.plot(x_values, y_values, 'o', label='Sample Data')

        for x, y in zip(x_values, y_values):
            plt.vlines(x, 0, y, colors='r', linestyles='dashed')

        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)
        plt.title('Discrete Signal Plot with Vertical Bars')
        plt.show()

    elif plot_choice == 'c':
        # Choose the interpolation method (e.g., linear)
        interpolation_method = 'linear'

        # Create an interpolation function
        interp_func = interp1d(x_values, y_values, kind=interpolation_method, fill_value="extrapolate")

        # Generate new x-values for reconstruction
        new_x = np.linspace(min(x_values), max(x_values), num=100)

        # Use the interpolation function to obtain the corresponding y-values
        new_y = interp_func(new_x)

        # Continuous signal plot
        plt.figure(figsize=(8, 6))
        plt.plot(x_values, y_values, 'o', label='Sample Data')
        plt.plot(new_x, new_y, '-', label='Reconstructed Signal')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.grid(True)
        plt.title('Continuous Signal Plot')
        plt.show()
    elif plot_choice == 'm':
        # Merge both discrete and continuous plots
        plt.figure(figsize=(8, 6))
        plt.plot(x_values, y_values, 'o', label='Sample Data (Discrete)')

        for x, y in zip(x_values, y_values):
            plt.vlines(x, 0, y, colors='r', linestyles='dashed')

        # Choose the interpolation method (e.g., linear)
        interpolation_method = 'linear'

        # Create an interpolation function
        interp_func = interp1d(x_values, y_values, kind=interpolation_method, fill_value="extrapolate")

        # Generate new x-values for reconstruction
        new_x = np.linspace(min(x_values), max(x_values), num=100)

        # Use the interpolation function to obtain the corresponding y-values
        new_y = interp_func(new_x)

        # Plot the continuous signal
        plt.plot(new_x, new_y, '-', label='Reconstructed Signal (Continuous)')

        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.grid(True)
        plt.title('Merged Discrete and Continuous Signal Plot')
        plt.show()

    else:
        print("Invalid choice. Enter 'd' for discrete plot or 'c' for continuous plot.")
        draw_signal("signal1.txt", 'd')


#########################


root=Tk()
e=Entry(root,width=80,borderwidth=30) #Allowing for input place
e.pack()
root.title("DSP Task 1")  # changing the title of the form

def onClick(): ## what will happen after clicking the button function
    path,char=e.get().split(' ') # get the text from the input area
    draw_signal(path,char)  ###(((((Calling the function)))))

myButton=Button(root,text=" Click on me Path ",command=onClick) 
myButton.pack()

root.mainloop()


