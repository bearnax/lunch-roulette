import json
import numpy

''' IMPORT DATA FROM JSON FILES'''
with open('participants.json') as json_data:
    participant_dict = json.load(json_data)

with open('lunch_locations.json') as json_data:
    lunch_dict = json.load(json_data)

def select_random_restaurant():
    '''return a restaurant at random from the available list'''

    restaurant_list = []
    for i in lunch_dict['locations']:
        if lunch_dict['locations'][i]['available'] == True and lunch_dict['locations'][i]['include'] == True:
            restaurant_list.append(i)
    return numpy.random.choice(restaurant_list)

def respin_reset():
    '''if it's been more than six months since a participant used a respin, reset it'''

    for i in participant_dict['people']:
        if participant_dict['people'][i]['respin']['available'] == False:
            if (datetime.date.today() - datetime.datetime.strptime(participant_dict['people'][i]['respin']['date-used'], '%Y-%m-%d').date()).days > (364/2):
                participant_dict['people'][i]['respin']['date-used'] = ""
                participant_dict['people'][i]['respin']['available'] = True

def lunch_location_availability_reset():
    '''if it's been more than six months since a lunch location was used, reset it'''

    for i in lunch_dict['locations']:
        if lunch_dict['locations'][i]['available'] == False:
            if (datetime.date.today() - datetime.datetime.strptime(lunch_dict['location'][i]['date-selected'], '%Y-%m-%d').date()).days > (364/2):
                lunch_dict['locations'][i]['date-selected'] = ""
                lunch_dict['locations'][i]['available'] = True

def set_restaurant_status():
    '''when a restaurant is selected, set it's availability to false and set the date selected to the day it ran.'''

    if len(second_pick) > 0:
        for i in lunch_dict['locations']:
            if lunch_dict['locations'][i]['name'] == second_pick:
                lunch_dict['locations'][i]['date-selected'] = str(datetime.date.today())
                lunch_dict['locations'][i]['available'] = False

    elif len(first_pick) > 0:
        for i in lunch_dict['locations']:
            if lunch_dict['locations'][i]['name'] == first_pick:
                lunch_dict['locations'][i]['date-selected'] = str(datetime.date.today())
                lunch_dict['locations'][i]['available'] = False




'''EXPORT FINISHED DATA TO JSON'''

with open('participants.json', 'w') as json_data:
    json.dump(participant_dict, json_data, sort_keys=True, indent=4)

with open('lunch_locations.json', 'w') as json_data:
    json.dump(lunch_dict, json_data, sort_keys=True, indent=4)
