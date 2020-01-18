# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:28:42 2020

@author: seehafem
"""

import Dominion
import testUtility
import random
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#Set up the number of curses and victory cards
nC = testUtility.getCurseCardCount(len(player_names))
nV = testUtility.getVictoryCardCount(len(player_names))

#Define box
box = testUtility.getBox(nV)

#Set supply order displayed when running the game
supply_order = testUtility.getSupplyOrder()

#INTRODUCE BUG: Form the supply with 5 (not 10) random cards from the box and all other standard setup.
supply = testUtility.getSupply(len(player_names), box, nC, nV, 5)

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