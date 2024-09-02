from datetime import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_travel_message

#Sets the current year
current_time = dt.today().year
print(current_time)

#Sets the base cost for time traveling
base_cost = Decimal("1000.00")
current_year = Decimal(current_time)

#Generates a random year between the current year and the year 10000. Converted to int because randint must take integers as inputs
rand_year = randint(int(current_year), 10000)
cost_multiplier = abs(current_year - rand_year)

#To get a cost proportional to the years traveled
timetravel_cost = base_cost * cost_multiplier

#Rounds the final cost to 2 decimal places
final_cost = round(timetravel_cost, 2)
destinations = ["Norway", "Sweden", "Canada", "Alaska", "Argentina", "Saudi Arabia", "Finland"]

#Randomly chooses a place from the list
rand_dest = choice(destinations)

print(generate_time_travel_message(rand_year, rand_dest, final_cost))
