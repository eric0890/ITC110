#pizzaconverter.py
#this file converts the price and size of a pizza into cost per square inch
#note: I tested using 10" diameter and $8 which equals 78.5 square inches divided by 800 cents = 9.82 (rounded)
from math import pi

def main():

    print("This program computes the cost per square inch of pizza. \n")

    #these formulas are needed to calcuate the final formula(s)
    diameter = int(input("Enter the diameter of the pizza (in inches): "))
    price = int(input("Enter the price of the pizza (in dollars): "))
    
    #this equation converts the user inputs and combines it with the formula for area
    areaprice = (pi * ((diameter / 2) ** 2) /(price))
    
    print("\nThe cost is", round(areaprice,2), "cents per square inch.")

main()

