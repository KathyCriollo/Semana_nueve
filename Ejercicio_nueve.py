#Ejericico nueve
from tkinter import*
tk=Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

my_image = PhotoImage(file="seshomaru.gif")
canvas.create_image(150,150, anchor=NW, image=my_image)
tk.mainloop()