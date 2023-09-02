#!/usr/bin/python3 


#Funtion to calculate temperature in Fahrenheit 

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit 


#Input temperature in Celsius 
celsius_temperature = float(input("Enter temperature in Celsius:"))


#Calculate temperature in Fahrenheit 
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)


#Display the result 
print (f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit")

