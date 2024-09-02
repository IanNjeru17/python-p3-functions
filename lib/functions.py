#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name ="ian"):
    print(f"Hello, {name}!")
greet()

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()          
greet_with_default("karukenya") 

def add(num1, num2):
    return num1 + num2
print(add)

def halve(number):
    return number/2
print(halve)
