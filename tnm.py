# import 
from tkinter import *
from tkinter import ttk
import pandas as pd
import tkinter.messagebox
import os


# Creating a GUI window, and giving it a title,dimensions and color
root = Tk()
root.resizable(False, False)
root.title("CANCER STAGING")
root.eval("tk::PlaceWindow . center")#place window at center of screen
root.geometry('270x280')
root.config(background =  "#B4B4EE")

# database loading
abs_path = os.path.abspath(os.path.dirname(__file__))
df = pd.read_csv(f'{abs_path}\\tnmdata.csv')


# code to add widgets:

# popup
def popup():
    tkinter.messagebox.showinfo("Info",  " The application uses the 9th American \nJoint Committee on Cancer TNM system\n If data is unknown please enter the value 'x'")

# Dropdown menu options

tumor_types=df['cancer'].unique()
tumor_list = ['Select tumor location']
tumor_list.extend(tumor_types)
# Datatype of menu text
menu= StringVar()
# Initial menu text
menu.set(tumor_list[0]) #default value of dropdown menu

# dropdown menu/entry 1
E1= ttk.OptionMenu(root, menu, *tumor_list)
E1.grid(row=1, column=1)

# labels

L1 = ttk.Label(root, text="Staging",font=("Arial",13), background =  "#B4B4EE").grid(row=0,column=1, padx = 5)
L2 = ttk.Label(root, text="T",font=("Arial",12),background =  "#B4B4EE").grid(row=2,column=0, padx = 10)
L3 = ttk.Label(root, text="N",font=("Arial",12),background =  "#B4B4EE").grid(row=3,column=0, padx = 10)
L4 = ttk.Label(root, text="M",font=("Arial",12),background =  "#B4B4EE").grid(row=4,column=0, padx = 10)
L5 = ttk.Label(root, text="Stage",font=("Arial",12),background =  "#B4B4EE").grid(row=5,column=0, padx = 10)

# entries

E2 = ttk.Entry(root)
E2.grid(row=2,column=1, pady = 5, padx = 25)
E3 = ttk.Entry(root)
E3.grid(row=3,column=1, pady = 5, padx = 25)
E4 = ttk.Entry(root)
E4.grid(row=4,column=1, pady = 5, padx = 25)
E5 = ttk.Entry(root)
E5.grid(row=5,column=1, pady = 5, padx = 25)

# cancer stage calculator

def proces():
    cancer_type=menu.get()

    if cancer_type not in tumor_list[1:]:
        tkinter.messagebox.showinfo('Warning!',f'cancer type is at {cancer_type}')
        return
    T=Entry.get(E2)

    if not T:
        tkinter.messagebox.showinfo('Warning!','Tumor size must be selected!')
        return
    N=Entry.get(E3)

    if not N:
        tkinter.messagebox.showinfo('Warning!','Node status must be selected!')
        return
    M=Entry.get(E4)

    if not M:
        tkinter.messagebox.showinfo('Warning!','Please select if metastasis is present\n by typing 0 for absent or 1 for present')
        return

    if M == '1':
        Entry.insert(E5,0,'IV')
    else:
        cancer_type = df.loc[df['cancer'] == cancer_type]
        query_T = cancer_type[cancer_type['T'] == T]
        query_N = query_T[query_T['N'] == N]
        query_M = query_N[query_N['M'] == M]

        result=query_N['answer'].tolist()
        if result:
            Entry.insert(E5,0,query_N['answer'].tolist())
        else:
            tkinter.messagebox.showinfo('Warning!','Entries not in the database.\n Please review your choices!')
     

# clear text command/deleting the content from the entry box
def clear_text():
        E2.delete(0, END)
        E3.delete(0, END)
        E4.delete(0, END)
        E5.delete(0, END)
        menu.set(tumor_list[0])

# Buttons

ResetB = ttk.Button(root, text="Click Here to Reset", command=clear_text).grid(row=7,column=1, pady = 5)
B=ttk.Button(root, text ="Submit",command= proces).grid(row=6, column=1, pady = 5)
C=ttk.Button(root, text='Click for more info',command=popup).grid(row=9,column=1,pady=5)
root.mainloop()