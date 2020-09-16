import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()

root.wm_attributes("-alpha", 0.71)
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
lframe = tk.Frame(root, bg="#272727")
lframe.pack()
label_img = tk.Label(lframe, image = photo, bg='#181818', bd = 10)
label_img.pack(padx=1, pady=1)

cnt = 0

def motion(event):
    global cnt
    print("event", cnt, event)
    cnt += 1
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-topmost", False)
    # root.state('iconic')
    #        WIN32                  VK_LWIN + D

# root.bind('<FocusOut>', motion)

back_window = tk.Toplevel()
back_window.wm_attributes("-topmost", True)
back_window.overrideredirect(True)

back_window.bind('<Button-1>', motion)

root.geometry("+770+535")
root.mainloop()