from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", 'Monkeys can live upto 300 years.')
answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if answer ==  'yes':
    print(' B===D-')

root.mainloop()