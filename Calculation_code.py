#!/usr/bin/python3 


# This is my third (3rd) assignment2

#Owner: Moshood

print  ("****************Area of a Circle******************")
Radius = float (input("Please enter the area of a circle: "))

Area = 3.142 * (Radius ** 2)

print (Area)



print ("******************Simple Interest********************")
Principal = float(input("Please enter the principal: "))
Rate_of_Interest = float(input("Please enter the interaest rate: "))
Time = float(input("Please enter the time period (in years): "))

Simple_Interest = (Principal * Rate_of_Interest * Time) // 100

print (Simple_Interest)




print ("*******************Area of a Triangle*******************")
Base = float(input("Please enter the length of the base: "))
Height = float(input("Please enter the height: "))

Area_of_Triangle = Base * Height // 2

print (Area_of_Triangle)
