from tkinter import *
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import time
import csv
import pyttsx3
import threading
from PIL import Image, ImageTk
import os

engine = pyttsx3.init()


window = Tk()
window.geometry("1700x900")
window.title("ScoutGPT")
window.config(background = "black")
small_logo = PhotoImage(file = 'Small_logo.png')
window.iconphoto(True, small_logo)
background = PhotoImage(file = "Background.png")
background_label = Label(window, image = background)
background_label.place(x = 10, y = 0)
player_label = {}
starting_x = 137
starting_y = 163
#
img_width = 75
img_height = 75


def load_resized_image(path, width=img_width, height=img_height):
    image = Image.open(path)
    image = image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(image)
travis_hunter_img = load_resized_image("images/travis_hunter.png")
abdul_carter_img = load_resized_image("images/abdul_carter.png")
mason_graham_img = load_resized_image("images/mason_graham.png")
will_campbell_img = load_resized_image("images/will_campbell.png")
ashton_jeanty_img = load_resized_image("images/ashton_jeanty.png")
cam_ward_img = load_resized_image("images/cam_ward.png")
tetairoa_mcmillan_img = load_resized_image("images/tetairoa_mcmillan.png")
shedeur_sanders_img = load_resized_image("images/shedeur_sanders.png")
armand_membou_img = load_resized_image("images/armand_membou.png")
tyler_warren_img = load_resized_image("images/tyler_warren.png")
will_johnson_img = load_resized_image("images/will_johnson.png")
jalon_walker_img = load_resized_image("images/jalon_walker.png")
shemar_stewart_img = load_resized_image("images/shemar_stewart.png")
kelvin_banks_jr_img = load_resized_image("images/kelvin_banks_jr.png")
mykel_williams_img = load_resized_image("images/mykel_williams.png")
mike_green_img = load_resized_image("images/mike_green.png")
colston_loveland_img = load_resized_image("images/colston_loveland.png")
kenneth_grant_img = load_resized_image("images/kenneth_grant.png")
james_pearce_jr_img = load_resized_image("images/james_pearce_jr.png")
josh_simmons_img = load_resized_image("images/josh_simmons.png")
walter_nolen_img = load_resized_image("images/walter_nolen.png")
matthew_golden_img = load_resized_image("images/matthew_golden.png")
jahdae_barron_img = load_resized_image("images/jahdae_barron.png")
jihaad_campbell_img = load_resized_image("images/jihaad_campbell.png")
emeka_egbuka_img = load_resized_image("images/emeka_egbuka.png")
malakai_starks_img = load_resized_image("images/malakai_starks.png")
omarion_hampton_img = load_resized_image("images/omarion_hampton.png")
derrick_harmon_img = load_resized_image("images/derrick_harmon.png")
nick_emmanwori_img = load_resized_image("images/nick_emmanwori.png")
tyler_booker_img = load_resized_image("images/tyler_booker.png")
luther_burden_iii_img = load_resized_image("images/luther_burden_iii.png")
grey_zabel_img = load_resized_image("images/grey_zabel.png")
josh_conerly_jr_img = load_resized_image("images/josh_conerly_jr.png")
donovan_ezeiruaku_img = load_resized_image("images/donovan_ezeiruaku.png")
nic_scourton_img = load_resized_image("images/nic_scourton.png")
shavon_revel_jr_img = load_resized_image("images/shavon_revel_jr.png")
donovan_jackson_img = load_resized_image("images/donovan_jackson.png")
maxwell_hairston_img = load_resized_image("images/maxwell_hairston.png")
jaxson_dart_img = load_resized_image("images/jaxson_dart.png")
aireontae_ersery_img = load_resized_image("images/aireontae_ersery.png")
treveyon_henderson_img = load_resized_image("images/treveyon_henderson.png")
benjamin_morrison_img = load_resized_image("images/benjamin_morrison.png")
tyleik_williams_img = load_resized_image("images/tyleik_williams.png")
landon_jackson_img = load_resized_image("images/landon_jackson.png")
kaleb_johnson_img = load_resized_image("images/kaleb_johnson.png")
azareyeh_thomas_img = load_resized_image("images/azareyeh_thomas.png")
darius_alexander_img = load_resized_image("images/darius_alexander.png")
alfred_collins_img = load_resized_image("images/alfred_collins.png")
jt_tuimoloau_img = load_resized_image("images/jt_tuimoloau.png")
jack_sawyer_img = load_resized_image("images/jack_sawyer.png")
tj_sanders_img = load_resized_image("images/tj_sanders.png")
trey_amos_img = load_resized_image("images/trey_amos.png")
jonah_savaiinaea_img = load_resized_image("images/jonah_savaiinaea.png")
xavier_watts_img = load_resized_image("images/xavier_watts.png")
jayden_higgins_img = load_resized_image("images/jayden_higgins.png")
tre_harris_img = load_resized_image("images/tre_harris.png")
quinshon_judkins_img = load_resized_image("images/quinshon_judkins.png")
princeley_umanmielen_img = load_resized_image("images/princeley_umanmielen.png")
elic_ayomanor_img = load_resized_image("images/elic_ayomanor.png")
tate_ratledge_img = load_resized_image("images/tate_ratledge.png")
cameron_williams_img = load_resized_image("images/cameron_williams.png")
harold_fannin_jr_img = load_resized_image("images/harold_fannin_jr.png")
jalen_milroe_img = load_resized_image("images/jalen_milroe.png")
wyatt_milum_img = load_resized_image("images/wyatt_milum.png")
jared_ivey_img = load_resized_image("images/jared_ivey.png")
quinn_ewers_img = load_resized_image("images/quinn_ewers.png")

player_label['travis_hunter'] = Label(window, image=travis_hunter_img)
player_label['abdul_carter'] = Label(window, image=abdul_carter_img)
player_label['mason_graham'] = Label(window, image=mason_graham_img)
player_label['will_campbell'] = Label(window, image=will_campbell_img)
player_label['ashton_jeanty'] = Label(window, image=ashton_jeanty_img)
player_label['cam_ward'] = Label(window, image=cam_ward_img)
player_label['tetairoa_mcmillan'] = Label(window, image=tetairoa_mcmillan_img)
player_label['shedeur_sanders'] = Label(window, image=shedeur_sanders_img)
player_label['armand_membou'] = Label(window, image=armand_membou_img)
player_label['tyler_warren'] = Label(window, image=tyler_warren_img)
player_label['will_johnson'] = Label(window, image=will_johnson_img)
player_label['jalon_walker'] = Label(window, image=jalon_walker_img)
player_label['shemar_stewart'] = Label(window, image=shemar_stewart_img)
player_label['kelvin_banks_jr'] = Label(window, image=kelvin_banks_jr_img)
player_label['mykel_williams'] = Label(window, image=mykel_williams_img)
player_label['mike_green'] = Label(window, image=mike_green_img)
player_label['colston_loveland'] = Label(window, image=colston_loveland_img)
player_label['kenneth_grant'] = Label(window, image=kenneth_grant_img)
player_label['james_pearce_jr'] = Label(window, image=james_pearce_jr_img)
player_label['josh_simmons'] = Label(window, image=josh_simmons_img)
player_label['walter_nolen'] = Label(window, image=walter_nolen_img)
player_label['matthew_golden'] = Label(window, image=matthew_golden_img)
player_label['jahdae_barron'] = Label(window, image=jahdae_barron_img)
player_label['jihaad_campbell'] = Label(window, image=jihaad_campbell_img)
player_label['emeka_egbuka'] = Label(window, image=emeka_egbuka_img)
player_label['malakai_starks'] = Label(window, image=malakai_starks_img)
player_label['omarion_hampton'] = Label(window, image=omarion_hampton_img)
player_label['derrick_harmon'] = Label(window, image=derrick_harmon_img)
player_label['nick_emmanwori'] = Label(window, image=nick_emmanwori_img)
player_label['tyler_booker'] = Label(window, image=tyler_booker_img)
player_label['luther_burden_iii'] = Label(window, image=luther_burden_iii_img)
player_label['grey_zabel'] = Label(window, image=grey_zabel_img)
player_label['josh_conerly_jr'] = Label(window, image=josh_conerly_jr_img)
player_label['donovan_ezeiruaku'] = Label(window, image=donovan_ezeiruaku_img)
player_label['nic_scourton'] = Label(window, image=nic_scourton_img)
player_label['shavon_revel_jr'] = Label(window, image=shavon_revel_jr_img)
player_label['donovan_jackson'] = Label(window, image=donovan_jackson_img)
player_label['maxwell_hairston'] = Label(window, image=maxwell_hairston_img)
player_label['jaxson_dart'] = Label(window, image=jaxson_dart_img)
player_label['aireontae_ersery'] = Label(window, image=aireontae_ersery_img)
player_label['treveyon_henderson'] = Label(window, image=treveyon_henderson_img)
player_label['benjamin_morrison'] = Label(window, image=benjamin_morrison_img)
player_label['tyleik_williams'] = Label(window, image=tyleik_williams_img)
player_label['landon_jackson'] = Label(window, image=landon_jackson_img)
player_label['kaleb_johnson'] = Label(window, image=kaleb_johnson_img)
player_label['azareyeh_thomas'] = Label(window, image=azareyeh_thomas_img)
player_label['darius_alexander'] = Label(window, image=darius_alexander_img)
player_label['alfred_collins'] = Label(window, image=alfred_collins_img)
player_label['jt_tuimoloau'] = Label(window, image=jt_tuimoloau_img)
player_label['jack_sawyer'] = Label(window, image=jack_sawyer_img)
player_label['tj_sanders'] = Label(window, image=tj_sanders_img)
player_label['trey_amos'] = Label(window, image=trey_amos_img)
player_label['jonah_savaiinaea'] = Label(window, image=jonah_savaiinaea_img)
player_label['xavier_watts'] = Label(window, image=xavier_watts_img)
player_label['jayden_higgins'] = Label(window, image=jayden_higgins_img)
player_label['tre_harris'] = Label(window, image=tre_harris_img)
player_label['quinshon_judkins'] = Label(window, image=quinshon_judkins_img)
player_label['princeley_umanmielen'] = Label(window, image=princeley_umanmielen_img)
player_label['elic_ayomanor'] = Label(window, image=elic_ayomanor_img)
player_label['tate_ratledge'] = Label(window, image=tate_ratledge_img)
player_label['cameron_williams'] = Label(window, image=cameron_williams_img)
player_label['harold_fannin_jr'] = Label(window, image=harold_fannin_jr_img)
player_label['jalen_milroe'] = Label(window, image=jalen_milroe_img)
player_label['wyatt_milum'] = Label(window, image=wyatt_milum_img)
player_label['jared_ivey'] = Label(window, image=jared_ivey_img)
player_label['quinn_ewers'] = Label(window, image=quinn_ewers_img)





class DraftSimulator:
    def __init__(self, teams, team_needs, available_players):
        self.teams = teams  # List of teams
        self.team_needs = team_needs  # Dictionary of team needs
        self.available_players = available_players  # List of available players
        self.drafted_players = []  # List of players that have been drafted
        self.current_pick = 0  # Keeps track of the current pick

    def score_player(self, player, team, team_needs):
        ovr = player["overall rank"]
        stat = player["stat score"]
        comb = player["combine score"]
        raw_score = (66 - ovr) * 0.3 + stat * 0.5 + comb * 0.2
        pos = player["position"]
        position_weight = team_needs.get(team, {}).get(pos, 0)
        match_score = position_weight
        overall_score = (raw_score * 0.4 + match_score * 0.6) * 2
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
            #print(f"Checking player: {player}")  # Debug print to see the player format
            if isinstance(player, dict):  # Ensure player is a dictionary
                score = self.score_player(player, team, self.team_needs)
                if score > best_score:
                    best_score = score
                    best_player = player
            else:
                print(f"Error: Expected a dictionary, but got {type(player)}")

        if best_player:
            self.available_players.remove(best_player)
            self.drafted_players.append((team, best_player))
            print(f"{team} selected {best_player['name']} (Position: {best_player['position']}, Score: {round(best_score, 2)})")
            speech = f"For the 2025 draft, the {team} selects {best_player['name']}"
            engine.say(speech)
            engine.runAndWait()
            x_off = 0
            y_off = 0
            if self.current_pick< 8:
                x_off = 0
                y_off = 75*(self.current_pick) - self.current_pick
            elif self.current_pick< 16:
                x_off = 360
                y_off = 75 * (self.current_pick-8) - self.current_pick%8
            elif self.current_pick < 24:
                x_off = 720
                y_off = 75 * (self.current_pick-16) - self.current_pick%8
            elif self.current_pick < 32:
                x_off = 1080
                y_off = 75 * (self.current_pick-24) - self.current_pick%8
            player_id = best_player['name'].replace(" ", "_").lower()
            player_label[player_id].place(x=starting_x+x_off, y=starting_y+y_off)
            self.current_pick += 1

    def run_draft(self):
        while self.current_pick < len(self.teams):
            self.make_pick()




# Example data for the teams, team needs, and available players
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

available_players = [
    {"name": "travis Hunter", "position": "WR/CB", "overall rank": 1, "stat score": 182.58, "combine score": 0},
    {"name": "Abdul Carter", "position": "DE", "overall rank": 2, "stat score": 164.5, "combine score": 0},
    {"name": "Mason Graham", "position": "DT", "overall rank": 3, "stat score": 143, "combine score": 0},
    {"name": "Will Campbell", "position": "OT", "overall rank": 4, "stat score": 100, "combine score": 40},
    {"name": "Ashton Jeanty", "position": "RB", "overall rank": 5, "stat score": 197.9, "combine score": 0},
    {"name": "Cam Ward", "position": "QB", "overall rank": 6, "stat score": 172.2, "combine score": 0},
    {"name": "Tetairoa McMillan", "position": "WR", "overall rank": 7, "stat score": 110.6, "combine score": 0},
    {"name": "Shedeur Sanders", "position": "QB", "overall rank": 8, "stat score": 168.2, "combine score": 0},
    {"name": "Armand Membou", "position": "OT", "overall rank": 9, "stat score": 100, "combine score": 80},
    {"name": "Tyler Warren", "position": "TE", "overall rank": 10, "stat score": 90.85, "combine score": 0},
    {"name": "Will Johnson", "position": "CB", "overall rank": 11, "stat score": 100.5, "combine score": 0},
    {"name": "Jalon Walker", "position": "LB", "overall rank": 12, "stat score": 118.5, "combine score": 0},
    {"name": "Shemar Stewart", "position": "DE", "overall rank": 13, "stat score": 100.5, "combine score": 60},
    {"name": "Kelvin Banks Jr", "position": "OT", "overall rank": 14, "stat score": 100, "combine score": 0},
    {"name": "Mykel Williams", "position": "DE", "overall rank": 15, "stat score": 82, "combine score": 0},
    {"name": "Mike Green", "position": "DE", "overall rank": 16, "stat score": 150, "combine score": 20},
    {"name": "Colston Loveland", "position": "TE", "overall rank": 17, "stat score": 58.7, "combine score": 0},
    {"name": "Kenneth Grant", "position": "DT", "overall rank": 18, "stat score": 112, "combine score": 0},
    {"name": "James Pearce Jr", "position": "DE", "overall rank": 19, "stat score": 121, "combine score": 0},
    {"name": "Josh Simmons", "position": "OT", "overall rank": 20, "stat score": 100, "combine score": 0},
    {"name": "Walter Nolen", "position": "DT", "overall rank": 21, "stat score": 147, "combine score": 0},
    {"name": "Matthew Golden", "position": "WR", "overall rank": 22, "stat score": 62.3, "combine score": 20},
    {"name": "Jahdae Barron", "position": "CB", "overall rank": 23, "stat score": 111.5, "combine score": -20},
    {"name": "Jihaad Campbell", "position": "LB", "overall rank": 24, "stat score": 160, "combine score": 40},
    {"name": "Emeka Egbuka", "position": "WR", "overall rank": 25, "stat score": 65.9, "combine score": 0},
    {"name": "Malakai Starks", "position": "S", "overall rank": 26, "stat score": 118, "combine score": -60},
    {"name": "Omarion Hampton", "position": "RB", "overall rank": 27, "stat score": 120.9, "combine score": 40},
    {"name": "Derrick Harmon", "position": "DT", "overall rank": 28, "stat score": 131.5, "combine score": 0},
    {"name": "Nick Emmanwori", "position": "S", "overall rank": 29, "stat score": 150, "combine score": 60},
    {"name": "Tyler Booker", "position": "OG", "overall rank": 30, "stat score": 100, "combine score": -80},
    {"name": "Luther Buden III", "position": "WR", "overall rank": 31, "stat score": 66.4, "combine score": 20},
    {"name": "Grey Zabel", "position": "OT", "overall rank": 32, "stat score": 100, "combine score": 20},
    {"name": "Josh Conerly Jr", "position": "OT", "overall rank": 33, "stat score": 100, "combine score": 0},
    {"name": "Donovan Ezeiruaku", "position": "DE", "overall rank": 34, "stat score": 170, "combine score": 20},
    {"name": "Nic Scourton", "position": "DE", "overall rank": 35, "stat score": 125.5, "combine score": 0},
    {"name": "Shavon Revel Jr", "position": "CB", "overall rank": 36, "stat score": 118, "combine score": 0},
    {"name": "Donovan Jackson", "position": "OG", "overall rank": 37, "stat score": 100, "combine score": 20},
    {"name": "Maxwell Hairston", "position": "CB", "overall rank": 38, "stat score": 92.5, "combine score": 60},
    {"name": "Jaxson Dart", "position": "QB", "overall rank": 39, "stat score": 180.7, "combine score": 0},
    {"name": "Aireontae Ersery", "position": "OT", "overall rank": 40, "stat score": 100 , "combine score": 40},
    {"name": "TreVeyon Henderson", "position": "RB", "overall rank": 41, "stat score": 144, "combine score": 60},
    {"name": "Benjamin Morrison", "position": "CB", "overall rank": 42, "stat score": 83.5, "combine score": 0},
    {"name": "Tyleik Williams", "position": "DT", "overall rank": 43, "stat score": 130, "combine score": 0},
    {"name": "Landon Jackson", "position": "DE", "overall rank": 44, "stat score": 140.5, "combine score": 40},
    {"name": "Kaleb Johnson", "position": "RB", "overall rank": 45, "stat score": 145.7, "combine score": -20},
    {"name": "Azareye'h Thomas", "position": "CB", "overall rank": 46, "stat score": 96.5, "combine score": -20},
    {"name": "Darius Alexander", "position": "DT", "overall rank": 47, "stat score": 131.5, "combine score": 20},
    {"name": "Alfred Collins", "position": "DT", "overall rank": 48, "stat score": 133.5, "combine score": -40},
    {"name": "JT Tuimoloau", "position": "DE", "overall rank": 49, "stat score": 160, "combine score": 0},
    {"name": "Jack Sawyer", "position": "DE", "overall rank": 50, "stat score": 159.5, "combine score": 0},
    {"name": "TJ Sanders", "position": "DT", "overall rank": 51, "stat score": 150, "combine score": 0},
    {"name": "Trey Amos", "position": "CB", "overall rank": 52, "stat score": 110, "combine score": -20},
    {"name": "Jonah Savaiinaea", "position": "OT", "overall rank": 53, "stat score": 100, "combine score": 40},
    {"name": "Xavier Watts", "position": "S", "overall rank": 54, "stat score": 132, "combine score": 0},
    {"name": "Jayden Higgins", "position": "WR", "overall rank": 55, "stat score": 91.7, "combine score": 40},
    {"name": "Tre Harris", "position": "WR", "overall rank": 56, "stat score": 129.7, "combine score": 0},
    {"name": "Quinshon Judkins", "position": "RB", "overall rank": 57, "stat score": 154.8, "combine score": 40},
    {"name": "Princeley Umanmielen", "position": "DE", "overall rank": 58, "stat score": 135.5, "combine score": 20},
    {"name": "Elic Ayomanor", "position": "WR", "overall rank": 59, "stat score": 135.5, "combine score": 20},
    {"name": "Tate Ratledge", "position": "OG", "overall rank": 60, "stat score": 100, "combine score": 60},
    {"name": "Cameron Williams", "position": "OT", "overall rank": 61, "stat score": 100, "combine score": 20},
    {"name": "Harold Fanin Jr", "position": "TE", "overall rank": 62, "stat score": 125.4, "combine score": 20},
    {"name": "Jalen Milroe", "position": "QB", "overall rank": 63, "stat score": 148.8, "combine score": 0},
    {"name": "Wyatt Milum", "position": "OT", "overall rank": 64, "stat score": 100, "combine score": -40},
    {"name": "Jared Ivey", "position": "DE", "overall rank": 65, "stat score": 149, "combine score": 0},
    {"name": "Quinn Ewers", "position": "QB", "overall rank": 66, "stat score": 135, "combine score": 0},
]
def run_draft_thread():
    simulator.run_draft()
simulator = DraftSimulator(teams, team_needs, available_players)
draft_thread = threading.Thread(target=run_draft_thread)
draft_thread.start()
window.mainloop()