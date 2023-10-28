import pyqrcode
from tkinter import *
from PIL import Image, ImageTk

def generate():
    link_name = linkname_entry.get()
    link = url_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = Image.open(file_name)
    photo = ImageTk.PhotoImage(image=image)
    img_label.config(image=photo)
    img_label.photo = photo

root = Tk()

canvas = Canvas(root, height=600, width=400)
canvas.pack()

qr_name = Label(root, text="QR Code Generator", fg="red", font=('Arial', 30))
canvas.create_window(200, 50, window=qr_name)

link_name = Label(root, text="Link name", fg="blue")
canvas.create_window(200, 100, window=link_name)

url_name = Label(root, text="Link URL", fg="blue")
canvas.create_window(200, 160, window=url_name)

linkname_entry = Entry(root)
canvas.create_window(200, 120, window=linkname_entry)

url_entry = Entry(root)
canvas.create_window(200, 180, window=url_entry)

button_gen = Button(root, text="Generate QR code", command=generate)
canvas.create_window(200, 220, window=button_gen)

img_label = Label(root)
canvas.create_window(200, 300, window=img_label)

root.mainloop()
