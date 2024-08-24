# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#Assigns the number of times 2 appears to the variable
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#Assigns the length of the toppings list to the variable
#"len()" is a function, not a list method
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizzas!")

pizzas_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]
print(pizzas_and_prices, "\n")

#Sorts the 2D list
pizzas_and_prices.sort()
print(pizzas_and_prices)

#Stores the first element 
cheapest_pizza = pizzas_and_prices[0]
print(cheapest_pizza)

#Stores the last element
priciest_pizza = pizzas_and_prices[-1]
print(priciest_pizza)

#Removes the last element
pizzas_and_prices.pop()
print(pizzas_and_prices)

#Adds a new element to the list
pizzas_and_prices.insert(4, [2.5, "peppers"])
print(pizzas_and_prices)

#Stores the first 3 elements in the list
three_cheapest = pizzas_and_prices[:-3]
print(three_cheapest)
