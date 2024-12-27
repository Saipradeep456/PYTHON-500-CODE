#Reverse a Number in Python


#Find the Reverse of a Number in Python Language
#We need to write a python code to reverse the given integer and print the integer. The typical method is to use modulo and divide operators to break down the number and reassemble again in the reverse order. Here are some of the methods to solve the above mentioned problems,

num = int(input("enter a number:"))
temp = num      # A backup of the original number is stored in temp (not used further in this code but can be helpful for comparison later).
reverse = 0   #This variable will store the reversed number as the loop progresses.

while num > 0:      #The while loop will continue as long as num is greater than 0. It processes each digit of num from right to left.
    remainder = num % 10     # The modulo operator (%) is used to get the last digit of num
    reverse = (reverse*10)+remainder    #Multiply the current value of reverse by 10 to shift its digits to the left.  Add the extracted remainder to the shifted value.

    num = num//10     #Use integer division (//) to remove the last digit from num.

print(reverse)


#Reverse a Number in Python


#Find the Reverse of a Number in Python Language
#We need to write a python code to reverse the given integer and print the integer. The typical method is to use modulo and divide operators to break down the number and reassemble again in the reverse order. Here are some of the methods to solve the above mentioned problems,

number = int(input("enter a number :"))
print(str(number)[::-1])


#Palindrome Program in Python
#Check Whether or Not the Number is a Palindrome in Python Language
#Given an integer input the objective is to check whether or not the given integer number as an input is palindrome or not.

num = int(input("enter a number:"))
temp = num 
reverse = 0
while temp> 0:
    remainder = temp % 10
    reverse = (reverse*10)+remainder
    temp= temp//10
if num == reverse:
    print("it is palindrome number")
else:
    print("it is not palindrome number")



#Palindrome Program in Python
#Check Whether or Not the Number is a Palindrome in Python Language
#Given an integer input the objective is to check whether or not the given integer number as an input is palindrome or not.

number = input("enter a number :")
reverse = number[::-1]
if reverse == number:
    print("palindrome")
else:
    print("not palindrome")