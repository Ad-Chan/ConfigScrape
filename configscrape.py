from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import shutil
from player import Player
import os.path
from os import path
from selenium.webdriver.common.by import By

largelist = []
players = []

if path.exists("proconfig.txt"):
    #print("Local file found!")
    file1 = open("proconfig.txt", "r")
else:
    print("Local file not found! Please create a new file before searching!")
    file1 = open("proconfig.txt", "w")

print("Welcome to Stosh's CSGO pro config program!")
print("Commands:")
print("[U] = update/create local file from prosettings.net")
print("[S] = search from local file")

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
        browser = webdriver.Firefox(options = options)
        browser.get("https://prosettings.net/cs-go-pro-settings-gear-list/")
        print("Opening headless browser...")
        #browser.refresh()
        nav = browser.find_element_by_tag_name("tbody")

        table_id = browser.find_element(By.ID,"table_1")
        rows = table_id.find_elements(By.TAG_NAME, "tr")
        tbody = table_id.find_element_by_tag_name("tbody")
        fullText = []
        for row in rows:
            #newPlayer = Player()
            newLine = []
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                newLine.append(col.text)
                #newPlayer.addToConfig(col.text)
            #if newPlayer.checkPlayer == True:
            #players.append(newPlayer)
            if len(newLine) != 0:                
                fullText.append(newLine)
        
        for i in fullText:
            for j in i:
                if j == "":
                    i.remove(j)
            #i.pop()

        #fullText.pop(0)
        fullText.pop(-1)

        for i in fullText:
            newPlayer = Player()
            for j in i:
                newPlayer.addToConfig(j)
            newPlayer.setInfo()
            newPlayer.removeFromConfig("Config")
            players.append(newPlayer)

        #tempString = ""
        #print("Processing data...")
        #for line in nav.text:
        #    if line != '\n':
        #        tempString += line
        #    else:
        #        largelist.append(tempString) 
                #print(tempString)           
        #        tempString = ""
        #for text in largelist:
        #    temptext = text.split()
        #    newPlayer = Player()
        #    for i in temptext:
        #        newPlayer.addToConfig(i)
        #    newPlayer.setInfo()
        #    newPlayer.removeFromConfig("Config")
        #    players.append(newPlayer)

        print("Printing configs")
        for player in players:
            player.printConfig()
            file1.write(player.returnConfig())
            file1.write("\n")

        file1.close()

    elif mode == 'S':
        largelist.clear()
        players.clear()
        file2 = open("proconfig.txt", "r")
        for line in file2:
            largelist.append(line)
        
        for text in largelist:
            temptext = text.split("|")
            newPlayer = Player()
            for i in temptext:
                newPlayer.addToConfig(i)
            newPlayer.setInfo()
            newPlayer.removeFromConfig("Config")
            players.append(newPlayer)
        file2.close()

        searchPlayer = input("Type search terms\n[B] to go back\n")
        searchPlayer = searchPlayer.split()
        first = False
        while searchPlayer[0] != "B":
            if first == True:        
                searchPlayer = input("Type search terms\n[B] to go back\n")
                searchPlayer = searchPlayer.split()
            printList = []
            if searchPlayer[0] == "B":
                break
            #searchTerm = input("Type a search term(s):\n")
            #searchTerm = searchTerm.split()
            for player in players:
                if player.findSimilar(searchPlayer) == True:
                    printList.append(player)
            if len(printList) > 0:
                print("Found " + str(len(printList)) + " player(s)")
                for player in printList:
                    player.printConfig()
                    #print("\n")
            if len(printList) <= 0:
                print("Players not found") 
            first = True     
    firstmain = True


