#Prime Number Program in Python
#Given an integer input for a number, the objective is to check whether or not the number is a prime. In order to do so we keep checking with all the numbers until square root of the number itself for factors of the number input. If found any, the number is not a prime. Here are some of the methods given to solve the above mentioned problem in python language
def sai_sri(darling):
  if darling<=1:
    return false
  for i in range(2,int(darling**0.5)+1):
    if darling % i == 0:
      return False
    return True

number = int(input("enter a  prime number:"))

if sai_sri(number):
  print("It is a prime number")
else:
  print("It is not prime number")




#Python Program to Print Prime Numbers In a Given Range
#Given two integer variables for range, the objective is to check for all the prime number that lay in the given interval. The two input integers will act as the interval limits low and high. In order to check which iterating, we’ll use nested loops. The outer loop will iterate through the numbers while the inner loop will check for Prime. Here are some of the methods used to solve the above mentioned problem in python language

def sai_pradeep(heartuu):
    if heartuu <= 1:
        return False
    for i in range(2, int(heartuu**0.5) + 1):
        if heartuu % i == 0:
            return False
    return True

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

print(f"Prime numbers between {start} and {end} are:")
for number in range(start, end + 1):
    if sai_pradeep(number):
        print(number, end=" ")





#Sum of Digits of a Number in Python
#Given a number as an input the objective is to calculate the sum of the digits of the number. We first break down the number into digits and then add all the digits to the sum variable. We use the following operators to break down the string,

#Modulo operator %: We use this operator to extract the digits from the number.
#Divide operator /: We use this operator to shorten the number after the digit has been extracte

number =input("enter a number")
sum = 0
for i in number:
  sum+=int(i)
print(sum)