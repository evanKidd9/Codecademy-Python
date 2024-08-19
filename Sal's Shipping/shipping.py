weight = 99
#Ground shipping
if weight <= 2:
  ground_cost = weight * 1.50 + 20 
  ground_premium = 125 
  drone_cost = weight * 4.50
elif weight >=2 and weight <= 6:
  ground_cost = weight * 3.00 + 20 
  ground_premium = 125 
  drone_cost = weight * 9.00
elif weight >= 2 and weight <=10:
  ground_cost = weight * 4.00 + 20 
  ground_premium = 125 
  drone_cost = weight * 12.00
elif weight >= 10:
  ground_cost = weight * 4.75 + 20 
  ground_premium = 125 
  drone_cost = weight * 14.25

print(ground_cost)
print(ground_premium)

#Drone Shipping 
print(drone_cost)
