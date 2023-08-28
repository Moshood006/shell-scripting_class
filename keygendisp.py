#!/usr/bin/python3 
import random

name = input("please enter your name: ")
age = input("please enter your age: ")
phone_number = input("please enter your phone number: ")
email_address = input("please enter your email address: ")




print(name) 
print(age)
print(phone_number) 
print(email_address)

#this will generate a random set of numbers as password and print along with the user details 

print("*********************************************************************") 
print("*********************************************************************") 
print("**  *****          *****                                           **") 
print("**    ****************                                             **") 
print("**     **************                                              **") 
print("**    ****************                                             **") 
print("**  ********     ********                                          **") 
print("*********************************************************************") 
print("*********************************************************************") 

user_number= random.randint(1,40)
user_number= [] 

print(name, age, user_number)