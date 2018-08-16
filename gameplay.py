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
GoblinsLair = Place("Goblin's Lair", [], [], [], [])
GoblinsLair.people = []	#goblin king, goblin's prisoner
for x in range (0, random.randint(10, 15)):
	GoblinsLair.creatures.append(Enemy("Goblin", 1, itemsGenerator(2, ["Goblin's Hide", "Goblin Armor", "Goblin Sword", "Goblin Shield", "Goblin Bones"])))
GoblinsLair.treasures = 1
GoblinsLair.houses = []

UnicornIsland = Place("Unicorn Island", [], [], [], [])
UnicornIsland.people = [] #Unicorn Leader, 
for x in range (0, random.randint(3, 7)):
	UnicornIsland.creatures.append(Enemy("Unicorn", 7, itemsGenerator(2, ["Unicorn Blood", "Unicorn Horn", "Unicorn Hair", "Rainbow", "Hooves", "Unicorn Bones"])))
UnicornIsland.treasures = 1
UnicornIsland.houses = []

VampireMansion = Place("Vampire Mansion", [], [], [], [])
VampireMansion.people = []
for x in range (0, random.randint(8, 13)):
	VampireMansion.creatures.append(Enemy("Vampire", 3, itemsGenerator(2, ["Vampire Fangs", "Vampire Cape", "Necklace", "Vampire Heart", "Vampire Bones"])))
VampireMansion.treasures = 1
VampireMansion.houses = []

WizardTower = Place("Wizard's Tower", [], [], [], [])
WizardTower.people = []
for x in range (0, 4):
	WizardTower.creatures.append(Enemy("Wizard", 10, itemsGenerator(2, ["Wand", "Staff", "Wizard Robes", "Divinity Orb", "Wizard Bones"])))
WizardTower.treasures = 1
WizardTower.houses = []

CentaurField = Place("Centaur Field", [], [], [], [])
CentaurField.people = []
for x in range (0, random.randint(5, 10)):
	CentaurField.creatures.append(Enemy("Centaur", 3, itemsGenerator(2, ["Centaur Hide", "Hooves", "Centaur Hair", "Centaur Blood", "Honor", "Centaur Bones"])))
CentaurField.treasures = 2
CentaurField.houses = []

Palace = Place("Palace", [], [], [], [])
Palace.people = []
Palace.treasures = 1
Palace.houses = []

CyclopDen = Place("Cyclop's Den", [], [], [], [])
CyclopDen.people = []
for x in range (0, random.randint(5, 10)):
	CyclopDen.creatures.append(Enemy("Cyclops", 7, itemsGenerator(2, ["Cyclops Eyeball", "Cyclops Club", "Cyclops Lioncloth", "Rock", "Cyclops Bones"])))
CyclopDen.treasures = 1
CyclopDen.houses = []

SirenLake = Place("Siren Lake", [], [], [], [])
SirenLake.people = []
for x in range (0, random.randint(5, 10)):
	SirenLake.creatures.append(Enemy("Siren", 6, itemsGenerator(1, ["Siren Scales", "Siren's Song", "Siren Teeth", "Siren Bones"])))
SirenLake.treasures = 1
SirenLake.houses = []

HOME = Place("HOME", [], [], [], [])
HOME.people = []
HOME.treasures = 1
HOME.houses = []

MARKET = Place("MARKET", [], [], [], [])
MARKET.people = []
MARKET.treasures = 1
MARKET.houses = []

PhoenixField = Place("Phoenix Field", [], [], [], [])
PhoenixField.people = []
for x in range (0, random.randint(5, 10)):
	PhoenixField.creatures.append(Enemy("Phoenix", 9, itemsGenerator(2, ["Phoenix Feather", "Phoenix Ashes", "Phoenix Talons", "Eternal Flame", "Phoenix Bones"])))
PhoenixField.treasures = 1
PhoenixField.houses = []

ElvishKingdom = Place("Elvish Kingdom", [], [], [], [])
ElvishKingdom.people = []
for x in range (0, random.randint(5, 10)):
	ElvishKingdom.creatures.append(Enemy("Elf", 12, itemsGenerator(2, ["Elf's Hide", "Elf Armor", "Elf Blood", "Elf Shield", "Elf Bones"])))
ElvishKingdom.treasures = 1
ElvishKingdom.houses = []

DragonLair = Place("Dragon's Lair", [], [], [], [])
DragonLair.people = []
for x in range (0, 2):
	DragonLair.creatures.append(Enemy("Dragon", 15, itemsGenerator(2, ["Dragon's Hide", "Dragon Scales", "Dragon Wings", "Eternal Flame", "Dragon Bones"])))
DragonLair.treasures = 1
DragonLair.houses = []

AmazonianKingdom = Place("Amazonian Kingdom", [], [], [], [])
AmazonianKingdom.people = []
for x in range (0, random.randint(5, 10)):
	AmazonianKingdom.creatures.append(Enemy("Amazonian", 8, itemsGenerator(2, ["Amazonian Armor", "Amazonian Sword", "Amazonian Sword", "Amazonian Shield", "Amazonian Bones"])))
AmazonianKingdom.treasures = 1
AmazonianKingdom.houses = []

PuzzleRoom = Place("Puzzle Room", [], [], [], [])
PuzzleRoom.people = []
PuzzleRoom.treasures = 1
PuzzleRoom.houses = []

ARIGOR[0][0] = GoblinsLair
ARIGOR[0][1] = UnicornIsland
ARIGOR[0][2] = VampireMansion
ARIGOR[0][3] = WizardTower
ARIGOR[1][0] = CentaurField
ARIGOR[1][1] = Palace
ARIGOR[1][2] = ARIGOR[1][1]
ARIGOR[1][3] = CyclopDen
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

def describe_Location(positionX, positionY):
def describe_ThingsYouCanDo(positionX, positionY):
def describe_BattleScene():
def describe_Pickup()
def describe_Quest()
def describe_Marketplace(stage) #stage 1 is just displaying prices, stage 2 is confirming that alex wants to sell
def describe_


def changeAttributes_levelChange(level):	#changes attributes of alex and some other people when he reaches a new level. For example changes the dialog he speakes with the princess
	if level == 2:
	elif level == 3:
	elif level == 4:
	elif level == 5:
	elif level == 6:
	elif level == 7:
	elif level == 8:
	elif level == 9:
	elif level == 10:



Alexander = Alexander()

### Introductory

### Main Game Loop
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

	elif user_input_split[0] == ""

	else:
		print "Please enter a valid command.\n"

	user_input = raw_input("What would you like to do?\n")