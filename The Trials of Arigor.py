ARIGOR = []

for x in range(0, 4):
	for y in range(0, 4):
		rowMaker = []
		rowMaker.append(None)
	ARIGOR.append(rowMaker)
	rowMaker = []

##########################################################################################################
class Alexander(object):
	def __init__(self):
		self.gold = 0
		self.health = 1000
		self.mana = 100
		self.level = 0	#levels up with every quest
		self.inventory = []
		self.attacks = []	#when he learns an attack, it is appended here
		self.position = None	#tells where you are at the time in the form of ARIGOR[x][y]

	def attack(attackName):	#if user asks for an attack that isn't in the attacks, comp says no

	def pickUp(items):	#picks up an array, program loops through array and appends the items to inventory

	def move(direction):
		

class Enemy(object):
	def __init__(self, species, health, gold, items):	#items is an array, can be empty. Gold is amount
		self.species = species
		self.health = health
		self.gold = gold
		self.items = items
	
	def attack():	#each species has its own attacks, the attacks it deals are random	#could have conditional, if health != 0, continue attacking, then stop after health <= 0, won't need die()
		
	def die():	#dies and does not attack, basically removes instance of object

	def drop():	#is invoked when enemy dies

class Friend(object):	#These are npcs in the game that can help you or give you stuff
	def __init__(self, species, health, gold, items):
		self.species = species
		self.health = health
		self.gold = gold
		self.items = items

	def heal():

	def die():

	def drop():

class Place(object):	#gives a template to make a place and add things to it
	def __init__(self, name, people, creatures, treasures, houses):	#every variable is an array excpt name and treasure
		self.people = people
		self.creatures = creatures
		self.treasures = treasures
		self.houses = houses

class chest(object):
	def __init__(self, amount, answer):	#the puzzle is a RANDOM number thing and you need to solve it
		self.amount = amount
		self.answer = answer	#in the paras, answer is given by naming the function

	def open(codeNumber):	#if codeNumber equals the answer, it gives Alex the money
			

def codeMaker():	#takes random number b/w 0 and 3, and makes a puzzle out of it
	print "Complete the sequence: "
	return answer

######################################################################################################
GoblinsLair = Place("Goblin's Lair", [], [], [], [])
GoblinsLair.self.people = []
GoblinsLair.self.creatures = []
GoblinsLair.self.treasures = 1
GoblinsLair.self.houses = []

UnicornIsland = Place("Unicorn Island", [], [], [], [])
UnicornIsland.self.people = []
UnicornIsland.self.creatures = []
UnicornIsland.self.treasures = 1
UnicornIsland.self.houses = []

VampireMansion = Place("Vampire Mansion", [], [], [], [])
VampireMansion.self.people = []
VampireMansion.self.creatures = []
VampireMansion.self.treasures = 1
VampireMansion.self.houses = []

WizardTower = Place("Wizard's Tower", [], [], [], [])
WizardTower.self.people = []
WizardTower.self.creatures = []
WizardTower.self.treasures = 1
WizardTower.self.houses = []

CentaurField = Place("Centaur Field", [], [], [], [])
CentaurField.self.people = []
CentaurField.self.creatures = []
CentaurField.self.treasures = 1
CentaurField.self.houses = []

Palace = Place("Palace", [], [], [], [])
Palace.self.people = []
Palace.self.creatures = []
Palace.self.treasures = 1
Palace.self.houses = []

CyclopDen = Place("Cyclop's Den", [], [], [], [])
CyclopDen.self.people = []
CyclopDen.self.creatures = []
CyclopDen.self.treasures = 1
CyclopDen.self.houses = []

SirenLake = Place("Siren Lake", [], [], [], [])
SirenLake.self.people = []
SirenLake.self.creatures = []
SirenLake.self.treasures = 1
SirenLake.self.houses = []

HOME = Place("HOME", [], [], [], [])
HOME.self.people = []
HOME.self.creatures = []
HOME.self.treasures = 1
HOME.self.houses = []

MARKET = Place("MARKET", [], [], [], [])
MARKET.self.people = []
MARKET.self.creatures = []
MARKET.self.treasures = 1
MARKET.self.houses = []

PhoenixField = Place("Phoenix Field", [], [], [], [])
PhoenixField.self.people = []
PhoenixField.self.creatures = []
PhoenixField.self.treasures = 1
PhoenixField.self.houses = []

ElvishKingdom = Place("Elvish Kingdom", [], [], [], [])
ElvishKingdom.self.people = []
ElvishKingdom.self.creatures = []
ElvishKingdom.self.treasures = 1
ElvishKingdom.self.houses = []

DragonLair = Place("Dragon's Lair", [], [], [], [])
DragonLair.self.people = []
DragonLair.self.creatures = []
DragonLair.self.treasures = 1
DragonLair.self.houses = []

AmazonianKingdom = Place("Amazonian Kingdom", [], [], [], [])
AmazonianKingdom.self.people = []
AmazonianKingdom.self.creatures = []
AmazonianKingdom.self.treasures = 1
AmazonianKingdom.self.houses = []

PuzzleRoom = Place("Puzzle Room", [], [], [], [])
PuzzleRoom.self.people = []
PuzzleRoom.self.creatures = []
PuzzleRoom.self.treasures = 1
PuzzleRoom.self.houses = []

######################################################################################################
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
######################################################################################################


