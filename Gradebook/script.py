last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
#List combining subjects and grades
gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]

#Adds computer science class and grade
gradebook.append(["computer science", 100])

#Adds visual arts class and grade
gradebook.append(["visual arts", 93])

#Increase visual arts grade by 5
gradebook[5][1] += 5

#Removes grade value in visual arts
gradebook[2].remove(85)

#Adds Pass to visual arts class grade
gradebook[2].append("Pass")

#Combines the 2 lists
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
