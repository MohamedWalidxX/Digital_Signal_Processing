import numpy as np

from draw import draw_signal
from cosine_wave import generate_cosine_signal
from sino_waves import generate_sinusoidal_signal
from comparesignals import SignalSamplesAreEqual
from ArithmeticOperations import *


directory = "inOut/task3/"
signalFile = "Signal1.txt"
signalFile2 = "Signal2.txt"
file = "Quan1_input.txt"
quantize_signal(directory+file, 3, 0)