import json
from datetime import datetime
import random
from collections import namedtuple
from db_functions import DatabaseController


lunch_data_filename = "data/lunch_spots_test.json"
user_data_filename = "data/participants_test.json"
results_data_filename = "data/results_test.json"



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



# ======================================================================
#                                                              LOAD DATA
# ======================================================================

LunchSpot = namedtuple("LunchSpot", [
    "name",
    "location_id",
    "include"
])

def load_lunch_spots(lunch_data_location):
    temp_lunch_list = []
    lunch_data = load_json(lunch_data_location)
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
    filtered_list = remove_recent_locations(load_lunch_spots(lunch_data_filename), 364)

    return random.choice(filtered_list)


if __name__='__main__':
    DatabaseController.connect()