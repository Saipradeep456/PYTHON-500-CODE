#Reverse a Number in Python


#Find the Reverse of a Number in Python Language
#We need to write a python code to reverse the given integer and print the integer. The typical method is to use modulo and divide operators to break down the number and reassemble again in the reverse order. Here are some of the methods to solve the above mentioned problems,

num = int(input("enter a number:"))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse*10)+remainder
    num = num//10
print(reverse)
