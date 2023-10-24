import numpy as np

from draw import draw_signal
from cosine_wave import generate_cosine_signal
from sino_waves import generate_sinusoidal_signal
from comparesignals import SignalSamplesAreEqual
from ArithmeticOperations import *


directory = "inOut/task2/"
signalFile = "Signal1.txt"
signalFile2 = "Signal2.txt"
shift_signal(directory+signalFile, 500)