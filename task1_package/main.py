import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import sino_waves as si
import cosine_wave as cs
from tkinter import messagebox

from tkinter import *
import ArithmeticOperations as Ar
import DerivativeSignal as Dr
import cosine_wave as cs
import sino_waves as si
from comparesignals import SignalSamplesAreEqual
from tkinter import Toplevel, filedialog
from comparesignals import SignalSamplesAreEqual, SignalSamplesAreEqual2
from inOut.task7.ConvTest import ConvTest

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
        FrequencyDomain = Button(self.root, text="Frequency Domain", command=self.goTofrequencyDomain)
        Dct=Button(self.root,text=" DCT & DC ",command=self.goToDctDomain)
        TimeDomain=Button(self.root,text="TimeDomain",command=self.goToTimeDomain)
        Convlove=Button(self.root,text="Convolve",command=self.goToConvolove)
        sinButton.pack()
        cosButton.pack()
        myButton.pack()
        emptyPageButton.pack()
        quantizePage.pack()
        FrequencyDomain.pack()
        Dct.pack()
        TimeDomain.pack()
        Convlove.pack()


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
        x, y = Ar.shift_signal(path,int(shiftAmount))
        if (int(shiftAmount) < 0):
            SignalSamplesAreEqual("inOut/task6/Shifting and Folding/Output_ShifFoldedby500.txt",[],y)
        else :
            SignalSamplesAreEqual("inOut/task6/Shifting and Folding/Output_ShiftFoldedby-500.txt",[],y)




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

    def goTofrequencyDomain(self):
        new_window = Toplevel(self.root)
        new_window.title("Frequency Domain")

        # File path widgets
        path_label = Label(new_window, text="Enter File Path:")
        path_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        path_entry = Entry(new_window, width=50)
        path_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        browse_button = Button(new_window, text="Browse", command=lambda: self.browse_file(path_entry))
        browse_button.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        # Sampling frequency widgets
        fs_label = Label(new_window, text="Enter Sampling Frequency:")
        fs_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        fs_entry = Entry(new_window, width=10)
        fs_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # DFT button
        button1 = Button(new_window, text="DFT", command=lambda: self.onClickDFT(path_entry.get(), fs_entry.get()))
        button1.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Inverse DFT button
        button2 = Button(new_window, text="Inverse DFT",
                         command=lambda: self.onClickIDFT(path_entry.get(), fs_entry.get()))
        button2.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Index widgets
        index_label = Label(new_window, text="Enter Index:")
        index_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        index_entry = Entry(new_window, width=10)
        index_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Amplitude widgets
        amplitude_label = Label(new_window, text="Enter Amplitude:")
        amplitude_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        amplitude_entry = Entry(new_window, width=10)
        amplitude_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Phase widgets
        phase_label = Label(new_window, text="Enter Phase:")
        phase_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        phase_entry = Entry(new_window, width=10)
        phase_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        path_label9 = Label(new_window, text="Enter File Path:")
        path_label9.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        path_entry9 = Entry(new_window, width=50)
        path_entry9.grid(row=7, column=1, padx=10, pady=10, columnspan=2)

        browse_button9 = Button(new_window, text="Browse", command=lambda: self.browse_file(path_entry9))
        browse_button9.grid(row=8, column=3, padx=10, pady=10, sticky="w")

        # Modify button
        action_button = Button(new_window, text="Modify",
                               command=lambda: self.onClickModify(index_entry.get(), amplitude_entry.get(),
                                                                  phase_entry.get(),path_entry9.get() ,fs_entry.get()))
        action_button.grid(row=10, column=0, padx=10, pady=10, sticky="w")

    to_be_modified_amplitudes = []
    to_be_modified_phases = []
    def browse_file(self, path_entry):
        file_path = filedialog.askopenfilename()
        path_entry.delete(0, END)
        path_entry.insert(0, file_path)
    def onClickDFT(self,path,fs):
        amplitudes, phases, real_list, imaginary_list = Ar.discrete_fourier_transform_reader(path, int(fs),0)


    def onClickIDFT(self,path,fs):
        l1 = Ar.discrete_fourier_transform_reader(path, int(fs),1)

    def onClickModify(self,idx,amplitude,phase,path,fs):
        listAmpltiude=[] # hard coded list
        listPhase=[] # hard coded list

        Ar.modify_component(int(idx),int(amplitude),int(phase),listAmpltiude,listPhase,path,int(fs))
    def goToDctDomain(self):
        new_window = Toplevel(self.root)
        new_window.title("DCT")
        path_label = Label(new_window, text="Enter File Path:")
        path_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        path_entry = Entry(new_window, width=50)
        path_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        browse_button = Button(new_window, text="Browse", command=lambda: self.browse_file(path_entry))
        browse_button.grid(row=0, column=3, padx=10, pady=10, sticky="w")
        ########
        m_label = Label(new_window, text="Enter m coefficients")
        m_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        m_entry = Entry(new_window, width=10)
        m_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        button1 = Button(new_window, text="DCT", command=lambda: self.onClickDCT(path_entry.get(), m_entry.get()))
        button1.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        path_label2 = Label(new_window, text="Enter File Path:")
        path_label2.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        path_entry2 = Entry(new_window, width=50)
        path_entry2.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

        browse_button2 = Button(new_window, text="Browse", command=lambda: self.browse_file(path_entry2))
        browse_button2.grid(row=4, column=3, padx=10, pady=10, sticky="w")
        button2 = Button(new_window, text="Remove DCT", command=lambda: self.onClickRemoveDCT(path_entry2.get()))
        button2.grid(row=6, column=0, padx=10, pady=10, sticky="w")
    def onClickDCT(self,path,m):
        res=Ar.discrete_cosine_transform(path,int(m))

    def onClickRemoveDCT(self,path):
        x,y=Ar.remove_dc_component(path)

    def goToTimeDomain(self):
        new_window = Toplevel(self.root)
        new_window.title("Time Domain")
        path_label = Label(new_window, text="Enter File Path:")
        path_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        path_entry = Entry(new_window, width=50)
        path_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        browse_button = Button(new_window, text="Browse", command=lambda: self.browse_file(path_entry))
        browse_button.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        ## Smothing UI && Button
        window_size_label = Label(new_window, text="Window Size")
        window_size_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        window_size_entry = Entry(new_window, width=10)
        window_size_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        button_smothing = Button(new_window, text="Smothing", command=lambda: self.onClickSmoth(path_entry.get(),window_size_entry.get()))
        button_smothing.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        ## Sharpning UI && Button
        button_sharpning = Button(new_window, text="Sharpning",command=lambda: self.onClickSharp())
        button_sharpning.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        #Delay
        shift_label = Label(new_window, text="Delay")
        shift_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        shift_label_entry = Entry(new_window, width=10)
        shift_label_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")
        button_Delay = Button(new_window, text="Delay",
                                 command=lambda: self.onClickShiftSignal(path_entry.get(), shift_label_entry.get()))
        button_Delay.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        ## Folding
        button_Folding = Button(new_window, text="Folding",
                              command=lambda: self.onClickFolding(path_entry.get()))
        button_Folding.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        # DC component Frquency domain
        fs_label = Label(new_window, text="Fs")
        fs_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")
        fs_label_entry = Entry(new_window, width=10)
        fs_label_entry.grid(row=8, column=1, padx=10, pady=10, sticky="w")
        button_fs = Button(new_window, text=" Remove DC frequency domain",
                              command=lambda: self.onClickDc_component(path_entry.get(), fs_label_entry.get()))
        button_fs.grid(row=9, column=0, padx=10, pady=10, sticky="w")


    def onClickFolding(self,path):
        X,Y=Ar.fold_signal(path)
        print("Fold -> ",X)
        print("Fold -> ",Y)
        SignalSamplesAreEqual2("inOut/task6/Shifting and Folding/Output_fold.txt",[],X)

    def onClickSmoth(self,path,window_size):
        smothed_signal=Ar.smooth_signal(path,int(window_size))
        print("Smothed Singal -->",smothed_signal)
        print("LEN: ", len(smothed_signal))
        if int(window_size) == 3:
            SignalSamplesAreEqual("inOut/task6/Moving Average/OutMovAvgTest1.txt",[],smothed_signal)
        else:
            SignalSamplesAreEqual("inOut/task6/Moving Average/OutMovAvgTest2.txt",[], smothed_signal)


    def onClickSharp(self):
        Dr.DerivativeSignal()
    def onClickDc_component(self,path,fs):
        out =Ar.remove_dc_component_frequency_domain(path,int(fs))
        SignalSamplesAreEqual("inOut/task5/DC_component_output.txt",[],out)

    def onClickConvolve(self, path1,path2):
        indices_list, values_list = Ar.convolve(path1, path2)
        ConvTest(indices_list, values_list)

    def goToConvolove(self):
        new_window = Toplevel(self.root)
        new_window.title("Convolve")
        path_label = Label(new_window, text="Enter File Path:")
        path_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        path_entry = Entry(new_window, width=50)
        path_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        browse_button = Button(new_window, text="Browse", command=lambda: self.browse_file(path_entry))
        browse_button.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        path_labe2 = Label(new_window, text="Enter File Path:")
        path_labe2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        path_entry2 = Entry(new_window, width=50)
        path_entry2.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        browse_button2 = Button(new_window, text="Browse", command=lambda: self.browse_file(path_entry2))
        browse_button2.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        ConvolveButton = Button(new_window, text="Convolve", command=lambda:self.onClickConvolve(path_entry.get(),path_entry2.get()))
        ConvolveButton.grid(row=3, column=2, padx=10, pady=10, sticky="w")


    
        








    def run(self):
        self.root.mainloop()


gui = GUI()
gui.run()