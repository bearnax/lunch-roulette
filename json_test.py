import json

with open('participants.json') as json_data:
    d = json.load(json_data)

print d
print d['people']['amy']['first-name']

print "\nLarry old status"
print d['people']['larry']['respin']['available']
d['people']['larry']['respin']['available'] = False
print "\nLarry new status"
print d['people']['larry']['respin']['available']
