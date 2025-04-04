class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f"The is the {self.name} menu!!! It is available between {self.start_time} and {self.end_time}!\n"

  def bill(self, purchased):
    total = 0
    for item in purchased:
      # check if item is on the menu
      if item in self.items:
        total += self.items[item]
    return total

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f"The address of this franchise is {self.address}!"

  def available_menus(self, time):
    available = []
    for menu in self.menus:
      # if menu is available at given time
      if time >= menu.start_time and time <= menu.end_time:
        available.append(menu)
    return available

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


brunch = Menu("Brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
  }, 11, 16)

early_bird = Menu("Early-Bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
  }, 15, 18)

dinner = Menu("Dinner", {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
  }, 17, 23)

kids = Menu("Kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
  }, 11, 21)

# Recall the "purchased" parameter is a list
#print(brunch.bill(["waffles", "home fries", "coffee"]))
#print(early_bird.bill(["salumeria plate", "mushroom ravioli (vegan)"]))


menus = [brunch, early_bird, dinner, kids]
flagship = Franchise("1232 West End Road", menus)
newInstall = Franchise("12 East Mulberry Street", menus)

#print(flagship.available_menus(12))
#print(newInstall.available_menus(17))

basta = Business("Basta Fazoolin' with my Heart", [flagship, newInstall])

arepas_menu = Menu("Arepas", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
  }, 10, 20)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
arepa = Business("Take a' Arepa", [flagship, newInstall])

print(arepa.franchises[0])
