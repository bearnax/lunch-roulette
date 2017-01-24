import random
import numpy as np

lunchplace = {
    "name" : "",
    "price" : "", #$, $$, $$$, $$$$, $$$$$
    "cuisine" : "",
    "street-address" : "",
    "city" : "",
    "zip" : ""
}

restaurant_pool = {
    "r1" : {
        "name" : "El Ray del Taco",
        "price" : "$",
        "cuisine" : "Mexican",
        "street-address" : "5288 Buford Hwy NE",
        "city" : "Doraville",
        "zip" : "30346"
    },
    "r2" : {
        "name" : "Super H Mart",
        "price" : "$",
        "cuisine" : "Asian",
        "street-address" : "B, 6035 Peachtree Rd",
        "city" : "Doraville",
        "zip" : "30360"
    },
    "r3" : {
        "name" : "Atlanta Chinatown",
        "price" : "$$",
        "cuisine" : "Asian",
        "street-address" : "5383 New Peachtree Rd",
        "city" : "Atlanta",
        "zip" : "30341"
    },
    "r4" : {
        "name" : "Mellow Mushroom",
        "price" : "$$",
        "cuisine" : "Pizza",
        "street-address" : "5575 Chamblee Dunwoody Rd",
        "city" : "Atlanta",
        "zip" : "30338"
    }
}

rawlist = [
    "H Mart",
    "El Ray del Taco",
    "Chinese Cultural Center",
    "Mellow Mushroom",
    "Heirloom BBQ",
    #too far "Fat Matt's",
    "Pho and/or Bahn Mis",
    "Costco",
    "Eclipse di Luna",
    "Desta",
    "Cho Dang Tofu House (Korean BBQ)",
    "Flying Biscuit",
    "Waffle House",
    "ShakeShack",
    "Olive Garden",
    "Marlow's Tavern",
    "Superica",
    "Greek",
    "Chick-fil-a",
    #too far "Australian Bakery",
    "Takorea",
    "Taco Veloz",
    "McDonald's",
    #too far "Purnima",
    "Teela Taqueria",
    "Royal China, Dim Sum",
    "CowFish",
    "J's Mini HotPot Deluxe",
    "Nori Nori",
    #too far "Sushi Kiko"
]

# print len(rawlist)
# rand_item = random.choice(rawlist)
# print rand_item
# print len(rawlist)
#
# numpy_item = np.random.choice(rawlist,size=None,replace=False)
# print numpy_item
# print len(rawlist)

print ".\n.\n.\n.\n.\n.\n.\n.\n."
print np.random.choice(rawlist).upper()
print "\n"


# NEW FEATURES BASED ON GOOGLE SHEET AND MAPS API

# Import the spreadsheet and create a data table using pandas

# FUNCTION: Pick a restaurant within the users driving limits
    # Remove the restaurants that are too far away
        # Ask the user how far away (in minutes) they're willing to go to eat
        # Use the Maps API to filter out anything greater than distance entered
        # Return a list of restaurants to pick from
            # Show the user the list of what was excluded
            # Pick a random restaurant from the remaining pool
            # Show the user the restaurant name, address, cuisine, $$, and driving distance with and without traffic for the current time.
