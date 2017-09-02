import os
import random


def createMaze(xrange,yrange):
    table = [[" " for i in range(xrange)] for j in range(yrange)]
    return table


def displayMaze(table, xrange, yrange):
    outputMaze = ""
    for a in range(0, (xrange*2)+2):
        outputMaze += "-"
    print outputMaze
    for i in range(0, (xrange-1)):
        outputMaze = ""
        for j in range(0, (yrange - 1)):
            outputMaze += table[i][j] + " "
        if 'X' in outputMaze:
            print "| " + outputMaze + " |"
    outputMaze = ""
    for a in range(0, (xrange * 2) + 2):
        outputMaze += "-"
    print outputMaze


def generatePath(table, xrange, yrange, mapLevel):
    randDirection = ["N", "S", "E", "W"]
    xLoc = 0
    yLoc = random.randint(0, (yrange - 2))
    table[yLoc][xLoc] = "S"
    countSteps = 0
    countX = 0
    while (yLoc < (yrange-1)) and (xLoc < (xrange-1)):
        randDir = random.randint(0, 3)
        if randDirection[randDir] == "N" and table[(yLoc-1)][xLoc] == ' ':
            if yLoc > 0 and table[yLoc-1][xLoc-1] == ' ' and table[yLoc-1][xLoc+1] == ' ':
                yLoc -= 1
                table[yLoc][xLoc] = "X"
                countX += 1
        elif randDirection[randDir] == "S" and table[(yLoc+1)][xLoc] == ' ':
           if yLoc < yrange and table[yLoc+1][xLoc-1] == ' ' and table[yLoc+1][xLoc+1] == ' ':
               yLoc += 1
               table[yLoc][xLoc] = "X"
               countX += 1
        elif randDirection[randDir] == "E" and table[yLoc][(xLoc+1)] == ' ':
           if xLoc < xrange and table[yLoc-1][xLoc+1] == ' ' and table[yLoc+1][xLoc+1] == ' ':
               xLoc += 1
               table[yLoc][xLoc] = "X"
               countX += 1
        elif randDirection[randDir] == "W" and table[yLoc][(xLoc-1)] == ' ':
           if xLoc > 0 and table[yLoc-1][xLoc-1] == ' ' and table[yLoc+1][xLoc-1] == ' ':
                xLoc -= 1
                table[yLoc][xLoc] = "X"
                countX += 1
        countSteps += 1
        if countSteps > (xrange * 20):
            break
        elif xLoc == (xrange - 2) and countX > (xrange*2):
            print "XP for Completing: " + str(((countX * mapLevel)/2+50))
            return table, True
        elif xLoc == (xrange - 2) and countX <= (xrange*2):
            break
        elif xLoc >= 1 and yLoc == (yrange - 2) and countX > (xrange*2):
            print "XP for Completing: " + str(countX)
            return table, True
        elif xLoc >= 1 and yLoc == (yrange - 2) and countX <= (xrange*2):
            break
    return table, False


def generateCreatures(mapLevel):
    class creature(object):
        def __init__(self,name,lvlHandicap,strength,ability):
            self.name = name
            self.lvlHandicap = lvlHandicap
            self.strength = strength
            self.ability = ability

    mummy = creature('Mummy',-1,5,'None')
    skeleton = creature('Skeleton',-2,4,'None')
    witch = creature('Witch',2,7,'Poison')
    whitedragon = creature('White Dragon',5,12,'Fire')
    orc = creature('Orc',1,9,'None')
    rattlesnake = creature('Rattlesnake',-3,3,'Poison')
    hobogoblin = creature('Hobogoblin',0,8,'None')
    thief = creature('Thief',1,7,'Steal')
    giant = creature('Giant',-1,10,'None')
    spider = creature('Spider',0,6,'Poison')
    kobold = creature('Kobold',1,7,'None')
    bat = creature('Bat',-3,3,'None')
    theCreatures = [bat, kobold, spider, giant, thief, hobogoblin, rattlesnake, orc, whitedragon, witch, skeleton, mummy]
    jackal = creature('Jackal',1,5,'None')
    hyena = creature('Hyena',0,4,'None')
    lizardman = creature('Lizardman',1,9,'None')
    vulture = creature('Vulture',0,7,'None')
    goblin = creature('Goblin',1,7,'None')
    zombie = creature('Zombie',-1,5,'None')
    cockatrice = creature('Cockatrice',1,8,'Poison')
    thug = creature('Thug',0,6,'None')
    ghoul = creature('Ghoul',1, 7, 'None')
    ogre = creature('Ogre',0,9,'None')
    berserker = creature('Berserker',-2,5,'None')
    druid = creature('Druid',3,7,'Slowness')
    gargoyle = creature('Gargoyle',2,6,'None')
    werewolf = creature('Werewolf',3,4,'None')
    theCreatures += [werewolf, gargoyle, druid, berserker, ogre, ghoul, thug, cockatrice, zombie, goblin, vulture, lizardman, hyena, jackal]
    banshee = creature('Banshee',-2,6,'Invisibility')
    ghost = creature('Ghost',-1,5,'Invisibility')
    cyclops = creature('Cyclops',2,8,'None')
    drider = creature('Drider',-3,6,'None')
    medusa = creature('Medusa',2,5,'Slowness')
    reddragon = creature('Red Dragon', 4, 10, 'None')
    dungeonGuardian = creature('Dungeon Guardian', 3, 11, 'None')
    stormGiant = creature('Storm Giant', 1, 8, 'None')
    orog = creature('Orog', -1, 5, 'None')
    assasin = creature('Assassin', 1,10, 'None')
    spy = creature('Spy',-2,4,'None')
    hydra = creature('Hydra',2,7,'None')
    frostGiant = creature('Frost Giant', 0,7,'Slowness')
    vampire = creature('Vampire',-1,6,'None')
    golem = creature('Golem', -2,5,'None')
    theCreatures += [banshee, ghost, cyclops, drider, medusa, reddragon, dungeonGuardian, stormGiant, orog, assasin, spy, hydra, frostGiant, vampire, golem]
    baboom = creature('Baboom', -3, 3, 'None')
    badger = creature('Badger', -1, 4, 'None')
    lizardking = creature('Lizard King',3,8,'None')
    octopus = creature('Octopus',0,7,'None')
    raven = creature('Raven',-3,4,'None')
    scorpion = creature('Scorpion', -1, 2, 'Poison')
    weasel = creature('Weasel', 1,5,'None')
    bandit = creature('Bandit', 1, 5, 'None')
    banditleader = creature('Bandit Leader', 2, 7, 'None')
    theCreatures += [baboom, badger, lizardking, octopus, raven, scorpion, weasel, bandit, banditleader]
    print "-"*15 + "Creatures of the Dungeon" + "-"*15
    for i in range(3, 19):
        randCreature = random.randint(0, (len(theCreatures)-1))
        #print str(randCreature) + " " + str(len(theCreatures))
        randLevel = random.randint(mapLevel,mapLevel*6)
        calcLevel = theCreatures[randCreature].lvlHandicap + randLevel
        calcLevel = (calcLevel / 5) + mapLevel
        calcHP = theCreatures[randCreature].strength + randLevel
        calcHP = (calcHP * random.randint(1,(2+mapLevel))) + 13
        if theCreatures[randCreature].ability == 'None':
            print '{0:2}'.format(str(i)) + " - " + '{0:16}'.format(theCreatures[randCreature].name) + " Level:" + '{0:2}'.format(str(calcLevel)) + "   HP:" + '{0:3}'.format(str(calcHP))
        else:
            print '{0:2}'.format(str(i)) + " - " + '{0:16}'.format(theCreatures[randCreature].name) + " Level:" + '{0:2}'.format(str(calcLevel)) + "   HP:" + '{0:3}'.format(str(calcHP)) + "   Ability: " + theCreatures[randCreature].ability


def displayAttackRules():
    print
    print "-"*15 + "Attack or Defend" + "-"*15
    print "Attack 2 die 6 + if Fighter +" + str(random.randint(1,3)) + " + Weapon Bonus"
    print "[Note: If attacked by creature ability is applied if " + str(random.randint(2,12)) + " is rolled with 2 die 6]"
    print
    print "Defend (2 die 6) * 2 + if Mage +" + str(random.randint(1, 3)) + " + Armor Bonus"
    print "[Note: Creatures are unable to defend attacks]"
    print

def displayCamporMove():
    print
    print "Determine if you are Attacked by Rolling 2 die 6"
    print "While Camping: " + str(random.randint(2,12))
    listN = []
    while (len(listN)<3):
        listN = []
        for i in range(0,3):
            randN = random.randint(2,12)
            if randN not in listN:
                listN.append(randN)
    listN.sort()
    print "Arriving at next Destination: " + str(listN[0]) + " " + str(listN[1]) + " " + str(listN[2])

def main():
    response = 'y'
    while response == 'y':
        level = raw_input("Level of Map [1-10]: ")
        level = int(level)
        x = 20 + (level*2)
        y = 20 + (level*2)
        goodTable = False
        print
        print
        print "Dungeon - Level: " + str(level)
        while goodTable == False:
            mazeTable = createMaze(x,y)
            mazeTable, goodTable = generatePath(mazeTable,x,y,level)
        displayMaze(mazeTable, x, y)
        displayCamporMove()
        displayAttackRules()
        generateCreatures(level)
        print
        response = raw_input("Generate another map? (y/n) ")
        if response == 'N' or response == 'n':
            response == 'n'
        print
        print



if __name__ == '__main__':
    main()