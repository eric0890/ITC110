# distanceconverter.py
# convert kilometers (input) to miles (output)

def main():
    print("This program converts kilometers to miles.")
    kilometers = int(input("Enter the distance in kilometers: "))
    
    #processing math
    miles = kilometers * .621371
    
    #final conversion output of above processes
    print (kilometers, "kilometers equals", round(miles,1) ,"miles.")

main()

