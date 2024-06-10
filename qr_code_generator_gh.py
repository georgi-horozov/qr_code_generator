import os
from tkinter import *
import qrcode

if not os.path.exists("Qrcode"):
    os.makedirs("Qrcode")

wnd = Tk()
wnd.title("QR code generator")
wnd.geometry("600x700")
wnd.resizable(False, False)
wnd.config(bg="#E3CF57")


# wnd_icon = PhotoImage(file="icon.png")
# wnd.iconphoto(False, wnd_icon)


def generate():
    name_qr = title.get()
    entry_qr = insert_link.get()
    qr = qrcode.make(entry_qr)
    qr.save("Qrcode/" + str(name_qr) + ".png")

    global Image
    Image = PhotoImage(file="Qrcode/" + str(name_qr) + ".png")
    Image_view.config(image=Image)


Image_view = Label(wnd, bg="#E3CF57")
Image_view.pack(padx=50, pady=15, side=BOTTOM)


Label(wnd, text="Title of QR code", fg="#000000", bg="#E3CF57", font="arial 18").place(x=50, y=50)

title = Entry(wnd, width=20, font="arial 15")
title.place(x=50, y=90)

Label(wnd, text="Insert link", fg="#000000", bg="#E3CF57", font="arial 18").place(x=50, y=130)

insert_link = Entry(wnd, width=45, font="arial 15")
insert_link.place(x=50, y=170)

Button(wnd, text="Create", width=20, height=2, fg="white", bg="#000000", bd=1, font="arial 10", command=generate).place(x=50, y=210)


wnd.mainloop()