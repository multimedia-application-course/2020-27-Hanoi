import tkinter as tk
global n
global pole_number
n=5  #设置一个默认值
pole_number=3
window=tk.Tk()
window.title("汉诺塔")
window.geometry("500x300")
lable1=tk.Label(window,text="设置汉诺塔上盘子的个数(默认5个)",font=("Arial",12),width=30,height=2)
button1=tk.Button(window,text="确定",command=window.quit)

lable2=tk.Label(window,text="设置汉诺塔上柱子的个数",font=("Arial",12),width=30,height=2)


def print_selection(v):
    global n
    l.config(text='you have selected ' + v)
    n=int(v)
s = tk.Scale(window,from_=1, to=8, orient=tk.HORIZONTAL, length=200, showvalue=1,tickinterval=1, resolution=1, command=print_selection)
l = tk.Label(window, bg='green', fg='white', width=20, text='empty')

def print_selection(v):
    global pole_number
    l2.config(text='you have selected ' + v)
    pole_number=int(v)
s2 = tk.Scale(window,from_=3, to=5, orient=tk.HORIZONTAL, length=200, showvalue=1,tickinterval=1, resolution=1, command=print_selection)
l2 = tk.Label(window, bg='green', fg='white', width=20, text='empty')

lable1.pack()
l.pack()
s.pack()
lable2.pack()
l2.pack()
s2.pack()
button1.pack()
window.mainloop()
