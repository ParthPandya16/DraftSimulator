from tkinter import *
import numpy as np

window = Tk()
window.geometry("1700x900")
window.title("ScoutGPT")
window.config(background = "black")
small_logo = PhotoImage(file = 'Small_logo.png')
window.iconphoto(True, small_logo)

background = PhotoImage(file = "Background.png")
background_label = Label(window, image = background)
background_label.place(x = 25, y = 0)

teams = ["Titans", "Browns", "Giants", "Patriots", "Jaguars", "Raiders", "Jets", "Panthers",
         "Saints", "Bears", "49ers", "Cowboys", "Dolphins", "Colts", "Falcons", "Cardinals",
         "Bengals", "Seahawks", "Buccaneers", "Broncos", "Steelers", "Chargers", "Packers", "Vikings",
         "Texans", "Rams", "Ravens", "Lions", "Commanders", "Bills", "Eagles", "Chiefs"]

current_pick = 1
for current_team in teams:
    #draft()
    print(str(current_pick) + ": " + current_team)
    current_pick += 1

window.mainloop()