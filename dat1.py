##Python Program to check if a Number Is Positive Or Negative
#Given an integer input, the objective is check whether the given integer is Positive or Negative.

num = -123
if num > 0:
  print("positive")
elif num < 0:
  print("negative")
else:
  print("null")



#Python Program to Check Whether a Number is Even or Odd
#Given an integer input the objective is to write a Python code to Check Whether a Number is Even or Odd. To do so the main idea is to divide the number by 2 and check if it’s divisible or not. It’s an Even number is it’s perfectly divisible by 2 or an Odd number otherwise.

num = int(input("enter a number:"))
if num%2 == 0:
  print("it is even number")
else:
  print("it is odd number")



#Python Program to Find the Sum of First N Natural Numbers
#Given an integer input of N, the objective is to find the sum of all the natural numbers until the given input integer. To do so we can use different approaches to write the Python code and some such methods are mentioned below


sai = 96

sum = 0
for i in range(sai+1):
  sum+= i
  print(sum)  



 #Python Program to Find the Sum of First N Natural Numbers
#Given an integer input of N, the objective is to find the sum of all the natural numbers until the given input integer. To do so we can use different approaches to write the Python code and some such methods are mentioned below
#formula -> num*(num+1)/2

num = 9
print(num*(num+1)/2)



#Python program to print sum of N natural numbers
#Given an integer value the objective of the code is to sum up all the numbers until the input integer number. To do so we usually use iteration, we iterate through the numbers until the input number is reached while appending the number to the sum variable. Here are some methods to solve the above mentioned problem
                          #OR
                          #Formula -> num*(num+1)/2


num, sum = 6,0
for i in range (num+1):
  sum+= i
  print(sum)




#Find the Sum of Numbers in a given Range in Python
#Given two integer inputs as the range [low , high], the objective is to find the sum of all the numbers that lay in the given integer inputs as interval. In order to do so we usually iterate through the the numbers in the given range and keep appending them to the sum variable. Here are few methods to solve the above mentioned problem in Python Language.

num1,num2 = 3,6
sum = 0
for i in range(num1,num2+1):
  sum+=i
  print(sum)



#Find the Sum of Numbers in a given Range in Python
#Given two integer inputs as the range [low , high], the objective is to find the sum of all the numbers that lay in the given integer inputs as interval. In order to do so we usually iterate through the the numbers in the given range and keep appending them to the sum variable. Here are few methods to solve the above mentioned problem in Python Language.

                        # FORMULA#


  #Formula to Find the Sum of Numbers in an Interval

#The formula to find the sum of n natural numbers is:
#Sum = n * ( n + 1 ) / 2

#Therefore in order to find the sum in a given interval we'll minus the sum of the numbers until the lower range from the whole sum and add an offset as the lowest bound is itself included in the summation. Hence the final formula is :
#Sum = b * ( b + 1 ) / 2 – a * ( a + 1 ) / 2 + a .

num1, num2 = 3, 6
sum = int((num2*(num2+1)/2) - (num1*(num1+1)/2) + num1)
print(sum)




#Find the Greatest of Two Numbers in Python
#Given two integer inputs, the objective is to find the largest number among the two integer inputs. In order to do so we usually use if-else statements to check which one’s greater. Here are some of the Python methods to solve the above mentioned problem.

num1 ,num2 = 3,9
if num1>num2:
  print(num1)
else:
  print(num2)



#Find the Greatest of Two Numbers in Python
#Given two integer inputs, the objective is to find the largest number among the two integer inputs. In order to do so we usually use if-else statements to check which one’s greater. Here are some of the Python methods to solve the above mentioned problem.

num1, num2 = 30 , 59
print(max(num1,num2))




#Find the Greatest of the Three Numbers​ in Python
#Given three integers as inputs the objective is to find the greatest among them. In order to do so we check and compare the three integer inputs with each other and which ever is the greatest we print that number. Here are some methods to solve the above problem.

num1, num2, num3 = 10, 3456,30
if num1>num2 and num1>num3:
  print(num1)
elif num2> num1 and num2 >num3:
  print(num2)
else:
  print(num3)



#Leap Year Program in Python

#Check Whether a Year is a Leap Year or Not in Python
#Given an integer input as the year, the objective is to Check if a Year is a Leap Year or Not in Python Language. To do so we’ll check each condition mentioned below in the blue box. It either of the conditions is satisfied, the year is a leap year. It’s not otherwise. Here are some methods to check whether or not it’s a leap year

leap = 2024
if leap%4 == 0 and leap%100!= 0:
  print("it is leap year")
else:
  print("it is not leap year")




#Leap Year Program in Python

#Check Whether a Year is a Leap Year or Not in Python
#Given an integer input as the year, the objective is to Check if a Year is a Leap Year or Not in Python Language. To do so we’ll check each condition mentioned below in the blue box. It either of the conditions is satisfied, the year is a leap year. It’s not otherwise. Here are some methods to check whether or not it’s a leap year

import calendar
year = int(input("enter a year leap:"))
if calendar.isleap(year):
  print( "it is a leap year")
else:
  print("it is not leap year")