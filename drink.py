import tkinter as tk

from tkinter import *

# 建立主視窗 Frame
window = tk.Tk()

# 設定視窗標題
window.title('COUGAR 訂飲料系統')

# 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("800x600+250+150")


window.LabelFrame(window,text=txt, font=('Arial', 12), width=100, height=2)
# 執行主程式
window.mainloop()
