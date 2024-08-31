train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp
f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
    f_temp = (c_temp * 9 / 5 + 32)
    return f_temp
c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
    return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} newtons of force!")

def get_energy(mass, c = 3 * 10 ** 8):
    return mass * c
bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} joules")

def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The train does {train_work} joules of work over {train_distance} meters \n")


#Write a Python function to calculate the sum all the numbers in a list.
def list_sum(numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum
samp_list = [8, 2, 3, 0, 7]
print("The sum to the samp_list is", list_sum((samp_list)))
#Must utilize double parenthesis so the function knows to use multiple arguments despite having 1 parameter

#Write a Python function to check whether a random number falls within a given range.
import random #imports the ramdom module

def in_range(n):
    if n in range(2, 18):
        print("The number", n, "is in the range")
    else:
        print("The number", n, "is not in the range")
rand_num = random.randrange(1, 30, 3)
in_range(rand_num)


#Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def prime_check(y):
    if y == 1:
        return False #1 is not prime
    elif y == 2:
        return True #2 is prime
    else:
        #itierate through numbers from 2 to (n - 1)
        for x in range(2, y):
            #Check if 'y' is is divisible by 'x' without any remainders
            if y % x == 0:
                #If 'y' is divisible by 'x', it is not prime
                return False
        #If 'y' is not divisible by any number from 2 to (n - 1) it is prime
        return True
print(prime_check(6))

#Write a Python function that checks whether a passed string is a palindrome or not.
def palindrome(word):
    #Initialize pointers to check to check characters from start to finish
    left_pos = 0
    right_pos = len(word) - 1
    #Loop until the pointers meet or cross each other
    while right_pos >= left_pos:
        #Check if the left and right character positions are not equal
        if word[left_pos] != word[right_pos]:
            #If the characters don't match, it isn't a palindrome
            return False
        #Move right pointer to the left and left pointer to the right to continue checking
        left_pos += 1
        right_pos -= 1
    #If the loop finishes without returning a False, we have a palindrome
    return True
print(palindrome("siris"))
