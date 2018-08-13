from class_definitions import *


#################################### Define Map ####################################################
ARIGOR = []

for x in range(0, 4):
	for y in range(0, 4):
		rowMaker = []
		rowMaker.append(None)
	ARIGOR.append(rowMaker)
	rowMaker = []

################################### Define Enemy Classes #############################################

Goblin = Enemy("Goblin", 1, 100, [])
Goblin.items = []

Unicorn = Enemy("Unicorn", 1, 100, [])
Unicorn.items = []

Vampire = Enemy("Vampire", 1, 100, [])
Vampire.items = []

Wizard = Enemy("Wizard", 1, 100, [])
Wizard.items = []

Centaur = Enemy("Centaur", 1, 100, [])
Centaur.items = []

Cyclops = Enemy("Cyclops", 1, 100, [])
Cyclops.items = []

Siren = Enemy("Siren", 1, 100, [])
Siren.items = []

Phoenix = Enemy("Phoenix", 1, 100, [])
Phoenix.items = []

Elf = Enemy("Elf", 1, 100, [])
Elf.items = []

Dragon = Enemy("Dragon", 1, 100, [])
Dragon.items = []

Amazonian = Enemy("Amazonian", 1, 100, [])
Amazonian.items = []

#################################### Define Locations ################################################
GoblinsLair = Place("Goblin's Lair", [], [], [], [])
GoblinsLair.people = []
GoblinsLair.creatures = []
GoblinsLair.treasures = 1
GoblinsLair.houses = []

UnicornIsland = Place("Unicorn Island", [], [], [], [])
UnicornIsland.people = []
UnicornIsland.creatures = []
UnicornIsland.treasures = 1
UnicornIsland.houses = []

VampireMansion = Place("Vampire Mansion", [], [], [], [])
VampireMansion.people = []
VampireMansion.creatures = []
VampireMansion.treasures = 1
VampireMansion.houses = []

WizardTower = Place("Wizard's Tower", [], [], [], [])
WizardTower.people = []
WizardTower.creatures = []
WizardTower.treasures = 1
WizardTower.houses = []

CentaurField = Place("Centaur Field", [], [], [], [])
CentaurField.people = []
CentaurField.creatures = []
CentaurField.treasures = 1
CentaurField.houses = []

Palace = Place("Palace", [], [], [], [])
Palace.people = []
Palace.creatures = []
Palace.treasures = 1
Palace.houses = []

CyclopDen = Place("Cyclop's Den", [], [], [], [])
CyclopDen.people = []
CyclopDen.creatures = []
CyclopDen.treasures = 1
CyclopDen.houses = []

SirenLake = Place("Siren Lake", [], [], [], [])
SirenLake.people = []
SirenLake.creatures = []
SirenLake.treasures = 1
SirenLake.houses = []

HOME = Place("HOME", [], [], [], [])
HOME.people = []
HOME.creatures = []
HOME.treasures = 1
HOME.houses = []

MARKET = Place("MARKET", [], [], [], [])
MARKET.people = []
MARKET.creatures = []
MARKET.treasures = 1
MARKET.houses = []

PhoenixField = Place("Phoenix Field", [], [], [], [])
PhoenixField.people = []
PhoenixField.creatures = []
PhoenixField.treasures = 1
PhoenixField.houses = []

ElvishKingdom = Place("Elvish Kingdom", [], [], [], [])
ElvishKingdom.people = []
ElvishKingdom.creatures = []
ElvishKingdom.treasures = 1
ElvishKingdom.houses = []

DragonLair = Place("Dragon's Lair", [], [], [], [])
DragonLair.people = []
DragonLair.creatures = []
DragonLair.treasures = 1
DragonLair.houses = []

AmazonianKingdom = Place("Amazonian Kingdom", [], [], [], [])
AmazonianKingdom.people = []
AmazonianKingdom.creatures = []
AmazonianKingdom.treasures = 1
AmazonianKingdom.houses = []

PuzzleRoom = Place("Puzzle Room", [], [], [], [])
PuzzleRoom.people = []
PuzzleRoom.creatures = []
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
def updateScreenText():
Alexander = Alexander()

### Introductory

### Main Game Loop
user_input = None

while (user_input.lower() != "exit game"):
	if user_input[0] == "go":
		if user_input[1] == "north" and 