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
travis_hunter = Label(window, image = PhotoImage(file = "images/travis_hunter.png"))
shedeur_sanders = Label(window, image = PhotoImage(file = "images/shedeur_sanders.png"))
abdul_carter = Label(window, image = PhotoImage(file = "images/abdul_carter.png"))
cam_ward = Label(window, image = PhotoImage(file = "images/cam_ward.png"))

'''
mason_graham = Label(window, image = PhotoImage(file = "mason_graham.png"))
will_johnson = Label(window, image = PhotoImage(file = "will_johnson.png"))
tetairoa_mcmillan = Label(window, image = PhotoImage(file = "tetairoa_mcmillan.png"))
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
'''
csv_file_path = 'Player_data.csv'
available_players = []
with open(csv_file_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        available_players.append(row[0])
print(available_players)
'''
current_pick = 1
available_players = []
drafted_players = []
teams = ["Titans", "Browns", "Giants", "Patriots", "Jaguars", "Raiders", "Jets", "Panthers",
         "Saints", "Bears", "49ers", "Cowboys", "Dolphins", "Colts", "Falcons", "Cardinals",
         "Bengals", "Seahawks", "Buccaneers", "Broncos", "Steelers", "Chargers", "Packers", "Vikings",
         "Texans", "Rams", "Ravens", "Lions", "Commanders", "Bills", "Chiefs", "Eagles"]
team_needs = {
    "Titans": {"QB": 1.0,"WR": 0.9,"RB": 0.6,"TE": 0.0,"OG": 0.1,"OT": 0.5,"DT": 0.7,"DE": 0.8,"LB": 0.3,"CB": 0.2,"S": 0.4},
    "Browns": {"QB": 1.0,"WR": 0.9,"RB": 0.8,"TE": 0.3,"OG": 0.2,"OT": 0.4,"DT": 0.6,"DE": 0.7,"LB": 0.1,"CB": 0.0,"S": 0.5},
    "Giants": {"QB": 0.9,"WR": 0.2,"RB": 0.3,"TE": 0.4,"OG": 0.7,"OT": 1.0,"DT": 0.0,"DE": 0.1,"LB": 0.5,"CB": 0.8,"S": 0.6},
    "Patriots": {"QB": 0.0,"WR": 0.6,"RB": 0.7,"TE": 0.2,"OG": 0.8,"OT": 1.0,"DT": 0.5,"DE": 0.9,"LB": 0.4,"CB": 0.1,"S": 0.3},
    "Jaguars": {"QB": 0.3,"WR": 0.4,"RB": 0.2,"TE": 0.6,"OG": 0.8,"OT": 0.9,"DT": 0.5,"DE": 0.0,"LB": 0.7,"CB": 1.0,"S": 0.1},
    "Raiders": {"QB": 0.8,"WR": 0.9,"RB": 1.0,"TE": 0.0,"OG": 0.3,"OT": 0.4,"DT": 0.1,"DE": 0.2,"LB": 0.5,"CB": 0.7,"S": 0.6},
    "Jets": {"QB": 0.8,"WR": 0.1,"RB": 0.3,"TE": 1.0,"OG": 0.4,"OT": 0.9,"DT": 0.0,"DE": 0.2,"LB": 0.5,"CB": 0.6, "S": 0.7},
    "Panthers": {"QB": 0.0,"WR": 1.0,"RB": 0.1, "TE": 0.6, "OG": 0.7,"OT": 0.5,"DT": 0.9,"DE": 0.2,"LB": 0.3,"CB": 0.4,"S": 0.8},
    "Saints": {"QB": 1.0,"WR": 0.1,"RB": 0.2,"TE": 0.5,"OG": 0.4,"OT": 0.6,"DT": 0.8,"DE": 0.3,"LB": 0.7,"CB": 0.9,"S": 0.0},
    "Bears": {"QB": 0.0,"WR": 0.6,"RB": 0.9,"TE": 0.1,"OG": 0.2,"OT": 1.0,"DT": 0.3,"DE": 0.8,"LB": 0.4,"CB": 0.5,"S": 0.6},
    "49ers": {"QB": 0.0,"WR": 0.3,"RB": 0.1,"TE": 0.2,"OG": 0.9,"OT": 0.7,"DT": 1.0,"DE": 0.8,"LB": 0.4,"CB": 0.5,"S": 0.6},
    "Cowboys": {"QB": 0.6,"WR": 0.7,"RB": 1.0,"TE": 0.2,"OG": 0.5,"OT": 0.9,"DT": 0.0,"DE": 0.1,"LB": 0.3,"CB": 0.4,"S": 0.8},
    "Dolphins": {"QB": 0.0,"WR": 0.2,"RB": 0.1,"TE": 0.4,"OG": 0.7,"OT": 0.8,"DT": 0.9,"DE": 0.6,"LB": 0.3, "CB": 0.5,"S": 1.0},
    "Colts": {"QB": 0.4,"WR": 0.8,"RB": 0.0, "TE": 0.9,"OG": 0.3,"OT": 0.2,"DT": 0.1,"DE": 0.5,"LB": 0.6,"CB": 1.0,"S": 0.7},
    "Falcons": {"QB": 0.1,"WR": 0.3,"RB": 0.0,"TE": 0.2,"OG": 0.5,"OT": 0.4,"DT": 1.0,"DE": 0.9,"LB": 0.7,"CB": 0.8,"S": 0.6},
    "Cardinals": {"QB": 0.2,"WR": 0.3,"RB": 0.4,"TE": 0.0,"OG": 0.6,"OT": 0.7,"DT": 0.5,"DE": 0.9,"LB": 1.0,"CB": 0.9,"S": 0.1},
    "Bengals": {"QB": 0.0,"WR": 0.1,"RB": 0.3,"TE": 0.2,"OG": 0.5,"OT": 0.4,"DT": 0.7,"DE": 0.8,"LB": 0.9,"CB": 1.0,"S": 0.6},
    "Seahawks": {"QB": 0.1,"WR": 0.7,"RB": 0.0,"TE": 0.5,"OG": 1.0,"OT": 0.9,"DT": 0.6,"DE": 0.2,"LB": 0.8,"CB": 0.4,"S": 0.3},
    "Buccaneers": {"QB": 0.1,"WR": 0.6,"RB": 0.0,"TE": 0.2,"OG": 0.9,"OT": 0.3,"DT": 0.4,"DE": 0.8,"LB": 0.7,"CB": 1.0,"S": 0.5},
    "Broncos": {"QB": 0.0,"WR": 0.9,"RB": 1.0,"TE": 0.4,"OG": 0.3,"OT": 0.2,"DT": 0.7,"DE": 0.8,"LB": 0.1,"CB": 0.5,"S": 0.6},
    "Steelers": {"QB": 1.0,"WR": 0.1,"RB": 0.9,"TE": 0.0,"OG": 0.6,"OT": 0.5,"DT": 0.8,"DE": 0.4,"LB": 0.2,"CB": 0.3,"S": 0.7},
    "Chargers": {"QB": 0.0,"WR": 0.3,"RB": 0.6,"TE": 1.0,"OG": 0.2,"OT": 0.1,"DT": 0.7,"DE": 0.8,"LB": 0.4,"CB": 0.9,"S": 0.5},
    "Packers": {"QB": 0.0,"WR": 0.9,"RB": 0.1,"TE": 0.2,"OG": 0.8,"OT": 0.5,"DT": 0.3,"DE": 0.4,"LB": 0.7,"CB": 1.0,"S": 0.5},
    "Vikings": {"QB": 0.0,"WR": 0.3,"RB": 0.4,"TE": 0.1,"OG": 0.2,"OT": 0.8,"DT": 0.5,"DE": 0.7,"LB": 0.6,"CB": 0.9,"S": 1.0},
    "Texans": {"QB": 0.0,"WR": 0.7,"RB": 0.5,"TE": 0.6,"OG": 1.0,"OT": 0.9,"DT": 0.2,"DE": 0.1,"LB": 0.4,"CB": 0.3,"S": 0.8},
    "Rams": {"QB": 0.6,"WR": 0.2,"RB": 0.0,"TE": 0.4,"OG": 0.3,"OT": 1.0,"DT": 0.9,"DE": 0.5,"LB": 0.7,"CB": 0.8,"S": 0.1},
    "Ravens": {"QB": 0.0,"WR": 0.3,"RB": 0.1,"TE": 0.2,"OG": 0.7,"OT": 0.8,"DT": 0.9,"DE": 1.0,"LB": 0.4,"CB": 0.5,"S": 0.6},
    "Lions": {"QB": 0.0,"WR": 0.3,"RB": 0.1,"TE": 0.2,"OG": 0.4,"OT": 0.7,"DT": 0.8,"DE": 0.9,"LB": 0.5,"CB": 1.0,"S": 0.6},
    "Commanders": {"QB": 0.0,"WR": 0.7,"RB": 0.8,"TE": 0.3,"OG": 0.4,"OT": 0.1,"DT": 0.2,"DE": 1.0,"LB": 0.5,"CB": 0.6,"S": 0.9},
    "Bills": {"QB": 0.0,"WR": 0.7,"RB": 0.2,"TE": 0.1,"OG": 0.3,"OT": 0.5,"DT": 0.6,"DE": 0.4,"LB": 0.8,"CB": 0.9,"S": 1.0},
    "Chiefs": {"QB": 0.0,"WR": 0.5,"RB": 0.3,"TE": 0.1,"OG": 0.6,"OT": 1.0,"DT": 0.4,"DE": 0.7,"LB": 0.2,"CB": 0.8,"S": 0.9},
    "Eagles": {"QB": 0.1,"WR": 0.6,"RB": 0.0,"TE": 0.7,"OG": 0.3,"OT": 0.2,"DT": 1.0,"DE": 0.9,"LB": 0.5,"CB": 0.4,"S": 0.8}
}
players = [
    {"name": "Travis Hunter", "position": "WR/CB", "overall rank": 1, "stat score": 182.58, "combine score": 0},
    {"name": "Abdul Carter", "position": "DE", "overall rank": 2, "stat score": 154.5, "combine score": 0},
    {"name": "Mason Graham", "position": "DT", "overall rank": 3, "stat score": 143, "combine score": 0},
    {"name": "Will Campbell", "position": "OT", "overall rank": 4, "stat score": 100, "combine score": 40},
    {"name": "Ashton Jeanty", "position": "RB", "overall rank": 5, "stat score": 197.9, "combine score": 0},
    {"name": "Cam Ward", "position": "QB", "overall rank": 6, "stat score": 172.2, "combine score": 0},
    {"name": "Tetairoa McMillan", "position": "WR", "overall rank": 7, "stat score": 110.6, "combine score": 0},
    {"name": "Shedeur Sanders", "position": "QB", "overall rank": 8, "stat score": 168.2, "combine score": 0},
    {"name": "Armand Membou", "position": "OT", "overall rank": 9, "stat score": 100, "combine score": 80},
    {"name": "Tyler Warren", "position": "TE", "overall rank": 10, "stat score": 90.85, "combine score": 0},
    {"name": "Will Johnson", "position": "CB", "overall rank": 11, "stat score": 67.5, "combine score": 0},
    '''
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    {"name": "", "position": "", "overall rank":, "stat score":, "combine score":},
    '''
]



def score_player(players, teams, team_needs):
    ovr = players["overall rank"]
    stat = players["stat score"]
    comb = players["combine score"]
    raw_score = (66 - ovr) * 0.3 + stat * 0.5 + comb * 0.2
    pos = players["position"]
    position_weight = team_needs[teams].get(players['position'], 0)
    match_score = position_weight
    overall_score = raw_score + match_score
    return overall_score


def make_pick(self):
    if self.current_pick >= len(self.teams):
        return  # Draft is complete

    team = self.teams[self.current_pick]

    if team not in self.team_needs:
        print(f"No team needs data found for {team}")
        return

    # Score each available player for the current team
    best_player = None
    best_score = float('-inf')
    for player in self.available_players:
        score = score_player(player, team, self.team_needs)
        print(player)
        if score > best_score:
            best_score = score
            best_player = player

    if best_player:
        self.available_players.remove(best_player)
        self.drafted_players.append((team, best_player))
        print(f"{team} selected {best_player['name']} (Position: {best_player['position']}, Score: {round(best_score, 2)})")
        self.current_pick += 1

def run_draft(self):
    while self.current_pick < len(self.teams):
        self.make_pick()

run_draft()


'''
weights = {'Overall Rank': 0.4,'SOS': 0.1,'expert_rank_score': 0.3}

player_overall_score =
team_need_score =
draft_score = 0.6 * team_need_score + 0.4 * player_overall_score
'''
df = pd.read_csv("Player_data.csv")
player_features = ["Overall Rank", "SOS", "Stat Score", "Combine Score"] #, "Position Need",
X = df[player_features] #, team_needs
y = [1] * len(df)
rf = RandomForestClassifier(n_estimators = 100, random_state = 42)
rf.fit(X, y)
#print(rf.classes_)





'''
#drafts a player
def draft():
    global current_pick

    current_team = teams[current_pick - 1]
    needs = team_needs[current_team]

    best_score = -1
    best_player = None

    for _, row in df.iterrows():
        player_name = row['Prospect Name']
        player_position = row['Position']

        if player_name in drafted_players:
            continue  # skip already picked players

        position_bonus = 1.5 if player_position in needs else 1.0
        player_features = np.array([[row["Overall Rank"], row["SOS"], row["Stat Score"], row["Combine Score"]]])
        base_score = rf.predict_proba(player_features)[0][1]  # probability of being a good pick
        final_score = base_score * position_bonus

        if final_score > best_score:
            best_score = final_score
            best_player = player_name

    if best_player:
        drafted_players.append(best_player)
        available_players.remove(best_player)

    return best_player if best_player else available_players[0]  # fallback
'''

def update_draft_board(selected_player):
    try:
        img = PhotoImage(file=f"{selected_player.lower().replace(' ', '_')}.png")
        label = Label(window, image=img)
        label.image = img  # Keep reference to avoid garbage collection
        label.place(x=152, y=175)  # Position to be dynamic later
    except Exception as e:
        print(f"Image for {selected_player} not found: {e}")

'''
for current_team in teams:
    selected_player = draft()
    print(str(current_pick) + ": " + current_team + " - " + selected_player)
    update_draft_board(selected_player)
    #time.sleep(1)
    current_pick += 1
'''

window.mainloop()