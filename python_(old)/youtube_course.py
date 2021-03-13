# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:53:12 2020

@author: Joel Rodriguez
"""

print('     /|')
print('    / |   ')
print('   /  |   ')
print('  /___|')
print('show me the link please ')
print('here you are ')
print('https://www.youtube.com/watch?v=rfscVS0vtbw&list=PLTBeRxkEG6qZBSzS3X0Buh_vWefL1Sisa')
Character_name= "Joel"
Character_age= "32"
print ("There once was a man named " + Character_name + ", ")
print ("he was " + Character_age  + ","  "years old.")
print ('he really liked the name ' + Character_name + "," )
print ("but didn't like being " + Character_age  +  " years old.")
#import pdb
#pdb.set_trace()
#how to change a name
Character_name= "Stephanie Rodriguez"
Character_age= "27"
print ("There once was a woman named " + Character_name + ", ")
print ("she was " + Character_age  + ","  "years old.")
print ('she really liked the name ' + Character_name + "," )
print ("but didn't like being " + Character_age  +  " years old.")
print('she always told her husband to clean up the kitchen, because he was a slob, that did not even know how to spell.')
import numpy as np
from matplotlib import pyplot as plot
time= np.arange(0, 50, 0.002)
amplitude   = np.cos(time)
plot.plot(time, amplitude)

#how to break texts
print("Giraffe Academy")
#or
print("Girafe \n academy")

Phrase=("Girafe academy")
print(Phrase)
#use of concatenation
print(Phrase + "is the greatest thing ever, according to Joel!")
#attach functions to the "phrase"
#for instance in this case you can make the whole string upper cased
print(Phrase.upper())
#the claim can also be tested
print(Phrase.isupper())
#The claim can also be combined 
print(Phrase.upper().isupper())
#How to count the strings
print(len(Phrase))
print(Phrase[0])
print(Phrase[1])
print(Phrase[2])
print(Phrase[3])
print(Phrase.index("acad"))
print(Phrase.replace ("Girafe", "Cat dino Kenny boy"))
name = input("Enter your name: ")
print("Hello " + name + "!")
age = input('enter your age:  ')
weight = input ("How much do you weight"  "(in pounds)" "? ")
print("Hello " + name + "! you are " +  age + " and you weigh " + weight + " pounds.")
print("I always know everything because I asked important questions!!! I mean, seriously that is the only way to know!")


#Basic Calculator

num1 = input ("enter a number: ")
num2 = input ("enter another number: ")
result = float(num1) + float(num2)
print(result)


color= input ("What is your favorite color? ")
plural_noun= input("Enter plural noun: ")
Celebrity = input("Who is your favorite celebrity? ")
print("Roses are " + color )
print(plural_noun + " are blue")
print("I love " + Celebrity + " and so do you!")


friends = ["Antonio", "wayne" ,"Coller" ,"Martin" , "Tash", "Karen", "Jim" , "Angelo"]

print(friends[2:])

friends = ["Antonio", "wayne" ,"Coller" ,"Martin" , "Tash", "Karen", "Jim" , "Angelo"]

print(friends[1:])

lucky_numbers= [4, 8, 16, 23, 55, 90]
print("lucky_numbers")
#friends.extend()
#friends.remove()
#friends.clear() This will clear the entire list
#friends.pop
#friends.append("Ronald")
friends.insert(1, "Kelly")
print(friends)
#print(friends.index("Mike"))
#friends2= friends.copy()

#Tuples
Coordinates = (4,5)


print(Coordinates[0])


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
o= np.linspace(5,8,9)

o2 =np.logspace(1,5,9)
print(o)
print(o2)

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

#get dimension
a.ndim
print(a.ndim)
#get shape
b.shape
print(b.shape)
print(a.dtype)

c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(c)
# the notation is [row,col]
c[1]
print(c[1])
print(c[2])

# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd

num1 = input ("What is your first number? ")
num2 = input ("What is your second number? ")
result = float(num1) * float(num2)
print(result)

i = list(range(np.pi*-2,np.pi/10,np.pi)
j = np.cos(i)

y = Joel
y1 = Rodriguez

print( "If you’re a senior citizen with a serious underlying health condition, this would be a good time to practice common sense and to avoid activities including traveling on a cruise line,’ said @VP."* 1000)




"Roses are red, violets are blue, I like shakira and so do you"




a = input("What is your favorite color? ")
b = input("Plural object: ")
c = input("Favorite artist: ")
print("Roses are" + a, "violets are" + b , "I like" + c "and so do you!")


def raise_to_power(base_num, power_number):
result  = 1
for   index in range(pow_number)
result = result * base_number
return result

print(raise_to_power(2,3))   


