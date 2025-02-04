from tkinter import *

window = Tk()
window.geometry("840x940")
window.title("ScoutGPT")
icon = PhotoImage(file = 'Small_logo.png')
window.iconphoto(True, icon)
window.config(background = "black")
title_label = Label(window, text = "ScoutGPT Draft Simulator", font = ('Arial', 40, 'bold'), fg = 'white', bg = 'green')
title_label.pack()
#draftBackground = PhotoImage(file = "Draft_background.png")
#window.iconphoto(True, draftBackground)


teams = ["Titans", "Browns", "Giants", "Patriots", "Jaguars", "Raiders", "Jets", "Panthers",
         "Saints", "Bears", "49ers", "Cowboys", "Dolphins", "Colts", "Falcons", "Cardinals",
         "Bengals", "Seahawks", "Buccaneers", "Broncos", "Steelers", "Chargers", "Packers", "Vikings"
         "Texans", "Rams", "Ravens", "Lions", "Commanders", "Bills", "Eagles", "Chiefs"]

for current_team in teams:
    print(current_team)

#window.mainloop()