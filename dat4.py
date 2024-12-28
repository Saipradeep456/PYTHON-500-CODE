#Armstrong Number in Python
#Check Whether a Given Number is an Armstrong Number or Not
#Given an integer input, the objective is to check whether or not the given input variable is an Armstrong number. In order to do so, we check whether the sum of the digits of each number to the power the length of the number is equal to the number itself or not. If the number is the same as the original, it’s an Armstrong number. Mentioned below are a few of the Methods used to solve this problem

def is_armstrong(number):
  num_str =str(number) 
  num_digits = len(num_str)

  Armstrong_sum = sum(int(digit)**num_digits  for digit in num_str)
  return Armstrong_sum == number

sai = int(input("enter a number:"))
if is_armstrong(sai):
  print("it is amstrong number")
else:
  print("it is not amstrong numer")




#Find the Armstrong Numbers between Two Intervals using Pytho

#Find the Armstrong Numbers in a given Range in Python
#Given two integer inputs as intervals high and low, the objective is to write a python code to check if the numbers lying within the given interval are Armstrong Numbers or not.

#An Armstrong number or a Narcissistic number is any number that sums up itself when each of its digits is raised to the power of a total number of digits in the number. Let us try to understand this through the below example,

#abcd… = an + bn + cn + dn + …
#Where n is the order(length/digits in number)
#Let’s look at some examples of Armstrong Numbers.
def sai_sri(number):
  num_str = str(number)
  num_digits = len(num_str)
  armstron_sum = sum(int(digit)**num_digits for digit in num_str)
  return armstron_sum == number

def range_number(start,end):
  armstrong_number =[]
  for i in range (start,end+1):
    if sai_sri(i):
      armstrong_number.append(i)
  return armstrong_number

start = int(input("Enter the start of the range:"))
end = int(input("Enter the end of the rang:"))
result = range_number(start,end)

if result:
  print(f"armstong number b/w {start} and {end} :{result}")
else:
   print(f" no armstong number b/w {start} and {end}")