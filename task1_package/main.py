import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import sino_waves as si
import cosine_wave as cs
from tkinter import messagebox

from tkinter import *
import ArithmeticOperations as Ar
import cosine_wave as cs
import sino_waves as si




        # Continuous signal plot


#########################



class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("DSP Task 1")

        self.e = Entry(self.root, width=80, borderwidth=30)
        self.e.pack()

        self.choice = 1

        myButton = Button(self.root, text="Click on me to show Signal", command=self.onClick)
        sinButton = Button(self.root, text="Sin", command=self.sinClick)
        cosButton = Button(self.root, text="Cos", command=self.cosClick)
        emptyPageButton = Button(self.root, text="Arithmatic", command=self.goToEmptyPage)
        quantizePage=Button(self.root, text="Quantize", command=self.goToQuantize)

        sinButton.pack()
        cosButton.pack()
        myButton.pack()
        emptyPageButton.pack()
        quantizePage.pack()

    def onClick(self):
        arr = self.e.get().split(' ')
        if len(arr) != 5:
            messagebox.showerror("Input Error", "Not the right number of arguments")
        elif int(arr[3]) < int(arr[2]) * 2:
            messagebox.showerror("Nyquist Theory Error", "fs must be bigger than 2*f")
        else:
            if self.choice == 1:
                t, signal = si.generate_sinusoidal_signal(int(arr[0]), float(arr[1]), int(arr[2]), int(arr[3]),
                                                          float(arr[4]))
                plt.figure(figsize=(8, 6))
                plt.plot(t, signal)
                plt.xlabel('Time (s)')
                plt.ylabel('Amplitude')
                plt.title('Sinusoidal Signal')
                plt.grid(True)
                plt.show()
            else:
                t, signal = cs.generate_cosine_signal(int(arr[0]), float(arr[1]), int(arr[2]), int(arr[3]),
                                                          float(arr[4]))
                plt.figure(figsize=(8, 6))
                plt.plot(t, signal)
                plt.xlabel('Time (s)')
                plt.ylabel('Amplitude')
                plt.title('Cosine Signal')
                plt.grid(True)
                plt.show()

    def sinClick(self):
        self.choice = 1

    def cosClick(self):
        self.choice = 2

    def goToEmptyPage(self):
        # Code for opening an empty page or performing any desired action
        new_window = Toplevel(self.root)
        new_window.title("Arithmatic Page")

        label1 = Label(new_window, text="Argument 1:")
        label1.grid(row=0, column=0, padx=10, pady=10)

        entry1 = Entry(new_window)
        entry1.grid(row=0, column=1, padx=10, pady=10)

        label2 = Label(new_window, text="Argument 2:")
        label2.grid(row=1, column=0, padx=10, pady=10)

        entry2 = Entry(new_window)
        entry2.grid(row=1, column=1, padx=10, pady=10)

        label3 = Label(new_window, text="Additional Entry:")
        label3.grid(row=2, column=0, padx=10, pady=10)

        entry3 = Entry(new_window)
        entry3.grid(row=2, column=1, padx=10, pady=10)

        button1 = Button(new_window, text="Add Signals",command=lambda :self.onClickAddSignals(entry1.get(),entry2.get()) )
        button1.grid(row=3, column=0, padx=10, pady=10)

        button2 = Button(new_window, text="Subtract Signals",
                         command=lambda: self.onClickSubtractSignals(entry1.get(), entry2.get()))
        button2.grid(row=3, column=1, padx=10, pady=10)

        button3 = Button(new_window, text="Multiply Signal",
                         command=lambda :self.onClickMultiplySignal(entry1.get(), entry2.get()))
        button3.grid(row=4, column=0, padx=10, pady=10)

        button4 = Button(new_window, text="Square Signal",command=lambda :self.onClickSquareSignal(entry1.get()))
        button4.grid(row=4, column=1, padx=10, pady=10)

        button5 = Button(new_window, text="Shift Signal", command=lambda :self.onClickShiftSignal(entry1.get(), entry2.get()))
        button5.grid(row=5, column=0, padx=10, pady=10)

        button6 = Button(new_window, text="Normalize",command=lambda :self.onClickNormalize(entry1.get(), entry2.get(), entry3.get()))
        button6.grid(row=5, column=1, padx=10, pady=10)

        button7 = Button(new_window, text="Accumulate", command=lambda :self.onCickAccumlate(entry1.get()))
        button7.grid(row=6, column=0, padx=10, pady=10)
    def onClickAddSignals(self,path1 ,path2):
        Ar.addSignals(path1,path2)
    def onClickSubtractSignals(self,path1,path2):
        Ar.subtractSignals(path1,path2)

    def onClickMultiplySignal(self,path,constNum):
        Ar.multiplySignal(path,int(constNum))

    def onClickSquareSignal(self,path):
        Ar.square_signal(str(path))

    def onClickShiftSignal(self,path,shiftAmount):
        Ar.shift_signal(path,int(shiftAmount))

    def onClickNormalize(self,path,a , b):
        Ar.normalize(path,int(a),int(b))
    def onCickAccumlate(self,path):
        Ar.accumulate(path)


    def goToQuantize(self):
        new_window = Toplevel(self.root)
        new_window.title("Quantize Page")
        label1 = Label(new_window, text="File Path :")
        label1.grid(row=0, column=0, padx=10, pady=10)

        entry1 = Entry(new_window)
        entry1.grid(row=0, column=1, padx=10, pady=10)

        label2 = Label(new_window, text="Levels:")
        label2.grid(row=1, column=0, padx=10, pady=10)

        entry2 = Entry(new_window)
        entry2.grid(row=1, column=1, padx=10, pady=10)

        label3 = Label(new_window, text="Is Converted  1 | 0:")
        label3.grid(row=2, column=0, padx=10, pady=10)

        entry3 = Entry(new_window)
        entry3.grid(row=2, column=1, padx=10, pady=10)

        result_label1 = Label(new_window, text="Error:")
        result_label1.grid(row=4, column=0, padx=10, pady=10)

        result_label2 = Label(new_window, text="Encoded Samples:")
        result_label2.grid(row=5, column=0, padx=10, pady=10)

      #  button1 = Button(new_window, text="<< Quantize >>",command=lambda: self.onClickQuantize(entry1.get(), entry2.get(),entry3.get()))
        button1 = Button(new_window, text="<< Quantize >>",command=lambda: self.onClickQuantize(entry1.get(), entry2.get(), entry3.get(),result_label1,result_label2))
        button1.grid(row=3, column=1, padx=10, pady=10)


    def onClickQuantize(self,path,levels,is_converted,result_label1,result_label2):
        error,encoded_group_of_samples=Ar.quantize_signal(path,int(levels),int(is_converted))
        result_label1.config(text="Error: " + str(error))
        result_label2.config(text="Encoded Samples: " + str(encoded_group_of_samples))



    def run(self):
        self.root.mainloop()

    def run(self):
        self.root.mainloop()


gui = GUI()
gui.run()