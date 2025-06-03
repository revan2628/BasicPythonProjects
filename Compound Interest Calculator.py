import time
import sys

def quit(variable):
    if variable == "q":
        print("have a great day :)")
        time.sleep(1.7)
        sys.exit()

def restart(variable):
    if variable == "r":
        calculator()



def digit_check(variable):
    while str(variable).isdigit() == False:
        variable = input("Please enter a valid number: ")
        quit(variable)
        restart(variable)
    return int(variable)



def calculator():
    initial = input("Please enter the amount borrowed/lent: ")
    quit(initial)
    restart(initial)
    initial = initial.replace(" ", "").replace(",", "")
    digit_check(initial)

    interest = input("What is the Annual Interest Rate? (Note: please enter til 2 digits after the decimal point, ex: 16.00%, 12.33%): ")
    quit(interest)
    restart(interest)
    interest = interest.replace(" ", "").replace("%", "").replace(".", "")
    digit_check(interest)
    interest = int(interest)/10000

    period = input("How many times does the interest get compounded per year?")
    quit(period)
    restart(period)
    period = period.replace(" ", "")
    digit_check(period)
    period = int(period)

    time = input("How many years is the tenure? (Note: please enter til 2 digits after the decimal point, ex: 10.00, 9.45, 8.25 ): ")
    quit(time)
    restart(time)
    time = time.replace(" ", "").replace(".", "")
    digit_check(time)
    time = int(time)/100

    final = initial*(1 + (interest/period))**(period*time)
    print(f"The total amount that you would be paying after {time} years is {final:.2f} Rupees.")

calculator()
again = input("Would you like me to calculate anything else?(Y/N): ").upper()

while again == "Y":
    print("Okay :)")
    time.sleep(1)
    calculator()
    again = input("Would you like me to calculate anything else?(Y/N): ").upper()

if again == "N":
    print("Okay, Have a great day <3")
    time.sleep(2)
    sys.exit()