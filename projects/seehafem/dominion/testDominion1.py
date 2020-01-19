# -*- coding: utf-8 -*-
"""
Created on Thur Jan 16 19:25:46 2020

@author: seehafem
"""

import Dominion
import testUtility

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#Set up the number of curses and victory cards
nC = testUtility.getCurseCardCount(len(player_names))
nV = testUtility.getVictoryCardCount(len(player_names))

#Define box
box = testUtility.getBox(nV)

#Set supply order displayed when running the game
supply_order = testUtility.getSupplyOrder()

#Form the supply with 10 random cards from the box and all other standard setup.
supply = testUtility.getSupply(len(player_names), box, nC, nV, 10)

#INTRODUCE BUG: Change the cards called provinces in the supply to actually be estates
supply["Province"] = [Dominion.Estate()] * nV

#Initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.getPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)