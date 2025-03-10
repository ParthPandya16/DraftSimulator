from tkinter import *
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
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
travis_hunter = Label(window, image = PhotoImage(file = "travis_hunter.png"))
'''
abdul_carter = Label(window, image = PhotoImage(file = "abdul_carter.png"))
mason_graham = Label(window, image = PhotoImage(file = "mason_graham.png"))
shedeur_sanders = Label(window, image = PhotoImage(file = "shedeur_sanders.png"))
will_johnson = Label(window, image = PhotoImage(file = "will_johnson.png"))
tetairoa_mcmillan = Label(window, image = PhotoImage(file = "tetairoa_mcmillan.png"))
cam_ward = Label(window, image = PhotoImage(file = "cam_ward.png"))
will_campbell = Label(window, image = PhotoImage(file = ".png"))
ashton_jeanty = Label(window, image = PhotoImage(file = ".png"))
kelvin_banks_jr = Label(window, image = PhotoImage(file = ".png"))
mykel_williams = Label(window, image = PhotoImage(file = ".png"))
malakai_starks = Label(window, image = PhotoImage(file = ".png"))
tyler_warren = Label(window, image = PhotoImage(file = ".png"))
james_pearce_jr = Label(window, image = PhotoImage(file = ".png"))
luther_burden_iii = Label(window, image = PhotoImage(file = ".png"))
jalon_walker = Label(window, image = PhotoImage(file = ".png"))
colston_loveland = Label(window, image = PhotoImage(file = ".png"))
emeka_egbuka = Label(window, image = PhotoImage(file = ".png"))
kenneth_grant = Label(window, image=PhotoImage(file=".png"))
mike_green = Label(window, image=PhotoImage(file=".png"))
josh_simmons = Label(window, image=PhotoImage(file=".png"))
nic_scourton = Label(window, image=PhotoImage(file=".png"))
benjamin_morrison = Label(window, image=PhotoImage(file=".png"))
shavon_revel_jr = Label(window, image=PhotoImage(file=".png"))
shemar_stewart = Label(window, image=PhotoImage(file=".png"))
jahdae_barron = Label(window, image=PhotoImage(file=".png"))
john_conerly_jr = Label(window, image=PhotoImage(file=".png"))
walter_nolen = Label(window, image=PhotoImage(file=".png"))
tyler_booker = Label(window, image=PhotoImage(file=".png"))
derrick_harmon = Label(window, image=PhotoImage(file=".png"))
armand_membou = Label(window, image=PhotoImage(file=".png"))
jihaad_campbell = Label(window, image=PhotoImage(file=".png"))
tyleik_williams = Label(window, image=PhotoImage(file=".png"))
aireontae_ersery = Label(window, image=PhotoImage(file=".png"))
jack_sawyer = Label(window, image=PhotoImage(file=".png"))
matthew_golden = Label(window, image=PhotoImage(file=".png"))
donovan_jackson = Label(window, image=PhotoImage(file=".png"))
nick_emmanwori = Label(window, image=PhotoImage(file=".png"))
jonah_savaiinaea= Label(window, image=PhotoImage(file=".png"))
landon_jackson = Label(window, image=PhotoImage(file=".png"))
cameron_williams = Label(window, image=PhotoImage(file=".png"))
princely_umanmielen = Label(window, image=PhotoImage(file=".png"))
jt_tuimoloau = Label(window, image=PhotoImage(file=".png"))
trey_amos = Label(window, image=PhotoImage(file=".png"))
omarion_hampton = Label(window, image=PhotoImage(file=".png"))
tre_harris = Label(window, image=PhotoImage(file=".png"))
elic_ayomanor = Label(window, image=PhotoImage(file=".png"))
wyatt_milum = Label(window, image=PhotoImage(file=".png"))
kaleb_johnson = Label(window, image=PhotoImage(file=".png"))
jalen_milroe = Label(window, image=PhotoImage(file=".png"))
xavier_watts = Label(window, image=PhotoImage(file=".png"))
jayden_higgins = Label(window, image=PhotoImage(file=".png"))
alfred_collins = Label(window, image=PhotoImage(file=".png"))
grey_zabel = Label(window, image=PhotoImage(file=".png"))
treveyon_henderson = Label(window, image=PhotoImage(file=".png"))
darius_alexander = Label(window, image=PhotoImage(file=".png"))
tj_sanders = Label(window, image=PhotoImage(file=".png"))
maxwell_hairston = Label(window, image=PhotoImage(file=".png"))
harold_fannin_jr = Label(window, image=PhotoImage(file=".png"))
azareyeh_thomas = Label(window, image=PhotoImage(file=".png"))
quinshon_judkins = Label(window, image=PhotoImage(file=".png"))
donovan_ezeiruaku= Label(window, image=PhotoImage(file=".png"))
quinn_ewers = Label(window, image=PhotoImage(file=".png"))
jared_ivey = Label(window, image=PhotoImage(file=".png"))
jaxson_dart = Label(window, image=PhotoImage(file=".png"))
tate_ratledge = Label(window, image=PhotoImage(file=".png"))
'''

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
#these will be updated once free agency cools down
team_needs = {
    "Titans": ["QB", "DE", "WR"],
    "Browns": ["QB", "OT", "WR"],
    "Giants": ["QB", "CB", "OT"],
    "Patriots": ["WR", "CB", "OT"],
    "Jaguars": ["CB", "WR", "S"],
    "Raiders": ["QB", "WR", "CB"],
    "Jets": ["QB", "DT", "OT"],
    "Panthers": ["DE", "DT", "WR"],
    "Saints": ["TE", "CB", "DT"],
    "Bears": ["OG", "WR", ""],
    "49ers": ["OT", "CB", "DT"],
    "Cowboys": ["RB", "LB", "OG"],
    "Dolphins": ["S", "LB", "DT"],
    "Colts": ["TE", "OG", "CB"],
    "Falcons": ["CB", "DT", "LB"],
    "Cardinals": ["DT", "OG", "OT"],
    "Bengals": ["CB", "DE", "LB"],
    "Seahawks": ["OT", "WR", "QB"],
    "Buccaneers": ["DE", "OG", "OT"],
    "Broncos": ["RB", "TE", "WR"],
    "Steelers": ["QB", "CB", "RB"],
    "Chargers": ["DE", "DT", "S"],
    "Packers": ["WR", "CB", "DE"],
    "Vikings": ["CB", "DT", "S"],
    "Texans": ["WR", "OT", "OG"],
    "Rams": ["CB", "OT", "TE"],
    "Ravens": ["WR", "DE", "S"],
    "Lions": ["DE", "DT", "LB"],
    "Commanders": ["CB", "DE", "OT"],
    "Bills": ["CB", "WR", "S"],
    "Chiefs": ["WR", "OG", "OT"],
    "Eagles": ["OG", "DE", "LB"],
}

df = pd.read_csv("Player_data.csv")
features = ["Overall Rank", "SOS", "Stat Score", "Combine Score"] #, "Position Need", "Past Draft Behavior"
x = df[features]
y = [1] * len(df)
rf = RandomForestClassifier(n_estimators = 100, random_state = 42)
rf.fit(x, y)


#drafts a player
def draft():
    best_player = None
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
    travis_hunter.place(x=152, y=175) #testing for now
    return 0


for current_team in teams:
    selected_player = draft()
    print(str(current_pick) + ": " + current_team + " - " + selected_player)
    update_draft_board(selected_player)
    #time.sleep(1)
    current_pick += 1


window.mainloop()