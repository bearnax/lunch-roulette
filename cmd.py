import sys
import time
import app
from collections import namedtuple

# define your ridiculous slow printing function
def delay_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n")
    time.sleep(0.5)

# ======================================================================
#                                                      PREPARE THE DATA
# ======================================================================

locations = app.load_lunch_spots(app.lunch_data_filename)







# ======================================================================
#
# ======================================================================

Command = namedtuple("Command", ["title", "function"])

def view_restaurants():
    for i in locations:
        print(i.name)

def add_restaurant():
    restaurant_to_add = input("> ")
    app.add_location(restaurant_to_add, locations)

def exit():
    return 0

command_options = [
    Command("View Restaurants", view_restaurants),
    Command("Add a Restaurant", add_restaurant),
    Command("Remove a Restaurant", "rmv res"),
    Command("View Players", "view pl"),
    Command("Add a Player", "add p"),
    Command("Remove a Player", "rmv p"),
    Command("Exit", exit)
]

def welcome():
    delay_print("Welcome to Lunch Roulette.")
    delay_print("For those about to eat, we salute you!")
    delay_print("I hope you're in the mood for something good.")
    delay_print("Because I have a good feeling about this month.")

def command_interface():
    print("What would you like to do?")
    counter = 1
    for i in command_options:
        print("{}. {}".format(counter, i.title))
        counter += 1
    command = input("> ")
    for i in command_options:
        if i.title.lower() == command.lower():
            if i.function == exit:
                return 0
            else:
                i.function()
                return command_interface()


command_interface()


# def run_app():
#     delay_print("And your restaurant this month is...!")
#
#     session_data = pick_a_spot()
#     delay_print(session_data.name)
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
#         delay_print("Please enjoy.....")
#
#         session_data = pick_a_spot()
#         delay_print(session_data.name)
#
#         delay_print("I hope you feel good about the life choices you made that landed you here.")
#
#     elif q.upper() == "NO":
#         delay_print("Fair enough.")
#         response_for_no_respin = "I hope you enjoy your visit to {} then.".format(session_data.name)
#         delay_print(response_for_no_respin)
#     else:
#         delay_print("Learn how to type. We're done here.")
#     pass
