import time
import json
from datetime import datetime
import random
import sys
from collections import namedtuple

# ======================================================================
#                                                      DEFINE CONSTANTS
# ======================================================================

lunch_data_filename = "lunch_spots_test.json"
user_data_filename = "participants_test.json"
results_data_filename = "results_test.json"
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

#COMMAND LINE FUNCTIONS AND CONTROLS

# define your ridiculous slow printing function
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")
    time.sleep(0.5)

# def run_app():
#     delay_print("Welcome to Lunch Roulette.")
#     delay_print("For those about to eat, we salute you!")
#
#     session_data = initialize_classes()
#
#     eligible_options_for_printing = "There are {} restaurants that qualify.".format(session_data.count_eligible_restaurants())
#     delay_print(eligible_options_for_printing)
#
#     delay_print("But... there can be ONLY ONE!!!!")
#
#     session_data.make_a_pick()
#     delay_print("And your restaurant this month is...!")
#     delay_print(session_data.pick.name)
#
#     # would you like to respin?
#     delay_print("Good choice right?")
#     delay_print("I supposed I could give it another go if you like.")
#     delay_print("Want me to pick again? [Yes/No]")
#
#     q = input("> ")
#     if q.upper() == "YES":
#         delay_print("Very well.")
#         delay_print("LET'S DO THIS!")
#         session_data.make_a_pick()
#         delay_print("Please enjoy.....")
#         delay_print(session_data.pick.name)
#         delay_print("I hope you feel good about your life choices that landed you here.")
#     elif q.upper() == "NO":
#         delay_print("Fair enough.")
#         response_for_no_respin = "I hope you enjoy your visit to {} then.".format(session_data.pick.name)
#         delay_print(response_for_no_respin)
#     else:
#         delay_print("Learn how to type. We're done here.")
#     pass







# ======================================================================
#                                                              LOAD DATA
# ======================================================================

LunchSpot = namedtuple("LunchSpot", [
    "name",
    "location_id",
    "include"
])

def load_lunch_spots():
    temp_lunch_list = []
    lunch_data = load_json(lunch_data_filename)
    for i in lunch_data:
        temp_lunch_list.append(LunchSpot(
            i["name"],
            i["location_id"],
            i["include"]
        ))
    return temp_lunch_list

Users = namedtuple("Users", [
    "first_name",
    "last_name",
    "nickname"
])

def load_users():
    temp_user_list = []
    user_data = load_json(user_data_filename)
    for i in user_data:
        temp_user_list.append(Users(
            i["first-name"],
            i["last-name"],
            i["nickname"]
        ))
    return temp_user_list

PreviousResults = namedtuple("PreviousResults", [
    "lunch_date",
    "location_id",
    "user_respin_id"
])

def load_results():
    temp_results_list = []
    results_data = load_json(results_data_filename)
    for i in results_data:
        temp_results_list.append(PreviousResults(
            datetime.strptime(i["lunch_date"], "%Y-%m-%d"),
            i["location_id"],
            i["user_respin_id"]
        ))
    return temp_results_list

def remove_recent_locations(list_of_locations, days):
    """ Remove locations from the main list of restaurants
    that were used within a certain number of days

    params:
        list_of_locations = a list of LunchSpots namedtuples
                            the function load_lunch_spots()
        days = an integer, how many days since a restaurant was last used
                           and can be used again.

    """
    temp_list = list_of_locations
    results = load_results()

    for result in results:
        for location in temp_list:
            if location.location_id == result.location_id:
                if (datetime.today() - result.lunch_date).days < days:
                    temp_list.remove(location)
                else:
                    pass
            else:
                pass

    return temp_list

def pick_a_spot():
    """make a pick for lunch

    """
    filtered_list = remove_recent_locations(load_lunch_spots(), 364)

    return random.choice(filtered_list)







# ============================================================================
#                                                                     RUN CODE
# ============================================================================

def main():
    lunch_pick = pick_a_spot()

    print("{}".format(lunch_pick.name))

if __name__ == '__main__':
    status = main()
    sys.exit(status)
