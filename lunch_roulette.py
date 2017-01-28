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

def restaurant_chat():
    '''make the running of roulette a little more fun'''
    print "Here we go!!!"
    time.sleep(1)
    print "Who's hungry?!"
    time.sleep(2)
    print "\n...I know I am."
    time.sleep(1)
    print "Your selected restaurant for lunch roulette is....."
    time.sleep(3)
    print "I need a drum roll here!"
    i = 0
    while i < 30:
        print "."
        time.sleep(0.05)
        i += 1
    print "\n" + the_pick
    time.sleep(1)
    print "\nI'm really excited for you.\n"

def respin_reset():
    '''if it's been more than six months since a participant used a respin, reset it'''
    for item in participant_dict['people']:
        if participant_dict['people'][item]['respin']['available'] == False:
            if (datetime.date.today() - datetime.datetime.strptime(participant_dict['people'][item]['respin']['date-used'], '%Y-%m-%d').date()).days > (364/2):
                participant_dict['people'][item]['respin']['date-used'] = ""
                participant_dict['people'][item]['respin']['available'] = True


# without_spins.append((participant_dict['people'][item]['first-name'] + participant_dict['people'][item]['nickname'], (364/2) - (datetime.date.today() - datetime.datetime.strptime(participant_dict['people'][item]['respin']['date-used'], '%Y-%m-%d').date()).days))

def shame(name_arg, i):
    '''if someone tries to respin and they don't have one available, make fun of them.'''
    date_used = participant_dict['people'][i]['respin']['date-used']
    days_to_next_use = ((364/2) - (datetime.date.today() - datetime.datetime.strptime(participant_dict['people'][i]['respin']['date-used'], '%Y-%m-%d').date()).days)
    print "WHOA, WHOA, WHOA!!!"
    time.sleep(1)
    print "Hold your horses there %s!!!" % name_arg
    print "You used your re-spin back on %s" % date_used
    time.sleep(3)
    print "Someone needs to add 'SIMPLE ARITHMETIC' to their PDP, eh?"
    time.sleep(3)
    print "Since we all just found out that this isn't your strong suit, I'll figure it out for you."
    time.sleep(5)
    print "You have %d more days before you can use another respin." % days_to_next_use
    print "Which is %s" % str(datetime.date.today() + datetime.timedelta(days_to_next_use))
    time.sleep(3)
    print "You may want to write that down."

def check_spin_status(name_arg):
    '''check to see if someone can respin'''
    for i in participant_dict['people']:
        if participant_dict['people'][i]['first-name'] == name_arg:
            if participant_dict['people'][i]['respin']['available'] == True:
                return roulette()
            else:
                return shame(name_arg, i)

        # remind the user of the restaurant that was picked
        # check to see if someone else wants to spin
        # if no, end it
        # if yes


# def respin_chat():
#     '''allow the ability for the user to respin if they think the restaurant selection sucks'''
#     print "But the questions is, 'Are YOU excited?!'"
#     time.sleep(0.5)
#     print "Because there's something we can do about that."
#     def ask_for_respin():
#         return raw_input("Does anyone want to spin again? [Yes or No]\n> ")
#     #if it's a yes, check to make sure the person that asked for the respin, actually has one
#     if ask_for_respin().upper() == "YES":
#         print "Hmmm......"
#         time.sleep(1)
#         print "Interesting...."
#         time.sleep(1)
#         print "And, who is it that would like to me to spin again?"
#         time.sleep(0.5)
#
#
#
#     x = 0
#     while x < 1:
#         respin_choice = raw_input("How do you feel about this restaurant? Someone want to respin?! [Yes or No]\n> ")
#         if respin_choice.upper() == "YES":
#             spin_status = find_spin_status()
#             print "Hmmm....."
#             time.sleep(1)
#             print "Interesting..."
#             time.sleep(1)
#             print "Let me just check something right quick..."
#             time.sleep(1)
#             if len(spin_status) == 0:
#                 print "That's gonna be a problem, because there isn't ONE of you that's waited long enough to earn your spin back."
#                 time.sleep(1)
#                 print "SHAME!!!!"
#                 time.sleep(1)
#                 print "You're going to %s whether you like it or not!" % the_pick
#                 break
#             else:
#                 print "Good news!"
#                 time.sleep(0.25)
#                 print "There are %d of you with spins available" % len(spin_status)
#                 potential_spinner = raw_input("Who want to use their respin? First name only please.\n> ")
#
#                 #FIX THISS!!!!!!
#                 for key in spin_status:
#                     if potential_spinner.upper() == key].upper():
#                         participant_dict['people'][i]['respin']['available'] = False
#                         participant_dict['people'][i]['respin']['date-used'] = str(datetime.date.today())
#                         restaurant_chat()
#             x += 1
#         elif respin_choice.upper() == "NO":
#             print "God speed, enjoy your dining experience"
#             x += 1
#         else:
#             print "Where did you learn how to type? Let's try this again.\n"

'''
RUN STUFF DOWN HERE
'''

# restaurant_chat()
# respin_chat()

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
