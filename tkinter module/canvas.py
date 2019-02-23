import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(width=800, height=500)

img = tkinter.PhotoImage(file='tkinter_canvas.png')
canvas.create_image(0, 0, anchor='nw', image=img)

canvas.create_line((100,300), (600,200), fill='white', width=10)

canvas.pack()
root.mainloop()
