import time
import json
import datetime
import numpy
import roulette as rl
import chat


''' CREATE GLOBAL VARIABLES & CREATE SOME THE PICKS '''
first_pick = rl.lunch_dict['locations'][rl.select_random_restaurant()]['name']
print first_pick
second_pick = ""





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
#     second_pick = lunch_dict['locations'][rl.select_random_restaurant()]['name']
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
