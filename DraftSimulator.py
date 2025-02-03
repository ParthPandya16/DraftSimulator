from tkinter import *

window = Tk()
window.geometry("840x940")
window.title("ScoutGPT")
#icon = PhotoImage(file = 'logo.png')
#window.iconphoto(True, icon)
window.config(background = "black")
title_label = Label(window, text = "ScoutGPT Draft Simulator", font = ('Arial', 40, 'bold'), fg = 'white', bg = 'green')
title_label.pack()

window.mainloop()