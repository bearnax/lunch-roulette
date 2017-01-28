import random
import numpy as np
import time
import json
import datetime

#import all the participants and their ridiculous data
with open('participants.json') as json_data:
    participant_dict = json.load(json_data)

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

def roulette():
    restaurant = np.random.choice(rawlist)
    return restaurant

the_pick = roulette()

def restaurant_chat():
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
    print the_pick
    time.sleep(1)
    print "\nI'm really excited for you.\n"

def reset_respin_availability():
    '''first, check to see if there are any participants that have used their respin, and then see if it was outside of the last six months. If it is outside the last six months, then reset their ability to respin.'''
    for item in participant_dict['people']:
        if participant_dict['people'][item]['respin']['available'] == False:
            if (datetime.date.today() - datetime.datetime.strptime(participant_dict['people'][item]['respin']['date-used'], '%Y-%m-%d').date()).days > (364/2):
                participant_dict['people'][item]['respin']['date-used'] = ""
                participant_dict['people'][item]['respin']['available'] = True

#FIX THIS!!!!
def find_spin_status():
    '''return a list of the participants who have an available respin and how long those who don't must wait before they earn it back'''
    spins = {}
    for item in participant_dict['people']:
        if participant_dict['people'][item]['respin']['available'] == True:
            spins[participant_dict[item] = {}
        else:
            spins[participant_dict[item] = False
    return spins

# without_spins.append((participant_dict['people'][item]['first-name'] + participant_dict['people'][item]['nickname'], (364/2) - (datetime.date.today() - datetime.datetime.strptime(participant_dict['people'][item]['respin']['date-used'], '%Y-%m-%d').date()).days))

def respin():
    '''allow the ability for the user to respin if they think the restaurant selection sucks'''
    x = 0
    while x < 1:
        respin_choice = raw_input("How do you feel about this restaurant? Someone want to respin?! [Yes or No]\n> ")
        if respin_choice.upper() == "YES":
            spin_status = find_spin_status()
            print "Hmmm....."
            time.sleep(1)
            print "Interesting..."
            time.sleep(1)
            print "Let me just check something right quick..."
            time.sleep(1)
            if len(spin_status) == 0:
                print "That's gonna be a problem, because there isn't ONE of you that's waited long enough to earn your spin back."
                time.sleep(1)
                print "SHAME!!!!"
                time.sleep(1)
                print "You're going to %s whether you like it or not!" % the_pick
                break
            else:
                print "Good news!"
                time.sleep(0.25)
                print "There are %d of you with spins available" % len(spin_status)
                potential_spinner = raw_input("Who want to use their respin? First name only please.\n> ")

                #FIX THISS!!!!!!
                for key in spin_status:
                    if potential_spinner.upper() == key].upper():
                        participant_dict['people'][i]['respin']['available'] = False
                        participant_dict['people'][i]['respin']['date-used'] = str(datetime.date.today())
                        restaurant_chat()
            x += 1
        elif respin_choice.upper() == "NO":
            print "God speed, enjoy your dining experience"
            x += 1
        else:
            print "Where did you learn how to type? Let's try this again.\n"

# restaurant_chat()
respin()

#update the participants json file with any changes that were made
with open('participants.json', 'w') as json_data:
    json.dump(participant_dict, json_data, sort_keys=True, indent=4)




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
