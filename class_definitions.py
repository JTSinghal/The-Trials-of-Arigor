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
###########################################################################################################