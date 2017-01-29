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
    '''return a restaurant at random from the available list'''
    restaurant = np.random.choice(rawlist)
    return restaurant

the_pick = roulette()
new_pick = ""

def respin_reset():
    '''if it's been more than six months since a participant used a respin, reset it'''
    for item in participant_dict['people']:
        if participant_dict['people'][item]['respin']['available'] == False:
            if (datetime.date.today() - datetime.datetime.strptime(participant_dict['people'][item]['respin']['date-used'], '%Y-%m-%d').date()).days > (364/2):
                participant_dict['people'][item]['respin']['date-used'] = ""
                participant_dict['people'][item]['respin']['available'] = True

def ask_for_respin():
    response = raw_input("\nDoes anyone want to spin again? [Yes or No]\n> ")
    return process_respin_response(response)

def ask_for_respin_again():
    response = raw_input("\nAnyone else wanna go!? [Yes or No]\n> ")
    return process_respin_response(response)

def update_spin_status(dict_id):
    '''when a person uses their respin, set their availability to false and set their date used to today'''
    participant_dict['people'][dict_id]['respin']['available'] = False
    participant_dict['people'][dict_id]['respin']['date-used'] = str(datetime.date.today())

def process_respin_response(response):
    if response.upper() == "YES":
        print "\nMmmm Hmmm......"
        time.sleep(1)
        print "\nInteresting...."
        time.sleep(1)
        name_check = raw_input("\nAnd, who is requesting this spin?\n> ")
        check_spin_status(name_check)
    elif response.upper() == "NO":
        print "\nGod speed, enjoy your dining experience.\n"
    else:
        time.sleep(0.5)
        print "\nWhere did you learn how to type?"
        time.sleep(0.5)
        print "\nLet's try that again."
        ask_for_respin()

def shame(name_arg, i):
    '''if someone tries to respin and they don't have one available, make fun of them.'''
    date_used = participant_dict['people'][i]['respin']['date-used']
    days_to_next_use = ((364/2) - (datetime.date.today() - datetime.datetime.strptime(participant_dict['people'][i]['respin']['date-used'], '%Y-%m-%d').date()).days)
    print "WHOA, WHOA, WHOA!!!"
    time.sleep(1)
    print "\nHold your horses there %s!!!" % name_arg
    print "\nYou used your re-spin back on %s" % date_used
    time.sleep(3)
    print "\nSomeone should think about adding 'SIMPLE ARITHMETIC' to their PDP, eh?"
    time.sleep(3)
    print "\nYou still have a little time before you can use another respin"
    time.sleep(2)
    print "\nAnd, Since we all just found out math isn't your strong suit,\n I'll figure it out for you."
    time.sleep(3)
    print "\nYou have %d more days before you can use another respin." % days_to_next_use
    print "\nWhich is %s" % str(datetime.date.today() + datetime.timedelta(days_to_next_use))
    time.sleep(3)
    print "\nYou may want to write that down.\n"
    time.sleep(2)
    ask_for_respin_again()

def respin():
    print "\nYour reqeust for a new spin has been approved by the Meal Enhancement Computer."
    time.sleep(2)
    print "\nAlso known as the... MEC"
    time.sleep(0.5)
    print "\nHere comes your new pick.\n\n\n"
    time.sleep(5)
    new_pick = roulette()
    print new_pick.upper()
    time.sleep(3)
    print "\nI hope you feel good about your choice.\n"

def check_spin_status(name_arg):
    '''check to see if someone can respin'''
    respin_reset()
    for i in participant_dict['people']:
        if participant_dict['people'][i]['first-name'].upper() == name_arg.upper():
            if participant_dict['people'][i]['respin']['available'] == True:
                time.sleep(2)
                print "Alright, that checks out."
                update_spin_status(i)
                time.sleep(2)
                return respin()
            else:
                return shame(name_arg, i)
    print "\nI can't find that name on my list, so let's try again."
    time.sleep(1)
    new_name = raw_input("\nWho want's the respin? First name only please.\n> ")
    return check_spin_status(new_name)

def respin_chat():
    '''allow the ability for the user to respin if they think the restaurant selection sucks'''
    print "\nBut I think we should be asking, 'Are YOU excited?!'"
    time.sleep(3)
    print "\nBecause we can do something about that if you're not."
    time.sleep(3)
    ask_for_respin()

def restaurant_chat():
    '''make the running of roulette a little more fun'''
    print "Here we go!!!"
    time.sleep(1)
    print "\nWho's hungry?!"
    time.sleep(2)
    print "\n...I know I am."
    time.sleep(1)
    print "\nYour selected restaurant for lunch roulette is....."
    time.sleep(3)
    print "\nI need a drum roll here!"
    time.sleep(1)
    i = 0
    while i < 30:
        print "."
        time.sleep(0.05)
        i += 1
    print "\n" + the_pick
    time.sleep(1)
    print "\nI'm really excited for you.\n"
    time.sleep(4)
    respin_chat()

'''
RUN STUFF DOWN HERE
'''

restaurant_chat()

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
