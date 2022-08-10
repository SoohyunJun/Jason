from tkinter import *

win = Tk()
win.geometry("500x200")
win.title("What time?")
win.option_add("*Font","궁서 30")

btn=Button(win)
btn.config(text = "호돌이 미팅 - 현재 시각")
btn.config(width = 60, height = 30)

btn.pack()

win.mainloop()



