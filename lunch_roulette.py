import random
import numpy as np
import time

rawlist = [
    "H Mart",
    "El Ray del Taco",
    "Chinese Cultural Center",
    "Mellow Mushroom",
    "Heirloom BBQ",
    #too far "Fat Matt's",
    "Pho and/or Bahn Mis",
    "Costco",
    "Eclipse di Luna",
    "Desta",
    "Cho Dang Tofu House (Korean BBQ)",
    "Flying Biscuit",
    "Waffle House",
    "ShakeShack",
    "Olive Garden",
    "Marlow's Tavern",
    "Superica",
    "Greek",
    "Chick-fil-a",
    #too far "Australian Bakery",
    "Takorea",
    "Taco Veloz",
    "McDonald's",
    #too far "Purnima",
    "Teela Taqueria",
    "Royal China, Dim Sum",
    "CowFish",
    "J's Mini HotPot Deluxe",
    "Nori Nori",
    #too far "Sushi Kiko"
]

# print len(rawlist)
# rand_item = random.choice(rawlist)
# print rand_item
# print len(rawlist)
#
# numpy_item = np.random.choice(rawlist,size=None,replace=False)
# print numpy_item
# print len(rawlist)

def select_restaurant():
    print "\nHere we go!!!"
    time.sleep(1)
    print "Who's hungry?!"
    time.sleep(3)
    print "\nI know I am."
    time.sleep(1)
    print "Your selected restaurant for lunch roulette is....."
    time.sleep(3)
    print "Drum roll please"
    i = 0
    while i < 15:
        print "."
        time.sleep(0.1)
        i += 1
    print np.random.choice(rawlist).upper()
    time.sleep(1)
    print "\nI'm really excited for you.\n"

#Allow Vetos
def veto():
    i = 0
    while i < 1:
        veto = raw_input("Does someone want to veto?! [Yes or No]\n >")
        if veto.upper() == "YES":
            print "Well, let's do this again!"
            select_restaurant()
            i += 1
        elif veto.upper() == "NO":
            print "God speed, enjoy your dining experience"
            i += 1
        else:
            print "Where did you learn how to type? Let's try this again.\n"

select_restaurant()
veto()

# NEW FEATURES BASED ON GOOGLE SHEET AND MAPS API

# Import the spreadsheet and create a data table using pandas

# FUNCTION: Pick a restaurant within the users driving limits
    # Remove the restaurants that are too far away
        # Ask the user how far away (in minutes) they're willing to go to eat
        # Use the Maps API to filter out anything greater than distance entered
        # Return a list of restaurants to pick from
            # Show the user the list of what was excluded
            # Pick a random restaurant from the remaining pool
            # Show the user the restaurant name, address, cuisine, $$, and driving distance with and without traffic for the current time.
