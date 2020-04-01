import random
import math


"""
0
Dice games
"""

#We will need this code below

def is_prime(n):
    """
    n: int >=0
    return:bool == True iff n is prime
    """
    if n < 2:
        return False
    div = 2
    while div <= math.sqrt(n):
        if n%div == 0:
            return False
        div = div + 1
    return True

#************************
#** DICE and the DIE class
#*************************

class Die(object):
    # a die has one attribute (value) but
    #the user is not allowed to specify it
    def __init__(self):
        """
        attributes: value
        chosen randomly, NOT by user
        """
        self.value = random.randint(1,6)

    def __str__(self):
        """
        return a string value that looks like this: "[3]"
        showing whatever is the value of the die
        """
        return "[" + str(self.value) + "]"

    def roll(self):
        """
        return nothing. Just pick a random value for the dia
        """
        self.value = random.randint(1,6)

d = Die()
print(d)
d.roll()
print(d)


##****************************************
#1: The first computes the average value of 2 dice in a 1000 rolls
#Should be close to 7
#****************************************
print("""
***
*** average value of two dice in 1000 rolls"
***
""")
d1 = Die()
d2 = Die()
total = 0
for i in range(1000):
   total += d1.value + d2.value
   d1.roll()
   d2.roll()
print("average value of roll = ", total/1000.0)

##****************************************
#Complete the following bit of code
#2: Compute the average no of rolls
# of two dice to get a 2
#in 1000 trials
#Should be close to 36
#****************************************
print("""
***
***average no. of rolls to get a 2
***
""")
d1 = Die()
d2 = Die()
total = 0 
for trials in range(1000):
    d1.roll()
    d2.roll()
    count_rolls = 1
    while d1.value + d2.value != 2:
        d1.roll()
        d2.roll()
        count_rolls += 1
    total += count_rolls
print(total/1000)

"""
A sketch of a game class
"""
class Game(object):
    """
    roll two dice, adding up points until:
    you get a prime and win OR
    you get a multiple of 10 DDISTINCT FROM 0 and lose
    """
    #class variables
    WIN = 1  #Game.WIN is how you use this
    LOSE = -1
    PLAY  = 0
    
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()
        self.start()
        

    def start(self):
        
        self.user_wants_to_play = True #use this to define an outer loop
        #that replays the game until the user does not want to play

        while self.user_wants_to_play:
            self.total = 0
            while self.status() == Game.PLAY:
                input("Hit <enter> to roll the dice: ")
                self.die1.roll()
                self.die2.roll()
                self.total += self.die1.value + self.die2.value
                print(self) #to show the player what has just happened
            if self.status() == Game.WIN:
                print("you won!")
            elif self.status() == Game.LOSE:
                print("you lost bruh!")
            x = input("Play Again? (y/n): ")
            if x == "n":
                self.user_wants_to_play = False
        print("GOOD BYE!")
                
                

    def __str__(self):
        return "die 1 is " + str(self.die1.value) + "\n" + \
                "die 2 is " + str(self.die2.value) + "\n" + \
                "total is " + str(self.total)
    
    def status(self):
        if is_prime(self.total) and self.total > 10:
            return Game.WIN
        elif self.total%10 == 0 and self.total != 0:
            return Game.LOSE
        else:
            return Game.PLAY

#The next line starts the game because it creates an object of the
#Game class
Game()






"""
4: Student
Define a class of students.
A student might have
-- a name:str
-- a social security number:str   
-- an address:str
-- a transcript: a list of PAIRS
   [("MACRAME","A"),("Philosophy of Mind","B"),...]
(This can be done better with dictionaries, to be discussed later in
the course) 
--anything else you want

Provide methods to retrieve the name, address, ss#
and grade for a given course, and anything else you want.
Be creative
"""

class Student(object):
    pass




    
