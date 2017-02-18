import time
import json
import datetime
import random
import sys

# ======================================================================
#                                                      DEFINE CONSTANTS
# ======================================================================

lunch_data_filename = "lunch_locations_test.json"
user_data_filename = "participants_test.json"

# ======================================================================
#                                            DEFINE FUNCTIONS AND STUFF
# ======================================================================

''' IMPORT DATA FROM JSON FILES'''
def load_json(filename):
    with open(filename) as json_data:
        return json.load(json_data)

def dump_json(filename, data_to_export):
    with open(filename, 'w') as json_data:
        json.dump(data_to_export, json_data, sort_keys=True, indent=4)

def json_update_lunch_location(pick):
    '''for the restaurant selected, change it's availability to false and set the date of the lunch roulette that the user gave'''

    locations_to_save = load_json(lunch_data_filename)
    for i in locations_to_save:
        if i['name'] == pick:
            i['available'] = False
            i['date-used'] = str(datetime.date.today())
    dump_json(lunch_data_filename, locations_to_save)

#COMMAND LINE FUNCTIONS AND CONTROLS

# define your ridiculous slow printing function
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")
    time.sleep(0.5)

'''EXPORT FINISHED DATA TO JSON'''

# with open('participants.json', 'w') as json_data:
#     json.dump(participant_dict, json_data, sort_keys=True, indent=4)
#
# with open('lunch_locations.json', 'w') as json_data:
#     json.dump(lunch_dict, json_data, sort_keys=True, indent=4)

def inititalize_data():
    temp = Data()
    temp.set_lunch_spots()
    temp.filter_lunch_spots()
    temp.set_users()
    return temp

def run_app():
    delay_print("Welcome to Lunch Roulette.")
    delay_print("For those about to eat, we salute you!")
    session_data = inititalize_data()

    delay_print("Would you like to make a pick?[Yes/No]?")
    q = input("> ")
    if q.upper() == "YES":
        delay_print("Excellent choice.")
        session_data.make_a_pick()
        delay_print("Here's your choice!")
        delay_print(session_data.pick.name)
    else:
        pass

    pass

# ======================================================================
#                                                         DEFINE CLASSES
# ======================================================================

class LunchSpot(object):
    def __init__(self, name, available, date_used, include):
        self.name = name
        self.available = available
        self.date_used = date_used
        self.include = include
        self.time = 365

    def reset(self):
        self.date_used = ""
        self.available = True

class User(object):
    def __init__(self, first_name, last_name, nickname, available, date_used):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.nickname = nickname
        self.available = available
        self.date_used = date_used
        self.time = 364/2

    def reset(self):
        self.date_used = ""
        self.available = True

class Data(object):
    def __init__(self):
        self.lunch_spots = []
        self.filtered_lunch_spots = []
        self.users = []
        self.pick = None

    def set_lunch_spots(self):
        lunch_data = load_json(lunch_data_filename)
        for i in lunch_data:
            self.lunch_spots.append(LunchSpot(
                i['name'],
                i['available'],
                i['date-used'],
                i['include']
            ))

    def filter_lunch_spots(self):
        if len(self.lunch_spots) > 0:
            for i in self.lunch_spots:
                if i.include == True and i.available == True:
                    self.filtered_lunch_spots.append(i)
        else:
            print("No locations available, attempting to import")
            try:
                self.set_lunch_spots()
            except:
                print("Unable to import")
                pass

    def set_users(self):
        user_data = load_json(user_data_filename)
        for i in user_data:
            self.users.append(User(
                i["first-name"],
                i["last-name"],
                i['nickname'],
                i['available'],
                i['date-used']
            ))

    def selective_reset(self, category):
        """
        category = self.filtered_lunch_spots or self.users
        """

        count = 0
        for i in category:
            if i.available == False:
                if (datetime.date.today() - datetime.datetime.strptime(i.date-used, '%Y-%m-%d').date()).days > i.time:
                    i.reset()
                    count += 1
        print("Selective Reset Complete. {} Reset.".format(count))

    def full_reset(self, category):
        """ reset all availability and dates for either users or lunch set_lunch_spots

        param: category = self.filtered_lunch_spots or self.users
        """

        are_you_sure = input("Are you sure you want to reset all lunch locations? [YES/NO]\n> ")
        count = 0
        if are_you_sure == "YES":
            for i in category:
                i.reset()
            print("Full Reset Complete. {} Reset.".format(count))
        else:
            print("You answered No. I won't make any changes then.")

    def make_a_pick(self):
        self.pick = random.choice(self.filtered_lunch_spots)

# ======================================================================
#                                                               RUN CODE
# ======================================================================

def main():
    # run_app()
    print("Welcome to Lunch Roulette. Let's get started.")

    session_data = inititalize_data()

    q = input("Would you like to make a pick?[Yes/No]\n> ")
    if q.upper() == "YES":
        print("Excellent choice.")
        session_data.make_a_pick()
        print(session_data.pick.name)
    else:
        pass

if __name__ == '__main__':
    status = main()
    sys.exit(status)

#
# def ask_for_respin():
#     response = raw_input("\nDoes anyone want to spin again? [Yes or No]\n> ")
#     return process_respin_response(response)
#
# def ask_for_respin_again():
#     response = raw_input("\nAnyone else wanna go!? [Yes or No]\n> ")
#     return process_respin_response(response)
#
# def update_spin_status(dict_id):
#     '''when a person uses their respin, set their availability to false and set their date used to today'''
#     participant_dict['people'][dict_id]['respin']['available'] = False
#     participant_dict['people'][dict_id]['respin']['date-used'] = str(datetime.date.today())
#
# def process_respin_response(response):
#     if response.upper() == "YES":
#         print "\nMmmm Hmmm......"
#         time.sleep(1)
#         print "\nInteresting...."
#         time.sleep(1)
#         name_check = raw_input("\nAnd, who is requesting this spin?\n> ")
#         check_spin_status(name_check)
#     elif response.upper() == "NO":
#         print "\nGod speed, enjoy your dining experience.\n"
#     else:
#         time.sleep(0.5)
#         print "\nWhere did you learn how to type?"
#         time.sleep(0.5)
#         print "\nLet's try that again."
#         ask_for_respin()
#
# def shame(name_arg, i):
#     '''if someone tries to respin and they don't have one available, make fun of them.'''
#     date_used = participant_dict['people'][i]['respin']['date-used']
#     days_to_next_use = ((364/2) - (datetime.date.today() - datetime.datetime.strptime(participant_dict['people'][i]['respin']['date-used'], '%Y-%m-%d').date()).days)
#     print "WHOA, WHOA, WHOA!!!"
#     time.sleep(1)
#     print "\nHold your horses there %s!!!" % name_arg
#     print "\nYou used your re-spin back on %s" % date_used
#     time.sleep(3)
#     print "\nSomeone should think about adding 'SIMPLE ARITHMETIC' to their PDP, eh?"
#     time.sleep(3)
#     print "\nYou still have a little time before you can use another respin"
#     time.sleep(2)
#     print "\nAnd, Since we all just found out math isn't your strong suit,\n I'll figure it out for you."
#     time.sleep(3)
#     print "\nYou have %d more days before you can use another respin." % days_to_next_use
#     print "\nWhich is %s" % str(datetime.date.today() + datetime.timedelta(days_to_next_use))
#     time.sleep(3)
#     print "\nYou may want to write that down.\n"
#     time.sleep(2)
#     ask_for_respin_again()
#
# def respin():
#     print "\nYour reqeust for a new spin has been approved by the Meal Enhancement Computer."
#     time.sleep(2)
#     print "\nAlso known as the... MEC"
#     time.sleep(0.5)
#     print "\nHere comes your new pick.\n\n\n"
#     time.sleep(5)
#     second_pick = lunch_dict['locations'][select_random_restaurant()]['name']
#     print second_pick.upper()
#     time.sleep(3)
#     print "\nI hope you feel good about your choice.\n"
#
# def check_spin_status(name_arg):
#     '''check to see if someone can respin'''
#     respin_reset()
#     for i in participant_dict['people']:
#         if participant_dict['people'][i]['first-name'].upper() == name_arg.upper():
#             if participant_dict['people'][i]['respin']['available'] == True:
#                 time.sleep(2)
#                 print "Alright, that checks out."
#                 update_spin_status(i)
#                 time.sleep(2)
#                 return respin()
#             else:
#                 return shame(name_arg, i)
#     print "\nI can't find that name on my list, so let's try again."
#     time.sleep(1)
#     new_name = raw_input("\nWho want's the respin? First name only please.\n> ")
#     return check_spin_status(new_name)
#
# def respin_chat():
#     '''allow the ability for the user to respin if they think the restaurant selection sucks'''
#     print "\nBut I think we should be asking, 'Are YOU excited?!'"
#     time.sleep(3)
#     print "\nBecause we can do something about that if you're not."
#     time.sleep(3)
#     ask_for_respin()
#
# def restaurant_chat():
#     '''make the running of roulette a little more fun'''
#     print "Here we go!!!"
#     time.sleep(1)
#     print "\nWho's hungry?!"
#     time.sleep(2)
#     print "\n...I know I am."
#     time.sleep(1)
#     print "\nYour selected restaurant for lunch roulette is....."
#     time.sleep(3)
#     print "\nI need a drum roll here!"
#     time.sleep(1)
#     i = 0
#     while i < 30:
#         print "."
#         time.sleep(0.05)
#         i += 1
#     print "\n" + first_pick
#     time.sleep(1)
#     print "\nI'm really excited for you.\n"
#     time.sleep(4)
#     respin_chat()
#


''' RUN STUFF DOWN HERE '''

# restaurant_chat()
# set_restaurant_status()
