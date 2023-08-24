from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from scipy.fftpack import fft
from scipy import signal

##################################################

def binary(sym, sym_len):

  import numpy as np
  rand_n = np.random.rand(sym)
  rand_n[np.where(rand_n >= 0.5)] = 1
  rand_n[np.where(rand_n <= 0.5)] = 0

  sig = np.zeros(int(sym*sym_len))

  # generating symbols
  id1 = np.where(rand_n == 1)

  for i in id1[0]:
    temp = int(i*sym_len)
    sig[temp:temp+sym_len] = 1
  return sig

##################################################
#window_width = 800
#window_height = 600
root = Tk()
root.title('Advance Modulation Techniques')
#label1=Label(root, text="Advance Modulation Techniques",font=("Arial",25)).pack()
fig1 = Figure(figsize=(2, 2), dpi=80)
#___________________________________________________________#
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Advance Modulation Techniques')
tabControl.pack(expand = 1, fill ="both")
Label(tab1, text="Advance Modulation Techniques",font=("Arial",22)).pack()


canvas = FigureCanvasTkAgg(fig1, master=tab1) 
canvas.draw_idle()
canvas.get_tk_widget().place(x=230, y=50, width=1250, height=750)

##____________________Tool bar___________________##

toolbar = NavigationToolbar2Tk(canvas, root)

##################################################
##____________________ Frames ___________________##

frame1=Frame(tab1, width=200, height=105, relief=GROOVE, borderwidth=2)
frame1.place(x=10,y=90)
Label(frame1, text="Digital Signal Generator",font=("Arial",12)).place(x=10,y=10)

##################################################

frame2=Frame(tab1, width=200, height=160, relief=GROOVE, borderwidth=2)
frame2.place(x=10,y=192)
Label(frame2, text="Carrier Generator",font=("Arial",12)).place(x=40,y=10) #
Label(frame2, text="Amplitude").place(x=2,y=50)
Label(frame2, text="Frequency").place(x=2,y=80)

Ac=Entry(frame2, width=10,font=("Arial",12))
Ac.place(x=70, y=50)

fc=Entry(frame2, width=10,font=("Arial",12))
fc.place(x=70, y=80)

##################################################

frame3=Frame(tab1, width=200, height=105, relief=GROOVE, borderwidth=2)
frame3.place(x=10,y=350)
Label(frame3, text="ASK Generator",font=("Arial",12)).place(x=40,y=10)

##################################################

frame4=Frame(tab1, width=200, height=105, relief=GROOVE, borderwidth=2)
frame4.place(x=10,y=450)
Label(frame4, text="FSK Generator",font=("Arial",12)).place(x=40,y=10)

##################################################

frame5=Frame(tab1, width=200, height=105, relief=GROOVE, borderwidth=2)
frame5.place(x=10,y=550)
Label(frame5, text="PSK Generator",font=("Arial",12)).place(x=40,y=10)

##################################################

frame6=Frame(tab1, width=200, height=105, relief=GROOVE, borderwidth=2)
frame6.place(x=10,y=650)
Label(frame6, text="Reset Button",font=("Arial",12)).place(x=40,y=10)

##################################################
##____________________ Time Diclearation ___________________##

t1=np.linspace(0,1,1000)  

##################################################

def plot_Dig_sig():
    
    global sig
    Fs = 1000
    T = 1  ## Total Simulation time in sec
    Td = 0.1  ## Bit duration   
    Nsamples = int(Td*Fs)  ## No.of Samples in one Bit duration
    Nsym = int(np.floor(np.size(t1)/Nsamples))
    sig = binary(Nsym,Nsamples)
    plot1 = fig1.add_subplot(511)
    plot1.plot(sig,color= 'indigo',label='Digital Signal')
    plot1.set_xlabel('Time(Sec)')
    plot1.set_ylabel('Amplitude (V)')
    plot1.grid('True')
    plot1.legend()
    canvas.draw_idle()

###################################################

def plot_Carr_sig():
    global A_c
    A_c=float(Ac.get())
    global F_c
    F_c=float(fc.get())
    global carr_sig
    carr_sig=A_c*np.sin(2*np.pi*F_c*t1)
    plot2 = fig1.add_subplot(512)
    plot2.plot(carr_sig,color= 'maroon',label='Message Signal')
    plot2.set_xlabel('Time(Sec)')
    plot2.set_ylabel('Amplitude (V)')
    plot2.grid('True')
    plot2.legend()
    canvas.draw_idle()

##################################################
def plot_ASK_sig():
    
    Ask= sig*carr_sig    
    plot3 = fig1.add_subplot(513)
    plot3.plot(t1,Ask,color= 'olive',label='ASK signal')
    plot3.set_xlabel('Time (Sec)')
    plot3.set_ylabel('Amplitude (V)')
    plot3.grid('True')
    plot3.legend()
    canvas.draw_idle()

########################################################   
def plot_FSK_mod():    

    global f  
    f = F_c + F_c*sig/2
    phase = np.pi + np.pi*sig/2    
    Fsk_sig = np.sin(2*np.pi*f*t1)
    plot4 = fig1.add_subplot(514)
    plot4.plot(t1,Fsk_sig, color="purple",label='FSK Signal')
    plot4.set_xlabel('Time (Sec)')
    plot4.set_ylabel('Amplitude (V)')
    plot4.grid('True')
    plot4.legend()
    canvas.draw_idle()  

########################################################

def plot_PSK_mod():
    global phase
    phase = np.pi + np.pi*sig/2
    Psk_sig = np.sin(2*np.pi*F_c*t1 + phase)
    plot5 = fig1.add_subplot(515)
    plot5.plot(t1,Psk_sig,color="chocolate",label='PSK Signal')
    plot5.set_xlabel('Time (Sec)')
    plot5.set_ylabel('Amplitude (V)')
    plot5.grid('True')
    plot5.legend()
    canvas.draw_idle()  

########################################################

def Clear_btn1():
   fig1.clear()
   plt.close('all')
   canvas.draw_idle()

##################################################

plot_Dig_sig = Button(master = frame1, command = plot_Dig_sig,height = 2, width = 10,text = "Plot")
plot_Dig_sig.place(x= 55, y= 55)

##################################################

plot_Carr_sig = Button(master = frame2, command = plot_Carr_sig,height = 2, width = 10,text = "Plot")
plot_Carr_sig.place(x= 55, y= 110)

##################################################

plot_ASK_sig = Button(master = frame3, command = plot_ASK_sig,height = 2, width = 10,text = "Plot")
plot_ASK_sig.place(x= 55, y= 55)

##################################################

plot_FSK_mod = Button(master = frame4, command =plot_FSK_mod ,height = 2, width = 10,text = "Plot")
plot_FSK_mod.place(x= 55, y= 55)

##################################################

plot_PSK_mod = Button(master = frame5, command =plot_PSK_mod ,height = 2, width = 10,text = "Plot")
plot_PSK_mod.place(x= 55, y= 55)

##################################################

Clear_btn1 = Button(master = frame6, command = Clear_btn1,height = 2, width = 10,text = "Clear")
Clear_btn1.place(x= 55, y= 55)

#################_________________________________________Tab1 Ends____________________________________#####################
root.mainloop()