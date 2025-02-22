from tkinter import *
import numpy as np
import time
import csv


#initializing the window and the background
window = Tk()
window.geometry("1700x900")
window.title("ScoutGPT")
window.config(background = "black")
small_logo = PhotoImage(file = 'Small_logo.png')
window.iconphoto(True, small_logo)
background = PhotoImage(file = "Background.png")
background_label = Label(window, image = background)
background_label.place(x = 25, y = 0)

#images for each prospect
travis_hunter = PhotoImage(file = "TravisHunter.png")
travis_hunter_label = Label(window, image = travis_hunter)


#draft data
current_pick = 1
csv_file_path = 'Player_data.csv'
available_players = []
with open(csv_file_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        available_players.append(row[0])
#print(available_players)
drafted_players = []
teams = ["Titans", "Browns", "Giants", "Patriots", "Jaguars", "Raiders", "Jets", "Panthers",
         "Saints", "Bears", "49ers", "Cowboys", "Dolphins", "Colts", "Falcons", "Cardinals",
         "Bengals", "Seahawks", "Buccaneers", "Broncos", "Steelers", "Chargers", "Packers", "Vikings",
         "Texans", "Rams", "Ravens", "Lions", "Commanders", "Bills", "Chiefs", "Eagles"]



#drafts a player
def draft():
    #goes through the list of available players, and assigns weights to them
    for current_player in available_players:
        break
    #finds the player with the highest weight
    selected_player = available_players[0] #testing for now
    #adds player to drafted_players list and removes player from available_player list
    drafted_players.append(selected_player)
    #available_players.remove(selected_player)
    return selected_player

#updates the GUI
def update_draft_board(selected_player):
    travis_hunter_label.place(x=152, y=175) #testing for now
    return 0


for current_team in teams:
    selected_player = draft()
    print(str(current_pick) + ": " + current_team + " - " + selected_player)
    update_draft_board(selected_player)
    time.sleep(1)
    current_pick += 1

#window.mainloop()
