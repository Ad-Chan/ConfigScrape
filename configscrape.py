from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import shutil
from player import Player
import os.path
from os import path

largelist = []
players = []

if path.exists("proconfig.txt"):
    print("Local file found!")
    file1 = open("proconfig.txt", "r")
else:
    print("Local file not found! Please create a new file before searching!")
    file1 = open("proconfig.txt", "w")

print("Welcome to Stosh's CSGO pro config program!")
print("Commands:")
print("U = update/create local file from prosettings.net")
print("S = search from local file")

mode = input("Enter command: ")
firstmain = False
while mode != "exit":
    if firstmain == True:
        mode = input("Enter command: ")
    if mode == 'U':
        file1.close()
        file1 = open("proconfig.txt", "w")
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(options=options)
        browser.get("https://prosettings.net/cs-go-pro-settings-gear-list/")
        print("Opening headless browser...")
        browser.refresh()
        nav = browser.find_element_by_tag_name("tbody")

        tempString = ""
        print("Processing data...")
        for line in nav.text:
            if line != '\n':
                tempString += line
            else:
                largelist.append(tempString) 
                #print(tempString)           
                tempString = ""
        for text in largelist:
            temptext = text.split()
            newPlayer = Player()
            for i in temptext:
                newPlayer.addToConfig(i)
            newPlayer.setInfo()
            newPlayer.removeFromConfig("Config")
            players.append(newPlayer)

        print("Printing configs")
        for player in players:
            player.printConfig()
            file1.write(player.returnConfig())
            file1.write("\n")

        file1.close()

    elif mode == 'S':
        file2 = open("proconfig.txt", "r")
        for line in file2:
            largelist.append(line)
        
        for text in largelist:
            temptext = text.split()
            newPlayer = Player()
            for i in temptext:
                newPlayer.addToConfig(i)
            newPlayer.setInfo()
            newPlayer.removeFromConfig("Config")
            players.append(newPlayer)
        file2.close()

        searchPlayer = input("[G] for general search\n[T] for team search\n[N] for name search\n[R] for role search\n[B] to go back\n")
        first = False
        while searchPlayer != "B":
            if first == True:        
                searchPlayer = input("[G] for general search\n[T] for team search\n[N] for name search\n[R] for role search\n[B] to go back\n")

            printList = []
            if searchPlayer == 'G':
                searchTerm = input("Type a search term:\n")
                for player in players:
                    if player.findSimilar(searchTerm) == True:
                        printList.append(player)
                if len(printList) > 0:
                    print("Found player(s)")
                    for player in printList:
                        player.printConfig()
                        print("\n")
                if len(printList) <= 0:
                    print("Players not found")
            elif searchPlayer == 'T':
                team = input("Type the name of the team:\n")
                for player in players:
                    if  team.lower() in player.getTeam().lower():
                        printList.append(player)
                if len(printList) > 0:
                    print("Found player(s)")
                    for player in printList:
                        player.printConfig()
                        print("\n")
                if len(printList) <= 0:
                    print("Players not found")

            elif searchPlayer == 'N':
                name = input("Type the name of the player:\n")
                for player in players:
                    if name.lower() in player.getName().lower():
                        printList.append(player)
                if len(printList) > 0:
                    print("Found player(s)")
                    for player in printList:
                        player.printConfig()
                        print("\n")
                if len(printList) <= 0:
                    print("Players not found")  
                  
            elif searchPlayer == 'R':
                role = input("Type the name of the role (AWPer/rifler):\n")
                for player in players:
                    if role.lower() in player.getRole().lower():
                        printList.append(player)
                if len(printList) > 0:
                    print("Found player(s)")
                    for player in printList:
                        player.printConfig()
                        print("\n")
                if len(printList) <= 0:
                    print("Players not found")   
            first = True     
    firstmain = True


