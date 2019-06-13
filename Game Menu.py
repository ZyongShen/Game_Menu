import os
import subprocess
from tkinter import *



class GameMenu(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.SteamButton = Button(self, text="Steam")
        self.SteamButton["command"] = self.open_steam
        self.SteamButton.grid()

        self.BNetButton = Button(self, text="BNet")
        self.BNetButton["command"] = self.open_bnet
        self.BNetButton.grid()

        self.OriButton = Button(self, text="Origin")
        self.OriButton["command"] = self.open_origin
        self.OriButton.grid()

        self.OSUButton = Button(self, text="OSU")
        self.OSUButton["command"] = self.open_osu
        self.OSUButton.grid()

        self.uplayButton = Button(self,text="Uplay")
        self.uplayButton["command"] = self.open_uplay
        self.uplayButton.grid()

        self.lolButton = Button(self, text="League of Legends")
        self.lolButton["command"] = self.open_lol
        self.lolButton.grid()

        self.epicBtn = Button(self, text="Epic Games")
        self.epicBtn["command"] = self.open_epic
        self.epicBtn.grid()

        self.dolBtn = Button(self, text="Dolphin")
        self.dolBtn["command"] = self.open_dolpin
        self.dolBtn.grid()

        self.ps2Btn = Button(self, text="PCSX2")
        self.ps2Btn["command"] = self.open_ps2
        self.ps2Btn.grid()

        self.nexBtn = Button(self, text="Nexon")
        self.nexBtn["command"] = self.open_nex
        self.nexBtn.grid()

        self.cemuBtn = Button(self, text="Cemu")
        self.cemuBtn["command"] = self.open_cemu
        self.cemuBtn.grid()




    def open_steam(self):
        subprocess.Popen(['C:\Program Files (x86)\Steam\\Steam.exe'])

    def open_bnet(self):
        subprocess.Popen(['C:\Program Files (x86)\Battle.net\\Battle.net Launcher.exe'])

    def open_origin(self):
        subprocess.Popen(['C:\Program Files (x86)\Origin\\Origin.exe'])

    def open_osu(self):
        subprocess.Popen(['C:/Users/pekin/AppData/Local/osu!//osu!.exe'])

    def open_uplay(self):
        subprocess.Popen(['C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher//Uplay.exe'])

    def open_lol(self):
        subprocess.Popen(['C:\Riot Games\League of Legends\\LeagueClient.exe'])

    def open_epic(self):
        subprocess.Popen(['C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\\EpicGamesLauncher.exe'])

    def open_dolpin(self):
        subprocess.Popen(['C:\Program Files\Dolphin\\Dolphin.exe'])

    def open_ps2(self):
        subprocess.Popen(['C:\Program Files (x86)\PCSX2 1.4.0\\pcsx2.exe'])

    def open_nex(self):
        subprocess.Popen(['C:/Program Files (x86)/Nexon/Nexon Launcher//nexon_launcher.exe'])

    def open_cemu(self):
        subprocess.Popen(['C:/Users/pekin/Desktop/Gaming/CEMU Wii U//Cemu.exe'])



root = Tk() # This is making the window
root.title("Game Menu")
root.geometry("200x500")

app = GameMenu(root)
root.mainloop() # Make this whole thing