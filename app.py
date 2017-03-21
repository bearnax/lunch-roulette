import time
import json
import datetime
import random
import sys

# ======================================================================
#                                                      DEFINE CONSTANTS
# ======================================================================

lunch_data_filename = "lunch_spots.json"
user_data_filename = "participants_test.json"
# TODO: add a third file location to store individual 'runs' of roulette


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

def initialize_classes():
    temp = Data() # create the data object for this instance
    temp.set_lunch_spots()
    temp.set_users()
    return temp

def run_app():
    delay_print("Welcome to Lunch Roulette.")
    delay_print("For those about to eat, we salute you!")

    session_data = initialize_classes()

    eligible_options_for_printing = "There are {} restaurants that qualify.".format(session_data.count_eligible_restaurants())
    delay_print(eligible_options_for_printing)

    delay_print("But... there can be oNLY ONE!!!!")

    session_data.make_a_pick()
    delay_print("And your restaurant this month is...!")
    delay_print(session_data.pick.name)

    # would you like to respin?
    delay_print("Good choice right?")
    delay_print("I supposed I could give it another go if you like.")
    delay_print("Want me to pick again? [Yes/No]")

    q = input("> ")
    if q.upper() == "YES":
        delay_print("Very well.")
        delay_print("LET'S DO THIS!")
        session_data.make_a_pick()
        delay_print("Please enjoy.....")
        delay_print(session_data.pick.name)
        delay_print("I hope you feel good about your life choices that landed you here.")
    elif q.upper() == "NO":
        delay_print("Fair enough.")
        response_for_no_respin = "I hope you enjoy your visit to {} then.".format(session_data.pick.name)
        delay_print(response_for_no_respin)
    else:
        delay_print("Learn how to type. We're done here.")
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
        param: category (self.lunch_spots or self.users)
        """

        count = 0
        for i in category:
            if i.available == False:
                if (datetime.date.today() - datetime.datetime.strptime(i.date-used, '%Y-%m-%d').date()).days > i.time:
                    i.reset()
                    count += 1
        print("Selective Reset Complete. {} Reset.".format(count))

    def full_reset(self, category):
        """
        reset all availability and dates for either users or lunch set_lunch_spots

        param: category = self.lunch_spots or self.users
        """

        are_you_sure = input("Are you sure you want to reset all lunch locations? [YES/NO]\n> ")
        count = 0
        if are_you_sure.upper() == "YES":
            for i in category:
                i.reset()
                count += 1
            print("Full Reset Complete. {} Reset.".format(count))
        else:
            print("You answered No. I won't make any changes then.")

    def count_eligible_restaurants(self):
        eligible_list = []
        for i in self.lunch_spots:
            if i.include == True and i.available == True:
                eligible_list.append(i)
        return len(eligible_list)

    def make_a_pick(self):
        filtered_list = []
        for i in self.lunch_spots:
            if i.include == True and i.available == True:
                filtered_list.append(i)
        self.pick = random.choice(filtered_list)

# ======================================================================
#                                                               RUN CODE
# ======================================================================

def main():
    run_app()
    # print("Welcome to Lunch Roulette. Let's get started.")
    #
    # session_data = initialize_classes()
    # session_data.count_eligible_restaurants()
    #
    # session_data.full_reset(session_data.lunch_spots)
    # session_data.count_eligible_restaurants()
    #
    # q = input("Would you like to make a pick?[Yes/No]\n> ")
    # if q.upper() == "YES":
    #     print("Excellent choice.")
    #     session_data.make_a_pick()
    #     print(session_data.pick.name)
    # else:
    #     pass

if __name__ == '__main__':
    status = main()
    sys.exit(status)

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
