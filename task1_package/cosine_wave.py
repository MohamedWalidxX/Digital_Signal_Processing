import numpy as np
import matplotlib.pyplot as plt


def generate_cosine_signal(A, theta, f, fs, duration):
    """
    Generate a sinusoidal signal.

    Parameters:
        A (float): Amplitude of the sinusoidal signal.
        theta (float): Phase shift of the signal in radians.
        f (float): Analog frequency of the sinusoid.
        fs (float): Sampling frequency (must be at least 2*f to satisfy Nyquist).
        duration (float): Duration of the signal in seconds.

    Returns:
        tuple: A tuple containing the time values and the corresponding signal values.
    """
    # Calculate the number of samples needed
    num_samples = int(fs * duration)

    # Generate time values
    t = np.linspace(0, duration, num_samples, endpoint=False)
    print(t)

    # Generate the sinusoidal signal
    signal = A * np.cos(2 * np.pi * f * t + theta)

    return t, signal


# Example usage:
A = 3  # Amplitude
theta = 2.35619449019235  # Phase shift (in radians)
f = 200  # Analog frequency (5 Hz)
fs = 500  # Sampling frequency (must satisfy Nyquist: fs >= 2*f)
duration = 1.0  # Duration of the signal (in seconds)
