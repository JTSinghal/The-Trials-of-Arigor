
class Alexander(object):
	def __init__(self):
		self.gold = 0
		self.health = self.level * 1000
		self.mana = 100
		self.level = 1	#levels up with every quest
		self.inventory = []
		self.attacks = {}	#when he learns an attack, it is appended here
		self.positionX = None
		self.positionY = None

	def attack(self, attackName, enemyIdentifier):	#if user asks for an attack that isn't in the attacks, comp says no
		for attack in self.attacks:
			if (attackName == attack):
				enemyIdentifier.health -= self.attacks[attack]

	def die():
		#restart at last checkpoint with the items you had then

	def pickUp(pickup):	#picks up an array, program loops through array and appends the items to inventory
		for items in pickup:
			inventory.append(items)

	def move(direction):


class Enemy(object):
	def __init__(self, species, level, gold, items):	#items is an array, can be empty. Gold is amount
		self.species = species
		self.level = level   #defines strength of attack
		self.health = level * 100
		self.gold = gold
		self.items = items

	def attack(self, AlexanderIdentifier):	#each species has its own attacks, the attacks it deals are random	#could have conditional, if health != 0, continue attacking, then stop after health <= 0, won't need die()
		while(self.health != 0 and AlexanderIdentifier.health != 0):
			AlexanderIdentifier.health -= self.level * 10 #subject to change

	def die():	#dies and does not attack, basically removes instance of object
		drop()
		#delete instance of object from the monster array in the location it resides
		#delete instance of object

	def drop(self, AlexanderIdentifier, pickup):
		AlexanderIdentifier.gold += self.gold
		for items in self.items:
			pickup.append(items)

class Friend(object):	#These are npcs in the game that can help you or give you stuff
	def __init__(self, species, health, gold, items, advice):
		self.species = species
		self.health = health
		self.gold = gold
		self.items = items
		self.advice = advice  #advice given to alexander when he asks for help

	def die():
		drop()
		#delete instance of object from the people array in the location it resides
		#delete instance of object from the game

	def drop(self, AlexanderIdentifier, pickup):
		AlexanderIdentifier.gold += self.gold
		for items in self.items:
			pickup.append(items)

class Place(object):	#gives a template to make a place and add things to it
	def __init__(self, name, people, creatures, treasures, houses):	#every variable is an array excpt name and treasure
		self.name = name
		self.people = people
		self.creatures = creatures
		self.treasures = treasures
		self.houses = houses

class chest(object):
	def __init__(self, amount, answer):	#the puzzle is a RANDOM number thing and you need to solve it
		self.amount = amount
		self.answer = answer	#in the paras, answer is given by naming the function

	def open(codeNumber):	#if codeNumber equals the answer, it gives Alex the money

###########################################################################################################
