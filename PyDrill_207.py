# Python 3.8.5
# Author: Samantha Billips
# Polymorphism assignment 207
# Create 2 classes that inherit from another class
# 1. Each Child class should have at least two of their own attributes
# 2. The parent class should have atleast one method(function)
# 3. Both chld classes should utilize polymorphism on the parent class method
# 4. Add comments throughout code


#parent class New_char






class gameUser:
    c_name = ""
    c_password = "424242"

    def getcharinfo(self):
        c_nameEntry = input("Greetings, Wanderer! What is your name?:  ")
        c_passwordEntry = input("{}, eh? May I have the password?:  ".format(c_nameEntry))
        if (c_passwordEntry == self.c_password):
            print("Welcome, {}!\n\n Here's a gift that will prove helpful on your journey!\n\n *You recieve 5,000 Gold!*".format(c_nameEntry))

        else:
            print("Incorrect password. You shall not pass!")

#child class for gameUser
class CharInfo(gameUser):
    charRace = "Half-Elf"
    charClass = "Bard"
    tollGold = "5000"

#Same method; instead of c_password, use tollGold
    def getcharinfo(self):
        c_tollGold = input("\n\n*You approach a bridge. You need to cross it in order to get to the city, \nbut to your dismay, it's guarded by a troll. He doesn't seem happy to see you*\n\n\
BAH! YOU NEED TO PAY THE TROLL TOLL! HOW MUCH GOLD 'AVE YA GOT?:  ")
        if (c_tollGold == self.tollGold):
            print("{}, is it? Well, that's enough. Carry on. ".format(c_tollGold))
        else:
            print("YER DON'T HAVE ENOUGH GOLD TO PAY THE TOLL! GET OUTTA HERE, YA DINGUS!")

#invokes methods inside getcharinfo and CharInfo classes
Player = gameUser()
Player.getcharinfo()

Character = CharInfo()
Character.getcharinfo()
