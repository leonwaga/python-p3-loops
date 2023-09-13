#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print (count)
        count -= 1
    print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    square_integers = [x ** 2 for x in int_list]
    return square_integers

int_list = [1, 2, 3, 4, 5]
result = square_integers(int_list)
print (result)
    
    

def fizzbuzz():
    for number in range (1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print ("FizzBuzz")
        elif number % 5 == 0:
            print ("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)

fizzbuzz()


    
