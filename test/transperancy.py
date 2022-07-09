from tkinter import *
import tkinter.ttk
from pyparsing import alphas

if __name__=='__main__':
    root = Tk()

    root.title("burst shot")
    # root.attributes('-fullscreen', True)
    #root.resizable(False, False)
    
    labelTime = Label(root, text='strTest', font=('Helvetica', 200), fg='red')
    labelTime.pack()

    root.config(bg='#4a7a8c')
    root.wm_attributes('-transparentcolor','#4a7a8c')
    
    root.geometry('800x600')
    root.mainloop()