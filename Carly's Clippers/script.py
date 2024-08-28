hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices: total_price += price #Elegant one line loop
average_price = total_price / len(prices)
print("Average haircut price:", average_price)

#List comprehension to cut the prices in "prices" by 5
new_prices = [price - 5 for price in prices]
print("New prices:", new_prices)
total_revenue = 0

#Iterates through the indices of hairstyles and last_week lists
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
    
average_daily_revenue = total_revenue / 7

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Haircuts under 30:", cuts_under_30)