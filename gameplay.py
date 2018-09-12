from class_definitions import *
import random
from time import sleep


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

EmptyField = Place("Empty Field", [], [], [])
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
ARIGOR[2][1] = EmptyField
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
			print "UNICORN ISLAND: Ah Unicorn Island, the most magical place in the world. You find yourself on the greenest meadow you've ever seen, with a number of white and brown unicorns. The little ones are playing with each other in what seems to be some friendly rough-housing. The adults are either training or taking part in traditional unicorn activities. There are about " + len(UnicornIsland.creatures) + "in coats of armor. Notable members of this community are the Unicorn Leader, the Spiritual Unicorn, the Unicron Student, and the Horn-master.\n"	#"The Unicorn Clan is an ally to the Kingdom. Attacking any of their residents will result in your instant execution by the Unicorn Leader, and a brutal war between your territories. "
		if positionY == 2:
			print "VAMPIRE MANSION: You enter a dark abandoned-looking mansion and feel a sudden chill rush over you. Your every step seems to be monitored. The floor creaks under your foot and a group of bats emerge from the end of a dark hallway and fly right above your head. But you've been here before, you know what to expect. From memory you recall there being " + len(VampireMansion.creatures) + "vampires and you know the location of their coffins...hopefully. Notable members in this house include Count Dracula, the homeowner, and the vampire bats who turn human at any moment.\n"
		if positionY == 3:
			print "WIZARD TOWER: Always good to be here. Gwydion's 'humble' abode. A 200-foot tower leading up to his Office. You know you can skip leg day whenever you come visit. The stone tower holds a mystical quality, causing everyone to fall into a calm and pensive state. " + len(WizardTower.creatures) + " wizards are walking around, stacks of books following them, floating in midair. They seemed to be in deep thought about...something. There are a few notable individuals in the tower including Gwydion, his apprentice, and a jolly Wizard Janitor, who used his magic to keep the tower neat and clean.\n"
	if positionX == 1:
		if positionY == 0:
			print "CENTAUR FIELD: You come across a lush and mellow field. Several centuars roam the land. Known for their might, the centaurs can always be found training. A few are training at the archery ranges, a few are sprinting around the track, and others still are in the weight area on the field. There are about " + len(CentaurField.creatures) + " directly around you, wearing coats of armor, ready for battle. Some members in this community include Centaur Leader, his wife, a lone guard standing by the entrance, and the premier Centaur Trainer.\n"
		if positionY == 1:
			print "PALACE: The royal Palace of the Kingdom of Arigor is the most magnificent structure in the land. All ministers, guards, and soldiers in the palace are unbelievably loyal to the king, and can be seen diligently working to maintain peace within the lands. In your vicinity, you see King Phillip at his throne, Princess Elizabeth at his side, the royal guard, and a soldier.\n"
		if positionY == 2:
			print "ARIGOR TOWN: The hometown of the kindom's residents. All who live here see Phillip as a fair and wise ruler. A cliched, happy town with several cliched characters, including the Gardener, the Farmer, and the Maiden in Despair.\n"
		if positionY == 3:
			print "CYCLOPS' DEN: You enter a dark, stony cave, lit only by a dim fire. The fire is surrounded by a group of " + len(CyclopsDen.creatures) + " cyclops, each looking dumber than the other. An overwhelming smell of someone who hasn't showered in weeks fills the cave. At the far end of a cave, you see the Cyclops Leader, his trusty assistant, Meathead, and their dinner for the night, a tied up creature of some sort, who looks like he has accepted his fate.\n"
	if positionX == 2:
		if positionY == 0:
			print "SIREN LAKE: You got the boat you needed to explore this land by talking to a man standing at bay. For some reason, he was laughing hysterically, as if laughing at your decision, when you asked him for a boat. Siren Lake looked beautiful this time of day, but beware the dangers. A sweet song filled the air, coming from the sirens swimming underwater. You could make out " + len(SirenLake.creatures) + " dark figures resembling sirens under the lake surface. Some prominent figures in the lake are the Siren Queen, the Oracle, and Ariel the Mermaid."
		if positionY == 1:
			print "Empty Field: You arrive to an empty field. Tall, yellow grass surrounds you, moss covering the stones. One lone oak tree stands in the middle of the field, looking like something straight out of a horror story.\n"
		if positionY == 2:
			print "MARKET: Welcome to the market! Here you can trade goods from your inventory for money, or buy items instead.\n"
		if positionY == 3:
			print "PHOENIX FIELD: Glorious fiery-red creatures fly above you. The field is lush and green, which surprises you, considering the amount of fire it is exposed to. The phoenixes calculate their every step and move with amazing precision. There seem to be " + len(PhoenixField.creatures) + "phoenix soldiers in the sky, along with Alonso the Swift, the phoenix leader, the Feather-Keeper, and a small Rund Phoenix.\n"
	if positionX == 3:
		if positionY == 0:
			print "ELVISH KINGDOM: The legendary Elvish Kingdom is a sight to behold. Every structure was immaculately made. Every single resident looked as if they were hand-crafted by god. The soldiers were the best in the land, and therefore, King Phillip's alliance with the Kingdom is a crucial one. Beware those that oppose the Elves. You see " + len(ElvishKingdom.creatures) + " standing next to you. People that you talk to whenever you come here include, The Elvish King, the Elvish Queen, the Elvish Kight, and the Elvish Apprentice (similar to yourself).\n"
		if positionY == 1:
			print "DRAGON LAIR: You immediately break into a sweat in the near 200 degree heat. Most of the floor is lava, except for a couple large rocks leading to the throne of the Dragon King. " + len(DragonLair.creatures) + " dragons are lounging around, steam coming from their nose, their scales a sight to behold.\n"
		if positionY == 2:
			print "AMAZONIAN KINGDOM: Through a thicket of trees, you enter the Amazonian Kingdom. Large and ripped women roam the land, some on equally large horses, all adorning a suit of armor. Step pyramids of various sizes are dispersed around the kingdom. On the tallest of the pyramids, sat the Amazonian Queen, the strongest and wisest of the women, accompanied by her Amazonian Guard and her Strategist."
		if positionY == 3:
			print "PUZZLE ROOM: Welcome to the Puzzle Room! The puzzles never stop. Every time you enter this room, a new puzzle is created. If you solve the puzzle you get MONEY!!\n"
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

############################################Quest helper functions############################################################################

questCompleteBool = False; #certain value is checked in the end of the main loop to make sure the quest is not yet complete. If questCompleteBool is true at end of game loop, level up alexander and levelChange function is initiated
quest1 = [goneToWizardTower, talkedToGwydion]		#deliver parcel to Gwydion
quest2 = [goneToGoblinLair, talkedToGoblinKing, defeatedGoblins]		#retrieve sword from Goblins
quest3 = [goneToVampireMansion, talkedToCount, defeatedVampires]		#rescue princess from Vampires
quest4 = [goneToCyclopsDen, talkedToCyclopsLeader, confusedCyclops]		#retrieve Gwydion's orb from the Cyclops' Cave
quest5 = [goneToUnicornField, talkToUnicornLeader, goToHappinessHourglass, shrinkDown, defeatZombieGerms, receiveReward]		#help unicorns restore happiness
quest6 = [goneToPhoenixField, talkedToAlonso, defeatedFirstWave_Sirens, saveNursery, saveAlonso]		#Save Phoenix Field from Siren attack
quest7 = [goToElvishKingdom, talkToElfKing, solveElfPuzzle]		#Earn respect of the Elves
quest8 = [goToArigorTown, climbTallestBuilding, defeatOneDragon, useGwydionOrb, defeatDragonKing, talkToKingPhillip]		#save Arigor Town from the dragon attack 	#phillip is injured during the attack
quest9 = [gatherAtWizardTower, makeCentaursAttackGoblinsAndVampires, makesWizardsAttackCyclops, identifyCommonObjective, stopBattle]		#Lead war against Foes
def questAssistant(level): 	#function knows quest based on level input. function is meant to keep track of what has been done, and print/update subsequent aspects of the game, based on what you've done


def questBoolCheckAndUpdate(level): 	#based on the level input, function knows which quest alex is undertaking. The function is called at the end of the main game loop, and goes through the checklish of what the quest requires and updates the bools.
	if level == 1:
		for x in quest1:

	elif level == 2:
	elif level == 3:
	elif level == 4:
	elif level == 5:
	elif level == 6:
	elif level == 7:
	elif level == 8:
	elif level == 9:	

#################################################################################################################################################

def changeAttributes_levelChange(level):	#changes attributes of alex and some other people when he reaches a new level. For example changes the dialog he speakes with the princess
	print "You have completed your quest and leveled up! This comes with a lot of exciting new upgrades to your skills, as well as new accessibilities in the game.\n"
	if level == 2:
		Palace.people[0].dialogue = "Alexander! Thank you for delivering the parcel to Gwydion. There have been developments that allow for me to tell you exactly what you delivered. You see, now that the peace between the Elves and the Amazonians is broken, I am trying to make sure history does not repeat itself.\nInside the parcel lay my plan to rebuild the peace, by rallying all of our allies towards teh process. However, the clans understand how costly the struggle will be. Centaur Field is not going to fight with us unless they get something in return. Their price is the return of the Sacred Sword of Hudotos. Legend says that Hudotos was single-handedly able to defeat an army of Goblins using only that sword. Centaur intelligence says that a goblin spy infiltrated their treasury and stole the sword. Alexander, I'm going to need you to retrieve the sword. Having the centaurs on our side is vital to my plan, and this is the only way they will cooperate. I would start by going to the Goblin's Lair to see what you can find. Godspeed Alexander.\n"
	elif level == 3:
	elif level == 4:
	elif level == 5:
	elif level == 6:
	elif level == 7:
	elif level == 8:
	elif level == 9:
	elif level == 10:

	if level != 10:
		print "You can also start the next quest, just go talk to King Phillip and he will inform you of your mission.\n"
	else:
		print "Congratulations! You have completed the trials presented to you in Arigor. As a reward for your incredible bravery and service, you have been granted the position of Head Knight, the youngest ever to achieve such a feat! You see Princess Elizabeth from the corner of your eye, and you finally have the courage to walk up to her, and ask her to get dinner. \"A real date,\" you say to her blushing face. King Phillip has a statue of yourself built in the town square, and several generations of children look up to you as the greatest inspiration in their lives. Farewell, young Sir, and live the rest of your life to its fullest.\n"


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

	if questCompleteBool == True:
		Alexander.level += 1
		changeAttributes_levelChange(Alexander.level)

	questCompleteBool = False;

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

	elif user_input_split[0] == "attack":	#TODO 	#use sleep to give user the illusion of a fight. Randomly assert critical hit

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