import tkinter as tk
from PIL import Image, ImageTk
import re
import win32gui, win32con, win32com.client, win32api
import time
import os


def _window_enum_callback(hwnd, wildcard):

    if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
        win32gui.BringWindowToTop(hwnd)
        # 先发送一个alt事件，否则会报错导致后面的设置无效：pywintypes.error: (0, 'SetForegroundWindow', 'No error message is available')
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        # 设置为当前活动窗口
        win32gui.SetForegroundWindow(hwnd)

def wake(event):
    # WIN32 WIN + D
    win32api.keybd_event(91, 0, 0, 0)
    win32api.keybd_event(68, 0, 0, 0)
    win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)

    # Wake timetable window
    # root.wm_attributes("-topmost", True)
    # root.wm_attributes("-topmost", False)

    time.sleep(0.1)

    # os.system("refresh.bat")

    time.sleep(1)

    try:
        back_backup.destroy()
    except:
        pass

    back_backup = tk.Toplevel()
    back_backup.wm_attributes("-topmost", True)
    back_backup.overrideredirect(True)
    back_backup.geometry("10x50+1362+728")

    back_backup.bind('<Button-1>', wake)

    # win32gui.EnumWindows(_window_enum_callback, ".*%s.*" % 'tk')
    # win32gui.EnumWindows(_window_enum_callback, ".*%s.*" % 'maintk')

back_window = tk.Tk()#bg='green')#"#1d1d1d")
# back_window.wm_attributes("-alpha", 0.01)
back_window.wm_attributes("-topmost", True)
back_window.overrideredirect(True)
back_window.geometry("10x50+1362+728")
# back_window.geometry("100x100+0+720")

back_window.bind('<Button-1>', wake)


root = tk.Toplevel()

root.wm_attributes("-alpha", 0.71)
root.overrideredirect(True)

img = Image.open('img.png')
img = img.resize((450, 150), Image.ANTIALIAS)

photo = ImageTk.PhotoImage(img)
lframe = tk.Frame(root, bg="#272727")
lframe.pack()
label_img = tk.Label(lframe, image = photo, bg='#181818', bd = 10)
label_img.pack(padx=1, pady=1)

root.geometry("+770+535")

back_window.mainloop()