import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()

root.wm_attributes("-alpha", 0.6)
# root.wm_attributes("-toolwindow", True)
# root.wm_attributes("-topmost", True)
root.overrideredirect(True)


img = Image.open('img.png')

# print(img.size())
# w = img.width()
# h = img.height()

# set_height = 200
# w = w * set_height / h
# h = set_height
img = img.resize((450, 150), Image.ANTIALIAS)


photo = ImageTk.PhotoImage(img)
label_img = tk.Label(root, image = photo)
label_img.pack()

root.geometry("+780+530")
root.mainloop()