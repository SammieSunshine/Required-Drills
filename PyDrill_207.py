# Python 3.8.5
# Author: Samantha Billips
# Polymorphism assignment 207
# Create 2 classes that inherit from another class
# 1. Each Child class should have at least two of their own attributes
# 2. The parent class should have atleast one method(function)
# 3. Both chld classes should utilize polymorphism on the parent class method
# 4. Add comments throughout code


#Parent Class
class gameUser(): 
    c_name = ""
    c_password = "424242"

    
    def getcharinfo(self):
        c_nameEntry = input("Greetings, Wanderer! What is your name?:  ")
        c_passwordEntry = input("{}, eh? May I have the password?:  ".format(c_nameEntry))
        if (c_passwordEntry == self.c_password):
            print("Welcome, {}!\n\n Here's a gift that will prove helpful on your journey!\n\n *You recieve 5,000 Gold!*".format(c_nameEntry))
        
        else:
            print("Fine. whatever. Just go on, then.\n\n*A small bag hits you in the face. You look inside the bag to find 5,000 gold!*")

#child class CharInfo
class CharInfo(gameUser):
    charRace1 = "Elf"
    charRace2 = "Human"
    charClass1 = "Bard"
    charClass2 = "Muggle"
    tollGold = "5000" #Changed from INT to Str

    def charRace(self):
        raceEntry = input("Before you begin your journey, You must decide who your are. Are you an Elf or a human?: ")
        if (raceEntry == self.charRace1 or raceEntry == self.charRace2):
            print("I see. You're a {}!".format(raceEntry))

        else:
            print("Why so secretive?! Whatever. Go on. *Mumbles*")
            
    def charClass(self):
        classEntry = input("Bards are natural performers, but there's nothing wrong with being a muggle! Which are you?".format(classEntry))
        if (Class == self.charClass1 or Class == self.charClass2):
            print("You've decided who you are. \nSome will welcome you with open arms, while others shun you.\nStand strong, wanderer. Change for no one.")

        else:
            print("My. Aren't you just plain. Whatever. Move along.")
                

    #Same method seen in Parent Class
    #instead of c_tollGold, use tollGold
    def Troll(self):
        c_nameEntry = input("\n\n*You approach a bridge. You need to cross it in order to get to the city, \nbut to your dismay, it's guarded by a troll. He doesn't seem happy to see you*\n\n\"GARRGH! WHAT IS YOUR NAME?:" )
        c_tollGold = input("BAH! NO MATTER! YOU NEED TO PAY THE TROLL TOLL! HOW MUCH GOLD 'AVE YA GOT?:  ")
        if (c_tollGold == self.tollGold and c_nameEntry == self.c_nameEntry):
            print("{}, is it? Well, {}, carry on. ")
        else:
            print("YER DON'T HAVE ENOUGH GOLD TO PAY THE TOLL! GET OUTTA HERE, YA DINGUS! /n*Ouch!*/n*The toll troll kicks you SO HARD that he/nsends you FLYING back to the starting point*")



#invokes methods inside getcharinfo and CharInfo classes
Player1 = gameUser()
Player1.getcharinfo()

Character = CharInfo()
Character.getcharinfo()


        
