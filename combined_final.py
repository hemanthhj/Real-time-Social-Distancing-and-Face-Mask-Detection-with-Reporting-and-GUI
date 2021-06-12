from tkinter import *
from tkinter.ttk import *
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import tkinter as tk
import time
import os
import requests

window = Tk()

window.title("SOCIAL DISTANCING AND FACE MASK DETECTION AND REPORTING")
# window.config(bg="green")
window.geometry('650x505')
window.config(background="khaki2")

lbl = Label(window, text="WELCOME - CHOOSE ONE")
lbl.place(x=100, y=5)

lbl.config(font=("'Comic Sans MS", 25), )

lbl.config(background="gold")


# lbl.grid(column=2, row=1)

def disable_event():
    pass


def facem():
    tkinter.messagebox.showinfo("Welcome to Face Mask Detector.", "You are about to perform Face Mask Detection       "
                                                                  "                                      press "
                                                                  "ok to continue              and              press "
                                                                  "'q' to Quit")
    os.system('python3 newfacemask.py -n prn')


def sociald():
    tkinter.messagebox.showinfo("Welcome to Social Distance Detector.", "You are about to perform Social Distance "
                                                                        "Detection                                    "
                                                                        "  press "
                                                                        "ok to continue           and          press "
                                                                        "'q' to Quit")
    os.system('python3 ipsocial.py')


def facesocial():
    tkinter.messagebox.showinfo("Welcome to Both Face Mask and Social Distance Detector.", "You are about to perform "
                                                                                           "Both Face Mask and Social "
                                                                                           "Distance Detection        "
                                                                                           "     press "
                                                                                           "ok to continue         and "
                                                                                           "          press "
                                                                                           "'q' to Quit")
    os.system('python3 ipbothsocialface.py')


def imform():
    os.system('python3 ipcaptureimage.py')
    files = {
        'photo': open('NewPicture.jpg', 'rb')}

    resp = requests.post('https://api.telegram.org/bot1661354902:AAF45IAEwKkmiyeyLv6dWxoQbjSWZb7DN-4/sendPhoto?chat_id'
                         '=-1001422894866&caption=Personaly reported by security', files=files)

    print(resp.status_code)
    # time.sleep(5)
    tkinter.messagebox.showinfo("Welcome to Inform.", "Report has been sent        press ok to continue")
    print("Done")


def autom():
    tkinter.messagebox.showinfo("Welcome to Automated Face Mask Detector.", "You are about to perform Face Mask "
                                                                            "Detection "
                                                                            "press "
                                                                            "ok to continue              and          "
                                                                            "    press "
                                                                            "'q' to Quit")
    os.system('python3 face_mask_auto_ipwebcam.py')


imagetest = PhotoImage(file="comimg/facereg.png")
imagetest1 = PhotoImage(file="comimg/social.png")
imagetest2 = PhotoImage(file="comimg/bothfi.png")
imagetest3 = PhotoImage(file="comimg/infrmm.png")
imagetest4 = PhotoImage(file="comimg/automatic.png")
imagetest5 = PhotoImage(file="comimg/quitt.png")

bt1 = Button(window, compound="top", text="SOCIAL DISTANCING", image=imagetest1, command=sociald)
bt1.place(x=20, y=280)
# bt1.grid(column=1, row=8)
# bt1.pack()

bt2 = Button(window, compound="top", text="FACE MASK", image=imagetest, command=facem)
bt2.place(x=20, y=50)
# bt2.grid(column=1, row=4)

bt3 = Button(window, compound="top", text="MASK & SOCIAL DISTANCE", image=imagetest2, command=facesocial)
bt3.place(x=230, y=50)
# bt3.grid(column=2, row=4)

bt4 = Button(window, compound="top", text="SECURITY INFORM", image=imagetest3, command=imform)
bt4.place(x=230, y=280)
# bt4.grid(column=3, row=4)

bt5 = Button(window, compound="top", text="AUTOMATION", image=imagetest4, command=autom)
bt5.place(x=440, y=50)
# bt5.grid(column=2, row=8)

bt6 = Button(window, compound="top", text="QUIT", image=imagetest5, command=quit)
bt6.place(x=440, y=280)
# bt6.grid(column=3, row=8)

window.resizable(0, 0)
window.protocol("WM_DELETE_WINDOW", disable_event)
window.mainloop()
