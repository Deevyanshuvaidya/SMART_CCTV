import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
from finaltestface import in_out
from openFile import openFile
from record import record
from identify import maincall

def main():
    window = tk.Tk()
    window.title("Smart CCTV")
    window.iconphoto(False,tk.PhotoImage(file='icons/mn.png'))
    window.geometry('1080x700+250+50')

    frame1 = tk.Frame(window)

    label_title = tk.Label(frame1, text="Smart CCTV Camera")
    label_font = font.Font(size=35, weight='bold',family='Helvetica')
    label_title['font'] = label_font
    label_title.grid(pady=(10,10), column=2)

    icon = Image.open('icons/spy.png')
    icon = icon.resize((150,150), Image.LANCZOS)
    icon = ImageTk.PhotoImage(icon)
    label_icon = tk.Label(frame1, image=icon)
    label_icon.grid(row=1, pady=(5,10), column=2)

    btn1_image = Image.open('icons/security-camera.png')
    btn1_image = btn1_image.resize((50,50), Image.LANCZOS)
    btn1_image = ImageTk.PhotoImage(btn1_image)

    btn2_image = Image.open('icons/file.png')
    btn2_image = btn2_image.resize((50,50), Image.LANCZOS)
    btn2_image = ImageTk.PhotoImage(btn2_image)

    btn5_image = Image.open('icons/exit.png')
    btn5_image = btn5_image.resize((50,50), Image.LANCZOS)
    btn5_image = ImageTk.PhotoImage(btn5_image)

    btn6_image = Image.open('icons/lamp.png')
    btn6_image = btn6_image.resize((50,50), Image.LANCZOS)
    btn6_image = ImageTk.PhotoImage(btn6_image)

    btn7_image = Image.open('icons/incognito.png')
    btn7_image = btn7_image.resize((50,50), Image.LANCZOS)
    btn7_image = ImageTk.PhotoImage(btn7_image)


    # --------------- Button -------------------#
    btn_font = font.Font(size=25)

    btn1 = tk.Button(frame1, text='Record', height=90, width=180, fg='maroon',command = record, image=btn1_image, compound='left')
    btn1['font'] = btn_font
    btn1.grid(row=3, pady=(20,10))

    btn2 = tk.Button(frame1, text='Visitors', height=90, width=180, fg='maroon', command=openFile, compound='left', image=btn2_image)
    btn2['font'] = btn_font
    btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))

    btn5 = tk.Button(frame1, height=90, width=180, fg='maroon', command=window.quit, image=btn5_image)
    btn5['font'] = btn_font
    btn5.grid(row=6, pady=(20,10), column=2)

    btn6 = tk.Button(frame1, text='Identification', height=90, width=240, fg='maroon', command=maincall, image=btn6_image, compound='left')
    btn6['font'] = btn_font
    btn6.grid(row=5, pady=(20,10), column=2)

    btn7 = tk.Button(frame1, text="In Out", fg="maroon",command=in_out, compound='left', image=btn7_image, height=90, width=180)
    btn7['font'] = btn_font
    btn7.grid(row=3, column=2, pady=(20,10))



    frame1.pack() 
    window.mainloop()

main()
