import tkinter as tk
from tkinter import filedialog
import tkinter.font as font 

def openFile():
    
    def filepath_in():
        filepath = filedialog.askopenfilename(initialdir="D:\\Saad\\KIT College\\Projects\\Smart_CCTV\\visitors\\in")

    def filepath_out():
        filepath = filedialog.askopenfilename(initialdir="D:\\Saad\\KIT College\\Projects\\Smart_CCTV\\visitors\\out")
    root = tk.Tk()
    root.geometry("480x100")
    root.title("Visitors")

    label = tk.Label(root,text="Select Folder")
    label.grid(row=0,columnspan=2)
    label_font = font.Font(size=35, weight='bold', family="Helvetica")
    label['font'] = label_font

    btn_font = font.Font(size=25)
    

    button1 = tk.Button(root, text="In ", command=filepath_in, height=2, width=20)
    button1.grid(row=1, column=0, pady=(10,10), padx=(5,5))
    button1['font'] = btn_font

    button2 = tk.Button(root, text="Out ", command=filepath_out, height=2, width=20)
    button2.grid(row=1, column=1,pady=(10,10), padx=(5,5))
    button2['font'] = btn_font
    root.mainloop()