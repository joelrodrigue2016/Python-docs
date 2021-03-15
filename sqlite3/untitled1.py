# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 11:11:18 2020

@author: 18134
"""

# def raise_to_power(base_num, pow_num):
#     result  = 1
#     for   index in range(pow_num):
#           result = result * base_num
#     return result

# # A =  str(input("enter the first number: "))
# # B =  str(input("power: "))


# A =  2
# B =  2




# # print(raise_to_power(A,B))   


# number_grid = [
#       [1,2,3],
#       [4,5,6],
#       [7,8,9]
      
# ]
# print(number_grid[2][0])


from Student import Student

Student1 = Student("John", "Business", 3.1, False)
Student2 = Student("Joel", "Engineering", 3.8, False)
Student3 = Student("Jim", "Business", 4.0, False)
Student4 = Student("Pam", "Arts", 2.1, True)
print(Student1.name)
print(Student2.name)
print(Student3.name)
print(Student4.name)

print(Student1.on_honor_roll())
print(Student2.on_honor_roll())
print(Student3.on_honor_roll())
print(Student4.on_honor_roll())
