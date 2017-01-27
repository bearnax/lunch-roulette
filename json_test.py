import json
import datetime

with open('participants.json') as json_data:
    d = json.load(json_data)

print "\nLarry old status"
print d['people']['larry']['respin']['available']
print d['people']['larry']['respin']['date-used']

d['people']['larry']['respin']['available'] = False
d['people']['larry']['respin']['date-used'] = "2016-08-09"

print "\nLarry new status"
print d['people']['larry']['respin']['available']
print d['people']['larry']['respin']['date-used']

with open('participants.json', 'w') as json_data:
    json.dump(d, json_data, sort_keys=True, indent=4)

# update the respins in the json file
# if a particpant used their respin and that respin was more than 6 months ago
    # then set the available variable to true
six_months = 365/2

def respin_update():
    for item in d['people']:
        if d['people'][item]['respin']['available'] == False:
            if (datetime.date.today() - datetime.datetime.strptime(d['people'][item]['respin']['date-used'], '%Y-%m-%d').date()).days > six_months:
                d['people'][item]['respin']['date-used'] = ""
                d['people'][item]['respin']['available'] = True

respin_update()
print "\nLarry new NEW status"
print d['people']['larry']['respin']['available']
print d['people']['larry']['respin']['date-used']


# if recieving a user input, ask whether or not the user has a respin available
