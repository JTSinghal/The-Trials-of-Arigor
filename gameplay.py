from class_definitions import *
import random


#################################### Define Map ####################################################
ARIGOR = []

for x in range(0, 4):
	for y in range(0, 4):
		rowMaker = []
		rowMaker.append(None)
	ARIGOR.append(rowMaker)
	rowMaker = []

#################################### Items Array Generator ##########################################

def itemsGenerator(numItems, itemsToChooseFrom):
	returnedArray = []
	for x in range(0, numItems):
		returnedArray.append(random.choice(itemsToChooseFrom))

	return returnedArray

#################################### Define Locations ################################################
GoblinsLair = Place("Goblin's Lair", [], [], [])
GoblinsLair.people = [npc("Goblin King", "", ""), npc("Goblin Prisoner", "", ""), npc("Tavern Owner", "", ""), npc("leather-worker", "", "")]	#goblin king, goblin's prisoner
for x in range (0, random.randint(10, 15)):
	GoblinsLair.creatures.append(Enemy("Goblin", 1, itemsGenerator(2, ["Goblin's Hide", "Goblin Armor", "Goblin Sword", "Goblin Shield", "Goblin Bones"]), False))
GoblinsLair.treasures = 1

UnicornIsland = Place("Unicorn Island", [], [], [])
UnicornIsland.people = [npc("Unicorn Leader", "", ""), npc("Spiritual Unicorn", "", ""), npc("Unicorn Student", "", ""), npc("Horn-master", "", "")] #Unicorn Leader, 
for x in range (0, random.randint(3, 7)):
	UnicornIsland.creatures.append(Enemy("Unicorn", 7, itemsGenerator(2, ["Unicorn Blood", "Unicorn Horn", "Unicorn Hair", "Rainbow", "Hooves", "Unicorn Bones"]), True))
UnicornIsland.treasures = 1

VampireMansion = Place("Vampire Mansion", [], [], [])
VampireMansion.people = [npc("Count Dracula", "", ""), npc("homeowner", "", ""), npc("Vampire Bats", "", "")]
for x in range (0, random.randint(8, 13)):
	VampireMansion.creatures.append(Enemy("Vampire", 3, itemsGenerator(2, ["Vampire Fangs", "Vampire Cape", "Necklace", "Vampire Heart", "Vampire Bones"]), False))
VampireMansion.treasures = 1

WizardTower = Place("Wizard's Tower", [], [], [])
WizardTower.people = [npc("Gwydion", "", ""),npc( "Apprentice", "", ""), npc("Wizard Janitor", "", "")]
for x in range (0, 4):
	WizardTower.creatures.append(Enemy("Wizard", 10, itemsGenerator(2, ["Wand", "Staff", "Wizard Robes", "Divinity Orb", "Wizard Bones"]), True))
WizardTower.treasures = 1

CentaurField = Place("Centaur Field", [], [], [])
CentaurField.people = [npc("Centuar Leader", "", ""), npc("Centaur Wife", "", ""), npc("Guards", "", ""), npc("Centaur Trainer", "", "")]
for x in range (0, random.randint(5, 10)):
	CentaurField.creatures.append(Enemy("Centaur", 3, itemsGenerator(2, ["Centaur Hide", "Hooves", "Centaur Hair", "Centaur Blood", "Honor", "Centaur Bones"]), True))
CentaurField.treasures = 2

Palace = Place("Palace", [], [], [])
Palace.people = [npc("King Phillip", "", ""), npc("Princess Elizabeth", "", ""), npc("Royal Guard", "", ""), npc("Knight", "", "")]
Palace.treasures = 1

ArigorTown = Place("Arigor", [], [], [])
Palace.people = [npc("Gardener", "", ""), npc("Farmer", "", ""), npc("Maiden in Despair", "", "")]
Palace.treasures = 1

CyclopsDen = Place("Cyclops' Den", [], [], [])
CyclopsDen.people = [npc("Cyclops Leader", "", ""), npc("Meathead", "", ""), npc("Cyclops' Dinner", "", "")]
for x in range (0, random.randint(5, 10)):
	CyclopsDen.creatures.append(Enemy("Cyclops", 7, itemsGenerator(2, ["Cyclops Eyeball", "Cyclops Club", "Cyclops Lioncloth", "Rock", "Cyclops Bones"]), False))
CyclopsDen.treasures = 1

SirenLake = Place("Siren Lake", [], [], [])
SirenLake.people = [npc("Siren Queen", "", ""), npc("Ariel the Mermaid", "", ""), npc("The Oracle", "", "")]
for x in range (0, random.randint(5, 10)):
	SirenLake.creatures.append(Enemy("Siren", 6, itemsGenerator(1, ["Siren Scales", "Siren's Song", "Siren Teeth", "Siren Bones"]), False))
SirenLake.treasures = 1

HOME = Place("HOME", [], [], [])
HOME.people = []
HOME.treasures = 1

MARKET = Place("MARKET", [], [], [])
MARKET.people = []
MARKET.treasures = 1

PhoenixField = Place("Phoenix Field", [], [], [])
PhoenixField.people = [npc("Alonso the Swift", "", ""), npc("Feather Keeper", "", ""), npc("Phoenix Runt", "", "")]
for x in range (0, random.randint(5, 10)):
	PhoenixField.creatures.append(Enemy("Phoenix", 9, itemsGenerator(2, ["Phoenix Feather", "Phoenix Ashes", "Phoenix Talons", "Eternal Flame", "Phoenix Bones"]), True))
PhoenixField.treasures = 1

ElvishKingdom = Place("Elvish Kingdom", [], [], [])
ElvishKingdom.people = [npc("Elvish King", "", ""), npc("Elvish Queen", "", ""), npc("Elvish Knight", "", ""), npc("Elvish Apprentice", "", "")]
for x in range (0, random.randint(5, 10)):
	ElvishKingdom.creatures.append(Enemy("Elf", 12, itemsGenerator(2, ["Elf's Hide", "Elf Armor", "Elf Blood", "Elf Shield", "Elf Bones"]), True))
ElvishKingdom.treasures = 1

DragonLair = Place("Dragon's Lair", [], [], [])
DragonLair.people = [npc("Dragon King", "", "")]
for x in range (0, 2):
	DragonLair.creatures.append(Enemy("Dragon", 15, itemsGenerator(2, ["Dragon's Hide", "Dragon Scales", "Dragon Wings", "Eternal Flame", "Dragon Bones"]), False))
DragonLair.treasures = 1

AmazonianKingdom = Place("Amazonian Kingdom", [], [], [])
AmazonianKingdom.people = [npc("Amazonian Queen", "", ""), npc("Amazonian Guard", "", ""), npc("Strategist", "", "")]
for x in range (0, random.randint(5, 10)):
	AmazonianKingdom.creatures.append(Enemy("Amazonian", 8, itemsGenerator(2, ["Amazonian Armor", "Amazonian Sword", "Amazonian Sword", "Amazonian Shield", "Amazonian Bones"]), True))
AmazonianKingdom.treasures = 1

PuzzleRoom = Place("Puzzle Room", [], [], [])
PuzzleRoom.people = []
PuzzleRoom.treasures = 1

ARIGOR[0][0] = GoblinsLair
ARIGOR[0][1] = UnicornIsland
ARIGOR[0][2] = VampireMansion
ARIGOR[0][3] = WizardTower
ARIGOR[1][0] = CentaurField
ARIGOR[1][1] = Palace
ARIGOR[1][2] = ArigorTown
ARIGOR[1][3] = CyclopsDen
ARIGOR[2][0] = SirenLake
ARIGOR[2][1] = HOME
ARIGOR[2][2] = MARKET
ARIGOR[2][3] = PhoenixField
ARIGOR[3][0] = ElvishKingdom
ARIGOR[3][1] = DragonLair
ARIGOR[3][2] = AmazonianKingdom
ARIGOR[3][3] = PuzzleRoom	#keeps getting new puzzles for you to solve, for extra prizes, after each quest you finish

####################################### Main methods ##################################################

pickup = []   #will be emptied every 3 minutes all drops go in here

def describe_newGame():
	raw_input("You open your eyes.\n\n")
	raw_input("Me:\"I must have fallen asleep. Oh no! What time is it?? I need to meet with the King!\"")
	raw_input("You scramble to get out of bed and find your cloak. You hear hurried footsteps in the hallway near your door and see a familiar face. You feel a blush around your cheeks.\n")
	raw_input("\"Alex? Alexander!\n\"")
	raw_input("\nBefore you stands the fairest maiden that ever did rome the land, Princess Katherine, only child of the King, and heir to the kingdom. She entered the room with her characteristic warmth and contagious smile. Anyone else would be able to see the blush on her face seeing a half-asleep Alexander. Unfortunatley, Alexander aren't as perceptive when it came to matters of the heart.\n\n")
	raw_input("Me: \"Ah Princess! Apologies, I am not fully dressed, and I beleive I woke up late. But, it sure is nice to wake up to you- I mean to see you this early- I mean...umm\"\n")
	raw_input("\nYour blush grows deeper...along with hers.\n\n")
	raw_input("Princess Katherine: \"Alex, how many times do I need to tell you? You shall call me Kat and nothing more. Anyways, father is looking for you, you were supposed to meet with him 20 minutes ago, you know how impatient he gets.\"\n")
	raw_input("Me: \"Yes, sorry, Kat, I'll be right out, I just need to find my cloak.\"\n")
	raw_input("You find your cloak stuffed between two pillows, and make your way from your quarters to the main chamber of the Palace.\n\nThe main chamber is unusually busy this morning. King Phillip is sitting on his throne, surrouned by several ministers, a stern look on his face. You kneel before him.\n\n")
	raw_input("Me: \"Apologies for my tardiness your majesty. It won't happen again. Why did you ask for my presence this morning?\"")
	raw_input("King Phillip: \"Ah Alexander. Stand up, son, no need to worry, as long as you can take care of a task for me.\"\n")
	raw_input("Me: \"A task, sir? What kind of task is this?\"\n")
	raw_input("King Phillip: \"This task is of the utmost importance, Alex. About a week ago, the peace between the Elves and the Amazonians was broken.\"\n")
	raw_input("\nYou gasp. Decades ago, there had been a bitter hatred between the Elves and the Amazonians. Their 50-year war caused famines across the land, economic hardships, and power struggles between every clan, not to mention the hundreds of thousands of deaths. King Phillip had brokered a truce between the two clans, marking a turning point in the history of Arigor. Clans were now more involved with each other, working to help others rather than exclusively their own tribe. A break in the peace could threaten everything that the kingdom had worked so hard to build.\n\n")
	raw_input("King Phillip: \" That's right. I was only informed two days ago. Apparently an Elvish soldier set fire to 10 acres of Amazonian farmland in one night. The soldier was fittingly banished to the Dark Realm. Although the Amazonians put out the fire, the farmland is unusable and Andromeda, the leader of the Amazonians, is furious. This is why I wanted to meet with you today, I need for you to deliver an important message to Gwydion the Wizard. He will be vital in helping our cause. We need to right this wrong as soon as possible.\"\n")
	raw_input("Me: \"Yes, your majesty, I will do anything I can to help. What is the message you wish to deliver?\"\n")
	raw_input("King Phillip: \"The message is contained in this parcel. Unfortunatley, since you're not a full Knight, I can't reveal it's contents to you. But trust me when I say that you'll be doing the kingdom an enormous favor. Also take this gold for the tolls that you will cross to get to the Wizard Tower\"\n")
	raw_input("Me: \"Yes, sir. I'll be back soon\"\n")
	raw_input("\nA takes the parcel and gold and heads out of the main chamber. It was hard to hide his dissapointment with not being told the contents of the parcel. See, Alex is an orphan. 19 years ago, he was left at the palace doors in the middle of the night. The King took him in and raised him as one of his own. Seeing his potential, the King entered Alex into the Knight apprenticeship program. As such, he is still an apprentice, but so close to knighthood he can almost taste it. He has been one of the Kings closest aide for years, working several hours a day to make sure he is well served. So it still stings when the King wouldn't divulge information that was reserved for Knights. In any case, Alexander is determined to prove himself. Right now all he cares about is delivering the parcel in a timely manner. Gwydion the Wizard is a brilliant man, who played a vital role in helping King Phillip broker the peace the first time around. Alexander always enjoys going to the Wizard Tower to meet with him. They had formed quite a friendship.\n\n\n")
	raw_input("MISSION OBJECTIVE: Take the important parcel to Gwydion the Wizrd and deliver the message from King Phillip.\n\n")
	raw_input("One piece of advice: you can always type \"Help\" if you want to know what you are allowed to do/how to do it.\n\n")

def describe_Location(positionX, positionY):
	if positionX == 0:
		if positionY == 0:
			print "\nGOBLIN'S LAIR: You are situated in the grungiest place on the planet. Green, lazy, slow-moving goblins are roaming the streets going to seedy bars and weapons shops. Every single one of them are carrying around a small sword and basic shield. There are about " + len(GoblinsLair.creatures) + " goblin's giving you mean looks. A few notable members of this community are the Goblin King, the Goblin Prisoner, the tavern owner, and the leather-worker.\n"
		if positionY == 1:
			print "UNIVORN ISLAND: Ah Unicorn Island, the most magical place in the world. You find yourself on the greenest meadow you've ever seen, with a number of white and brown unicorns. The little ones are playing with each other in what seems to be some friendly rough-housing. The adults are either training or taking part in traditional unicorn activities. There are about " + len(UnicornIsland.creatures) + "in coats of armor. Notable members of this community are the Unicorn Leader, the Spiritual Unicorn, the Unicron Student, and the Horn-master.\n"	#"The Unicorn Clan is an ally to the Kingdom. Attacking any of their residents will result in your instant execution by the Unicorn Leader, and a brutal war between your territories. "
		if positionY == 2:
			print "VAMPIRE MANSION: You enter a dark abandoned-looking mansion and feel a sudden chill rush over you. Your every step seems to be monitored. The floor creaks under your foot and a group of bats emerge from the end of a dark hallway and fly right above your head. But you've been here before, you know what to expect. From memory you recall there being " + len(VampireMansion.creatures) + "vampires and you know the location of their coffins...hopefully. Notable members in this house include Count Dracula, the homeowner, and the vampire bats who turn human at any moment.\n"
		if positionY == 3:
			print "WIZARD TOWER: Always good to be here. Gwydion's 'humble' abode. A 200-foot tower leading up to his Office. You know you can skip leg day whenever you come visit."
	if positionX == 1:
		if positionY == 0:
			print "CENTAUR FIELD: "
		if positionY == 1:
			print "PALACE: "
		if positionY == 2:
			print "ARIGOR TOWN: "
		if positionY == 3:
			print "CYCLOPS' DEN: "
	if positionX == 2:
		if positionY == 0:
			print "SIREN LAKE: "
		if positionY == 1:
			print "HOME: "
		if positionY == 2:
			print "MARKET: "
		if positionY == 3:
			print "PHOENIX FIELD: "
	if positionX == 3:
		if positionY == 0:
			print "ELVISH KINGDOM: "
		if positionY == 1:
			print "DRAGON LAIR: "
		if positionY == 2:
			print "AMAZONIAN KINGDOM: "
		if positionY == 3:
			print "PUZZLE ROOM: "
	for npc in (ARIGOR[positionX][positionY]).people:
		print npc.description
	if len(ARIGOR[positionX][positionY].creatures) > 0:
		if ARIGOR[positionX][positionY].creatures[0].friendBool:
			print ARIGOR[positionX][positionY].name + " is an ally to the kingdom. Attacking any of their members will result in your immediate execution by King Phillip and a bitter war between the two territories. Control your bloodlust.\n"


def describe_ThingsYouCanDo(positionX, positionY, level):	#the level you're at determines the quest you're taking on. The things you can do in certain locations changes if you're taking on a quest involving that location
def describe_BattleScene():
def describe_Pickup()
def describe_Quest()
def describe_Marketplace(stage) #stage 1 is just displaying prices, stage 2 is confirming that alex wants to sell
def describe_


def changeAttributes_levelChange(level):	#changes attributes of alex and some other people when he reaches a new level. For example changes the dialog he speakes with the princess
	elif level == 2:
	elif level == 3:
	elif level == 4:
	elif level == 5:
	elif level == 6:
	elif level == 7:
	elif level == 8:
	elif level == 9:
	elif level == 10:



Alexander = Alexander()
Alexander.positionX = 1
Alexander.positionY = 2
describe_newGame()
describe_Location(Alexander.positionX, Alexander.positionY)

### Introductory

### Main Game Loop
describe_Location(Alexander.positionX, Alexander.positionY)
user_input = raw_input("What would you like to do? :\n")
user_input_split = user_input.lower().split()

while (user_input.lower() != "exit game"):
	user_input_split = user_input.lower().split()
	if user_input_split[0] == "go":

		if user_input_split[1] == "north":
			if Alexander.positionY == 0:
				print "There seems to be a cliff in this direction that you can't cross. Drat.\n"
			else:
				Alexander.positionY -= 1
		elif user_input_split[1] == "east":
			if Alexander.positionX == 3:
				print "There seems to be a cliff in this direction that you can't cross. Drat.\n"
			else:
				Alexander.positionX += 1
		elif user_input_split[1] == "south":
			if Alexander.positionY == 3:
				print "There seems to be a cliff in this direction that you can't cross. Drat.\n"
			else:
				Alexander.positionY += 1
		elif user_input_split[1] == "west":	
			if Alexander.positionX == 0:
				print "There seems to be a cliff in this direction that you can't cross. Drat.\n"
			else:
				Alexander.positionX -= 1
		else:
			print "Invalid request, you may only specify if you would like to GO: NORTH, SOUTH, EAST, or WEST\n"

		describe_Location(Alexander.positionX, Alexander.positionY)
		describe_ThingsYouCanDo(Alexander.positionX, Alexander.positionY)

	elif user_input_split[0] == "attack":	#TODO

		if user_input_split[1] != (ARIGOR[Alexander.positionX][Alexander.positionY]).creatures[0].species.lower():
			print "There are no " + user_input_split[1] + "s here.\n"
		elif user_input_split[2] < 0 or user_input_split[2] > len((ARIGOR[Alexander.positionX][Alexander.positionY]).creatures):
			print "Cannot attack " + user_input_split[1] + user_input_split[2] + ". There are only " + len((ARIGOR[Alexander.positionX][Alexander.positionY]).creatures) + user_input_split[1] + "s. If you would like to attack, please choose a number between 0 and " + len((ARIGOR[Alexander.positionX][Alexander.positionY]).creatures) + ".\n"
		else:

	elif user_input_split[0] + user_input_split[1] == "talk to":

		i = 0
		while((ARIGOR[Alexander.positionX][Alexander.positionY]).people[i] != user_input_split[2]):
			i++
		if (i >= len((ARIGOR[Alexander.positionX][Alexander.positionY]).people)):
			print "Please enter a valid person you would like to talk to, who is in your immediate surroundings.\n"
		else:
			print (ARIGOR[Alexander.positionX][Alexander.positionY]).people[i].dialogue

	elif user_input.lower() == "view map":


	else:
		print "Please enter a valid command.\n"

	describe_Location(Alexander.positionX, Alexander.positionY)
	user_input = raw_input("\nWhat would you like to do?\n")