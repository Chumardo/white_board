from tkinter import *
from tkinter import Scale
from turtle import bgcolor


window = Tk()
window.minsize(1290,700)
window.title("White Board")
window.iconphoto(False, PhotoImage(file='images/icon.png'))

canvas = Canvas(window, bg='white', bd=5, relief=GROOVE, height=580, width=1260)
canvas.place(x=10,y=100)

color_frame = LabelFrame(window, text='Colors', relief=RIDGE, bg="white", font=('arial', 15, 'bold'))
color_frame.place(x=10,y=10, width=665, height=75)

tool_frame = LabelFrame(window, text='Tools', relief=RIDGE, bg="white", font=('arial', 15, 'bold'))
tool_frame.place(x=800,y=10, width=190, height=75)

size = LabelFrame(window, text='Size', relief=RIDGE, bg="white", font=('arial', 15, 'bold'))
size.place(x=1100,y=10, width=180, height=75)


colors = ["#FF0000", "#008000", "#FFC0CB","#FFA500",
            "#FFFF00", "#008000", "#0000FF", "#A42A2A",
            "#FFFFFF", "#000000", "#808080", "#87CEEB"]

i=j=0
for color in colors:
    Button(color_frame, bd=3, bg=color, relief=RIDGE, width=3).grid(row=j, column=i, padx=1)
    i += 1

canvas_button = PhotoImage(file='images/canvas.png', height=30, width=30)
canvas_color_b1 = Button(tool_frame, image=canvas_button)
canvas_color_b1.grid(row=0,column=0, padx=5)

save_button = PhotoImage(file='images/save.png', height=30, width=30)
save_b2 = Button(tool_frame, image=save_button)
save_b2.grid(row=0, column=1, padx=5)


eraser_button = PhotoImage(file='images/eraser.png', height=30, width=30)
eraser_b3 = Button(tool_frame, image=eraser_button)
eraser_b3.grid(row=0, column=3, padx=5)

clear_button = PhotoImage(file='images/clear.png', height=30, width=30)
clear_b4 = Button(tool_frame, image=clear_button)
clear_b4.grid(row=0, column=4, padx=5)


size = Scale(size, bg='white', orient=HORIZONTAL, from_=0, to=50, length=170)
size.grid(row=0,column=0)

window.mainloop()