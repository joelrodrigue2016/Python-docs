# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:04:52 2020

@author: 18134
"""

# print("Hello world")
# print("what is your name? ")
# name = input()
# print("it is good to meet you " + name)
# print("the length of you name is: ")
# print(len(name), " characters")
# print("what is your age? ")
# age = input()
# print("You will be " + str(int(age)+1) + " in a year")



# name = 'Joel'
# if name == 'Alice':
#    print (" Hi Alice")
# print("Done")

# password = "swordfish"
# if password == "swordfish":
#     print("Access granted.")
# else:
#     print("Wrong password.")

# name = "Bob"
# age = 3000
# if name == "Alice":
#     print("Hi, Alice")
# elif age < 12:
#     print("You are not Alice, kiddo.")
# elif age > 2000:
#     print("unlike you, Alice is not an undead, inmortal vampire")
# elif age > 100:
#     print("You are not Alice, grannie")

# print("Enter name")
# name = input()
# if name != " ":
#     print("Thank you for entering a name. ")
# else:
#     print("You did not enter a name")

# spam = 0
# while spam < 5:
#     print("Hello World, My name is Joel Rodriguez.")
#     spam = spam+1
    
# if spam < 5:
#     print("Hello World, My name is Joel Rodriguez.")
#     spam = spam+1

# name = "Joel"
# while name != "your name":
#     print("please type your name. ")
#     name = input()
      
# print("Thank you")


# while True:
#     print("Please type your name")
#     name= input()
#     if name == "your name":
#         break
# print("Thank you!")
        
# Joel = 0
# while Joel < 90000:
#     Joel = Joel + 1
#     if Joel == 3:
#         continue
#     print("Joel is " + str(Joel))
    
# print("My name is")
# for i in range (50):
#     print("Jimmy five times " + str(i))

# print("My name is")
# for i in range (2,5):
#     print("Jimmy five times " + str(i))
    
# total = 0
# for num in range(101):
#     total = total + num
# print(total)

# import sys
# print("Hello")
# sys.exit()
# print ("good bye")

# def hello ():
#     print("Howdy")
#     print("Howdy!!!")
#     print("Hello there")
    
    
    
# hello()


# "hello has " + str(len("hello")) + " letters in it"




# def plusone (number):
#     return number+1

# newNumber = plusone(8)
# print(newNumber)

# print("cat", "dog", "mouse", sep = "          ")
# print("::::::::::::::::::::::::::::::::::::::::::")

# def Joel():
#     print("Joel is good")
#     print("Joel likes to cook")
#     print("Joel worships God")
#     print("Joel likes to excercise")
#     print("Joel loves his wife")
#     print("Joel watches tv")
    
    
# Joel()
    

# def DowJones ():
#     print("Dow Jones change by day since last Monday:")
#     print("Monday: +1,294")
#     print("Tuesday: -786")
#     print("Wednesday: +1,174")
#     print("Thursday: -970")
#     print("Friday: -257")
#     print("Monday: -2,013")
#     print("Tuesday: +1,167")
#     print("Wednesday: -1,464")
#     print("Thursday: -2,352")
#     print("Friday: +1,982")
#     print("This is just insane... the fastest roller coaster on the planet!")
    
#This code is wrong because eggs have two different functions    
# spam = 42 #global variable

# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0
# spam()
# print("Some code here.")
# print("Some more code here.")
    
# def spam():
#     eggs = "Hello"
#     print("eggs")

# eggs = 42
# spam()   
# print("eggs") 
    
    
# # ------------------------------------------------------
#     #how to import import everything from a library
#  from numpy import *

# cos(5)   #notice that saying np.cos(5) is not needed. it can be done in a straight-forward way

    
# -----------------------------------------------  

# def div42by(divideBy):
#    try:
#     return 42 / divideBy
#    except ZeroDivisionError:
#        print("Error: you tried to divide by zero")

# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))
    

# print("How many cats you have ")
# numCats = input()
# try:
        
#     if int(numCats) >= abs(4):
#          print("wow, you have a lot of cats")
#     else:
#          print("That's not that many cats")
# except ValueError:
#     print("You did not enter an integer")
    
# for i in range(4):
#     print(i)


# for i in [0,1,2,3]:
#     print(i)
    
# list(range(0,100,2))

#very important: This is how lists are created

# supplies = ("pens.", "staplers.","flame-throwers.", "bin.", "binders.")
# for i in range (len(supplies)):
#     print("index " + str(i) + " in supplies is: " + supplies[i] )
    
    
# supplies = ("pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers."
#             , "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", 
#             "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.",
#             "pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.",
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.",
#             "pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.",
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.",
#             "pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.",
#             "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.",
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.",
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.", 
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers."
#             , "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", 
#             "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.",
#             "pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.",
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.",
#             "pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.",
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.",
#             "pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.",
#             "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.",
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.",
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.", 
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers."
#             , "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", 
#             "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.",
#             "pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.",
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.",
#             "pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.",
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.",
#             "pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.",
#             "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.",
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.",
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.", 
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers."
#             , "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", 
#             "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.",
#             "pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.",
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.",
#             "pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.",
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.",
#             "pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.",
#             "flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.",
#             "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.",
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.",
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.","pens.", "staplers.","flame-throwers.", 
#             "bin.", "binders.","pens.", "staplers.","flame-throwers.", "bin.", "binders.","pens.", 
#             "staplers.","flame-throwers.", "bin.", "binders.")
# for i in range (len(supplies)):
#     print("index " + str(i) + " in supplies is: " + supplies[i] )
    
# How password works
# a = "Joel"
# print ("Enter password: ")
# password = input()
# if password == "Joel":
#     print ("Access granted!")
# else:
#     print("Wrong password")
    
# cat = ["fat", "orange", "loud"]
# size = cat [0]
# color = cat[1]
# disposition = cat[2]
# size, color, disposition = cat

# size, color, disposition = "skinny", "black", "quiet"
# a = "AAA"
# b = "BBB"
# a, b = b,a # This swaps the variables and values

# spam  = ["Hello", "hi", "Howdy", "Heyas"]

# spam = ["Zophie","Pooka","Fat-tail","Pooka"]

# spam = ["cat","dog","bat"]
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")
# spam.append("moose")

# spam = ["cat","dog","bat", "elephant"]
# spam.remove("bat")

# spam = ["cat", "bat", "rat", "hat", "cat", "ants"]

# spam.sort()  #How to sort in alpabetical order


# spam = [2,5,1,4,8,9,8,7,5,6,3,2,2,2,4,8,5,6,2,5,8,7,8,9]
# spam.sort()  #How to sort numbers in numerical order

# spam.sort(reverse = True)


# spam = ["a","b","Z","w", "W"]
# spam.sort() # uppper case letters come first

# spam.sort(key = str.lower) #loewr case letters come first


# # How password works
# a = "Joel"
# print ("Enter password: ")
# password = input()
# if password == a:
#     print ("Access granted!")
# else:
#     print("Wrong password")

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("divided by zero")
except ValueError:
    print("wrong value")

    
    
