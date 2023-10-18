def draw_signal(path, plot_choice):
    # Initialize empty lists to store x and y values
    print("here ---------------------------------------------------------------------------->")
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
