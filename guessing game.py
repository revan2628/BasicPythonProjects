import random
import time
import webbrowser

def game():
    min_num = input("please enter the minimum number for the range: ")
    min_num = min_num.replace(" ", "")
    while min_num == "" or min_num.isdigit() == False:
        webbrowser.open("https://youtu.be/edl_M_-RHzM?si=o3fMRQcHya-nVb9S")
        min_num = input("please enter the minimum number for the range: ")

    max_num = input("Now enter the maximum number: ")
    max_num = max_num.replace(" ", "")
    while max_num == "" or max_num.isdigit() == False:
        webbrowser.open("https://youtu.be/edl_M_-RHzM?si=o3fMRQcHya-nVb9S")
        max_num = input("Now enter the maximum number: ")

    min_num = int(min_num)
    max_num = int(max_num)

    while min_num > max_num:
        print("Extralu dengakunda cheppindhi cheyyi")
        min_num = input("please enter the minimum number for the range: ")
        while min_num == "" or min_num.isdigit() == False:
            webbrowser.open("https://youtu.be/edl_M_-RHzM?si=o3fMRQcHya-nVb9S")
            min_num = input("please enter the minimum number for the range: ")
        min_num = int(min_num)

        max_num = input("Now enter the maximum number: ")
        while max_num == "" or max_num.isdigit() == False:
            webbrowser.open("https://youtu.be/edl_M_-RHzM?si=o3fMRQcHya-nVb9S")
            max_num = input("Now enter the maximum number: ")
        max_num = int(max_num)

    number = random.randint(min_num, max_num)
    tries = 1
    num = input(f"Guess a number between {min_num} and {max_num}: ")

    while num == "" or num.isdigit() == False:
        webbrowser.open("https://youtu.be/edl_M_-RHzM?si=o3fMRQcHya-nVb9S")
        num = input(f"Please enter a number between {min_num} to {max_num}: ")

    num = int(num)

    while num < min_num or num > max_num:
        num = input(f"Please enter an integer in the range {min_num} to {max_num}: ")
        while num == "" or num.isdigit() == False:
            webbrowser.open("https://youtu.be/edl_M_-RHzM?si=o3fMRQcHya-nVb9S")
            num = input(f"Please enter a number between {min_num} to {max_num}: ")
        num = int(num)
    while num < number:
        num = input("Nope! you guessed lower, try something higher than what you've previously guessed: ")
        while num == "" or num.isdigit() == False:
            webbrowser.open("https://youtu.be/edl_M_-RHzM?si=o3fMRQcHya-nVb9S")
            num = input("Please enter a valid number: ")
        num = int(num)
        tries += 1

    while num > number:
        num = input("Nope! you guessed higher, try something lower than what you've previously guessed: ")
        while num == "" or num.isdigit() == False:
            webbrowser.open("https://youtu.be/edl_M_-RHzM?si=o3fMRQcHya-nVb9S")
            num = input("Please enter a valid number: ")
        num = int(num)
        tries += 1


    else:
        print("you've got it!!!!")
        print(f"... in {tries} tries")

game()
again = input("Do you want to play the game again? (Y/N)").upper()


while again == "Y":
    game()
    again = input("Do you want to play the game again? (Y/N)").upper()

if again == "N":
    print("Okayy, have a great day ;)")
    time.sleep(2)

else:
    print("cheppindhi cheyyochu kadhara erripuka")
    webbrowser.open("https://youtu.be/85-hoGOBzTQ?si=bCZViWaeeKkvBcUA")
    input("enter nokki saavu")
    

