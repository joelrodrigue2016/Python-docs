# is_male = True
# is_tall = True

# if is_male or is_tall:
#     print("you are a male or tall")
# else:
#     print("you are neither male nor female")
    
    
# is_tall_male = False
# is_tall = False

# if is_male and is_tall:
#     print("you are a male or tall")
# else:
#     print("you are neither male nor female")
    
    
#     is_tall_male = False
# is_tall = False

# if is_male and is_tall:
#     print("you are a male or tall")
# elif is_male and not (is_tall):
#     print("you are a short male")
# elif not ("is_male") and ("is_tall)"):
#     print("you are a short male")
# else:
#     print("you are neither male nor female")
    
    
#def max_num(num1, num2, num3):
#   if num1 >= num2 and num1 >= num3:
#         return num1
#   elif num2 >= num1 and num2 >= num3:
#         return num2
#   else:
#         return num3
#            
#print(max_num(300,40,5))
#    
monthConversions = {
        "Jan" : "January",
        "Feb"  : "February",
        "Mar" : "March",
        "Apr" : "April",
        "May" : "May",
        "Jun" : "June",
        "Jul" : "July",
        "Aug" : "August",
        "Sep" : "September",
        "Oct" : "October",
        "Nov" : "November",
        "Dec" : "December",
}
print(monthConversions["Nov"])

print(monthConversions.get("Dec"))
print(monthConversions.get("ass","Not a valid Key"))


#Another way this can be done is 

monthConversions = {
        0 : "January",
        1 : "February",
        2 : "March",
        "Apr" : "April",
        "May" : "May",
        "Jun" : "June",
        "Jul" : "July",
        "Aug" : "August",
        "Sep" : "September",
        "Oct" : "October",
        "Nov" : "November",
        "Dec" : "December",
}
print(monthConversions[0])

print(monthConversions.get(1))
print(monthConversions.get("9","Not a valid Key"))



# While loop is a structure in Python

#i = 1
#while i  <= 10:
#    print(i)
#    i= i+1
#print("Done with loop")    




#for letter in "Giraffe Academy":
#    print(letter)
#    
##    
##friends = ["Jim","Karen","Kevin"]  
##for friend in  friends:
##    print(friend)
##    
##   
##for index in range(len(friends)):
##    print(index)
##    
##    
##    for index in range(5):
##        if index == 0:
##            print("first iteration")
##        else:
##            print("not first")
##            
#            
#            
##def raise_to_power(base_num, pow_num):
##    result = 1
##    for index in range(pow_num):
##        result = result * base_num
##    return result 
##print(raise_to_power(9,2))
##    
#
#number_grid = [
#        [1,2,3],
#        [4,5,6],
#        [7,8,9],
#        [0]
#]
#for row in number_grid:
#    print(row)
#
#    
#
#
#number_grid = [
#        [1,2,3],
#        [4,5,6],
#        [7,8,9],
#        [0]
#]
#for row in number_grid:
#    for col in row:
#        print(col)
#        
#        
#        
## Build a translator
#        
#def translate(phrase):
#    translation = " "
#    for letter in phrase:
#        if letter in "A E I O U a e i o u":
#            translation = translation + "g"
#        else:
#            translation =  translation + letter
#    return translation
#print(translate(input("enter a phrase: ")))
    

#Try except: How to catch errors
try: 
   number = int(input("Enter a number: "))
   print(number)
except:
   print("invalid input")



try: 
   number = int(input("Enter a number: "))
   print(number)
except ZeroDivisionError:
    print("you cannot divide by zero")
except ValueError:
   print("invalid input")







