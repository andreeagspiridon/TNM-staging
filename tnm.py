#Use the Ttk(Tk themed widgets) by importing this module:
from tkinter import ttk
from tkinter import *
#represents all the functions and built-in modules in the tkinter library
import tkinter
top = tkinter.Tk()#an instance of tkinter frame or window
top.resizable(False, False)#make the Tkinter window not resizable by setting the property to False
top.title("CANCER STAGING")
top.geometry('270x280')

# Code to add widgets will go here...
#Popup
def popup():
    info = Toplevel()#Toplevel widget is used to create a window on top of all other windows
    info.geometry('300x90')
    info.resizable(False, False)
    info.title('INFO')
    ttk.Label(info, text="  The application uses the 9th American \nJoint Committee on Cancer TNM system",).grid(row=0,column=0,padx=25)
    ttk.Button(info, text='Quit', command=info.destroy).grid(row=2,column=0,pady=7)# destroy method has the ability to “destroy” any Tkinter GUI objects
    info.grab_set() #The widget grabs all events for the application

#Dropdown menu 
tumor_list = ['Select tumor location','stomach','pancreas','liver']

menu= StringVar()# Holds a string; the default value is an empty string
menu.set(tumor_list[0]) #default value of dropdown menu

#Create a dropdown Menu
E1= ttk.OptionMenu(top, menu, *tumor_list)
E1.grid(row=1, column=1)
#The OptionMenu widget provides you with a predefined set of options in a drop-down menu.
#OptionMenu(container, variable, default=None, *values, **kwargs)

L1 = ttk.Label(top, text="Staging",).grid(row=0,column=1, padx = 5)
L3 = ttk.Label(top, text="T",).grid(row=2,column=0, padx = 5)
L4 = ttk.Label(top, text="N",).grid(row=3,column=0, padx = 5)
L5 = ttk.Label(top, text="M",).grid(row=4,column=0, padx = 5)
L5 = ttk.Label(top, text="Stage",).grid(row=5,column=0, padx = 5)

E2 = ttk.Entry(top)
E2.grid(row=2,column=1, pady = 5, padx = 10)
E3 = ttk.Entry(top)
E3.grid(row=3,column=1, pady = 5, padx = 10)
E4 = ttk.Entry(top)
E4.grid(row=4,column=1, pady = 5, padx = 10)
E5 = ttk.Entry(top)
E5.grid(row=5,column=1, pady = 5, padx = 10)
B= ttk.Button(top, text ="Submit",).grid(row=6,column=1, pady = 5, padx = 5)


def proces():
    T=Entry.get(E2)
    N=Entry.get(E3)
    M=Entry.get(E4)
    if menu.get()=='stomach' and T=='is' and N=='0' and M=='0':
        answer='0'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='1' and N=='0' and M=='0':
        answer='IA'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='1' and N=='1' and M=='0':
        answer='IB'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='2' and N=='0' and M=='0':
        answer='IB'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='1' and N=='2' and M=='0':
        answer='IIA'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='2' and N=='1' and M=='0':
        answer='IIA'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='3' and N=='0' and M=='0':
        answer='IIA'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='2' and N=='2' and M=='0':
        answer='IIB'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='1' and N=='3a' and M=='0':
        answer='IIB'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='3' and N=='1' and M=='0':
        answer='IIB'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='4a' and N=='0' and M=='0':
        answer='IIB'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='2' and N=='3a' and M=='0':
        answer='IIIA'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='3' and N=='2' and M=='0':
        answer='IIIA'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='4a' and N=='1' and M=='0':
        answer='IIIA'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='4a' and N=='2' and M=='0':
        answer='IIIA'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='4b' and N=='0' and M=='0':
        answer='IIIA'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='1' and N=='3b' and M=='0':
        answer='IIIB'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='3' and N=='3a' and M=='0':
        answer='IIIB'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='2' and N=='3b' and M=='0':
        answer='IIIB'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='4a' and N=='3a' and M=='0':
        answer='IIIB'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='4b' and N=='1' and M=='0':
        answer='IIIB'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='4b' and N=='2' and M=='0':
        answer='IIIB'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='3' and N=='3b' and M=='0':
        answer='IIIC'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='4a' and N=='3b' and M=='0':
        answer='IIIC'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='4b' and N=='3a' and M=='0':
        answer='IIIC'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  T=='4b' and N=='3b' and M=='0':
        answer='IIIC'
        Entry.insert(E5,0,answer)
    if menu.get()=='stomach' and  M=='1':
        answer='IV'
        Entry.insert(E5,0,answer)
    if menu.get()=='pancreas' and T=='is' and N=='0' and M=='0':
        answer='0'
        Entry.insert(E5,0,answer)
    if menu.get()=='pancreas' and T=='1' and N=='0' and M=='0':
        answer='IA'
        Entry.insert(E5,0,answer)
    if menu.get()=='pancreas' and T=='2' and N=='0' and M=='0':
        answer='IB'
        Entry.insert(E5,0,answer)
    if menu.get()=='pancreas' and T=='3' and N=='0' and M=='0':
        answer='IIA'
        Entry.insert(E5,0,answer)
    if menu.get()=='pancreas' and T=='1' and N=='1' and M=='0':
        answer='IIB'
        Entry.insert(E5,0,answer)
    if menu.get()=='pancreas' and T=='2' and N=='1' and M=='0':
        answer='IIB'
        Entry.insert(E5,0,answer)  
    if menu.get()=='pancreas' and T=='3' and N=='1' and M=='0':
        answer='IIB'
        Entry.insert(E5,0,answer) 
    if menu.get()=='pancreas' and T=='1' and N=='2' and M=='0':
        answer='III'
        Entry.insert(E5,0,answer)
    if menu.get()=='pancreas' and T=='2' and N=='2' and M=='0':
        answer='III'
        Entry.insert(E5,0,answer)
    if menu.get()=='pancreas' and T=='3' and N=='2' and M=='0':
        answer='III'
        Entry.insert(E5,0,answer)
    if menu.get()=='pancreas' and T=='4' and M=='0':
        answer='III'
        Entry.insert(E5,0,answer)
    if menu.get()=='pancreas'  and M=='1':
        answer='IV'
        Entry.insert(E5,0,answer) 
    if menu.get()=='liver' and T=='1a' and N=='0' and M=='0':
        answer='IA'
        Entry.insert(E5,0,answer)    
    if menu.get()=='liver' and T=='1b' and N=='0' and M=='0':
        answer='IB'
        Entry.insert(E5,0,answer)  
    if menu.get()=='liver' and T=='2' and N=='0' and M=='0':
        answer='II'
        Entry.insert(E5,0,answer)  
    if menu.get()=='liver' and T=='3' and N=='0' and M=='0':
        answer='IIIA'
        Entry.insert(E5,0,answer) 
    if menu.get()=='liver' and T=='4' and N=='0' and M=='0':
        answer='IIIB'
        Entry.insert(E5,0,answer)
    if menu.get()=='liver'  and N=='1' and M=='0':
        answer='IVA'
        Entry.insert(E5,0,answer) 
    if menu.get()=='liver'  and M=='1':
        answer='IVB'
        Entry.insert(E5,0,answer)          
    
def clear_text():
        E2.delete(0, END)
        E3.delete(0, END)
        E4.delete(0, END)
        E5.delete(0, END)
        menu.set(tumor_list[0])

ResetB = ttk.Button(top, text="Click Here to Reset", command=clear_text).grid(row=7,column=1, pady = 5)
    
B=ttk.Button(top, text ="Submit",command= proces).grid(row=6, column=1, pady = 5)
C=ttk.Button(top, text='Click for more info',command=popup).grid(row=8,column=1, pady=5)
top.mainloop()

