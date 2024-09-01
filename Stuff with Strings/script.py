#Practice doing things with strings

#Accessing strings
var1 = 'Warframe'
var2 = "xel'Naga"

print(var1[3])

#Slicing strings
print(var2[1:5]) #Prints the characters from indices 1-5 (excluding 5). prints el'N
print(var1[2:7]) #prints rfram
print(var1[:3]) #Prints only the first 3 characters of the string, prints War
print(var2[3:]) #Prints everything after the first 3 characters of the string
print(var1[:-3]) #Prints everything until the last 3 characters
print(var2[-3:]) #Prints only the last 3 characters
print(var1*3) #Prints 3 copies of the same string
print(type(var1), "\n")

#Some built-in string methods
print(var2.capitalize()) #capitalizes the first character in the string
print(var2.casefold()) #converts all uppercase to lowercase
print(var2.count("a")) #counts the occurences of a character/s in a string
print(var2.find("a")) #prints the index of the first occurence of a character/s
print(var2.index("a")) #same as find()
print(var2.replace("a", "y")) #replaces every occurence of "a" with "y"
print(var2.replace("y", "a"))
print(var1.swapcase()) #inverts the case of all letters in the string
print(var2.upper()) #converts all lowercase into upper case

#Built in functions
print(len(var1))
print(max(var1))
print(min(var1))
