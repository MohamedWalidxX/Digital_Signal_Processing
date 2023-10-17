import numpy as np
import matplotlib.pyplot as plt
import comparesignals

def generate_sinusoidal_signal(A, theta, f, fs, duration):
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

    # Generate the sinusoidal signal
    signal = A * np.sin(2 * np.pi * f * t + theta)

    return t, signal


# Example usage:
A = 3  # Amplitude
theta = 1.96349540849362  # Phase shift (in radians)
f = 360  # Analog frequency (5 Hz)
fs = 720  # Sampling frequency (must satisfy Nyquist: fs >= 2*f)
duration = 1.0  # Duration of the signal (in seconds)

t, signal = generate_sinusoidal_signal(A, theta, f, fs, duration)

# Plot the signal
plt.figure(figsize=(8, 6))
plt.plot(t, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sinusoidal Signal')
plt.grid(True)
plt.show()
comparesignals.SignalSamplesAreEqual(file_name="SinOutput.txt", indices=0, samples=signal)