''' Write a program that takes your name as input and prints a personalized greeting along with a calculation of your birth year.'''

name= input("What is your name? ")
age = int(input("And, How old are you? "))

## Now we could define a function that converts the year of birth to ages


birth_year = 2025 - age

print("Hello",name)
print("Wow, you were born in", birth_year, ".") 

