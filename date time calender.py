''' from datetime import date , time , datetime

today = date.today()
now = datetime.now()

print("today's date is ", today)
print("Now, the current time is ", now)

print("date components", today.year , today.month, today.day)'''

"""def cost_hotel(night):
    return 5000*night

def plane_cost(city):
    if "delhi" == city:
        return 7000
    elif "kolkata" == city:
        return 6000
    elif "jaipur" == city:
        return 9000
    elif "punjab" == city:
        return 6500
    
def car_cost(days):
    if days>=7:
        return 1000*days - 1000
    elif days>=3:
        return 1000*days - 700
    else:
        return 1000*days 
    
def trip_cost(city, days , spending_money):
    return car_cost(days) + cost_hotel(days) + plane_cost(city) + spending_money

print("cost of car rental: ", car_cost(5))
print("cost of plane ride: ", plane_cost("jaipur"))
print("cost of hotel room", cost_hotel(6))
print("total trip cost:", trip_cost("jaipur",6, 10000))"""

import random
from datetime import datetime, timedelta  

def get_random_date(start_date, end_date):

    start = datetime.strptime(start_date, "%m/%d/%Y" )
    end = datetime.strptime(end_date, "%m/%d/%Y" )

    delta = (end - start).days

    random_days = random.randint(0, delta)

    random_date = start +timedelta(days= random_days)

    return random_date.strftime("%m/%d/%Y")

print("random date is ", get_random_date("1/1/2025", "12/31/2025"))
