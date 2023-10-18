import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import sino_waves as si
import cosine_wave as cs
from tkinter import messagebox

from tkinter import *




        # Continuous signal plot


#########################


root=Tk()
e=Entry(root,width=80,borderwidth=30) #Allowing for input place
e.pack()
root.title("DSP Task 1")  # changing the title of the form
choice=1



def onClick(): ## what will happen after clicking the button function
    arr=e.get().split(' ') # get the text from the input area
    if len(arr)!=5:
        messagebox.showerror("Input Error", "Not the right number of arguments")
    if arr[3]<arr[2]*2:
        messagebox.showerror("Nyquist Theory Error", "fs must be bigger than 2*f")
    
    elif choice==1:
         t, signal = si.generate_sinusoidal_signal(int(arr[0]),  float(arr[1]), int(arr[2]), int(arr[3]), float(arr[4]))
         plt.figure(figsize=(8, 6))
         plt.plot(t, signal)
         plt.xlabel('Time (s)')
         plt.ylabel('Amplitude')
         plt.title('Sinusoidal Signal')
         plt.grid(True)
         plt.show()
    #comparesignals.SignalSamplesAreEqual(file_name="CosOutput.txt", indices=0, samples=signal)
    else:
         t, signal = cs.generate_sinusoidal_signal(int(arr[0]),  float(arr[1]), int(arr[2]), int(arr[3]), float(arr[4]))
         plt.figure(figsize=(8, 6))
         plt.plot(t, signal)
         plt.xlabel('Time (s)')
         plt.ylabel('Amplitude')
         plt.title('cosine Signal')
         plt.grid(True)
         plt.show()


def sinClick():
    choice=1
def cosClick():
    choice=2


myButton=Button(root,text=" Click on me To show Signal ",command=onClick) 
sinButton=Button(root,text=" Sin ",command=sinClick) 
cosButton=Button(root,text=" Cos ",command=cosClick) 

sinButton.pack()
cosButton.pack()
myButton.pack()

root.mainloop()


