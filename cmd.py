import sys
import time
from app import pick_a_spot

# define your ridiculous slow printing function
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n")
    time.sleep(0.5)

def run_app():
    delay_print("Welcome to Lunch Roulette.")
    delay_print("For those about to eat, we salute you!")
    delay_print("I hope you're in the mood for something good.")
    delay_print("Because I have a good feeling about this month.")
    delay_print("And your restaurant this month is...!")

    session_data = pick_a_spot()
    delay_print(session_data.name)

    # would you like to respin?
    delay_print("Good choice right?")
    delay_print("I supposed I could give it another go if you like.")
    delay_print("Want me to pick again? [Yes/No]")

    q = input("> ")
    if q.upper() == "YES":
        delay_print("Very well.")
        delay_print("LET'S DO THIS!")
        delay_print("Please enjoy.....")

        session_data = pick_a_spot()
        delay_print(session_data.name)

        delay_print("I hope you feel good about the life choices you made that landed you here.")

    elif q.upper() == "NO":
        delay_print("Fair enough.")
        response_for_no_respin = "I hope you enjoy your visit to {} then.".format(session_data.name)
        delay_print(response_for_no_respin)
    else:
        delay_print("Learn how to type. We're done here.")
    pass

run_app()