#TAKING A VACATION
####################
#Plan Your Trip!
#1.After your previous code, print out the trip_cost( to "Los Angeles" for 5 days with an extra 600 dollars of spending money.

#Don't forget the closing ) after passing in the 3 previous values!


def hotel_cost(nights):
  return 140 * nights
  
print hotel_cost(3)
  
  
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  else:
    return 475
  
  
def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    return cost - 50
  elif days >= 3:
    return cost - 20
  else:
    return cost
  
def trip_cost(city, days, spending_money):
    sum = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) +spending_money
    return sum
    
    
print trip_cost( "Los Angeles",5, 600)