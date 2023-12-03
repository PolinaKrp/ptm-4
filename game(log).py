import logging
import random
import shutil
from time import sleep

from emoji import emojize
from simple_colors import *


def intro(): 
    """ 
    Function to print the basic introduction about the game 
    """ 
    columns = shutil.get_terminal_size().columns 
 
    print(magenta("SNAKE (🐍) WATER (💧) GUN (🔫)".center(columns))) 

    sleep(1.5) 

    print(cyan("GAME DEVELOPED BY - 👑 AKSHAT DODHIYA 👑".center(columns))) 
 
    sleep(2) 
    logger.info("the beginning of the game: success")

intro()

computer_choice, user_choice = "", ""  
computer_points, user_points, flag, chance = 0, 0, 0, 0 
replay = ""  


def choices():
    """
    This function takes input of user's choice and also takes random input from the computer from list 'options'
    """
    global computer_choice, user_choice  
    options = ["Snake", "Water", "Gun"]  
    computer_choice = random.choice(options)  

    print("Choose:\t\tS for", emojize(":snake:"),
          "\t\tW for", emojize(":droplet:"),
          "\t\tG for", emojize(":pistol:"))  # Printing options for user to select
    user_choice = input().lower()  # storing input of the user in lower case 


def results():
    """
    This function calculates points of both computer and user and
     it also prints whether the user won or lost in that chance and flag value is also handled in this function
    """
    global computer_points, user_points, flag
    flag = 0
    index = 0
    if computer_choice == roles[index]:
        if user_choice == roles[index][index] or user_choice == roles[index]:
            print(yellow("AWWW...!!"), emojize(":neutral_face:"),
                  yellow("\nTWO SNAKES HAD BITTEN EACH OTHER :/"))
            logger.info(
                "the user chose " + f'{roles[index]}'
                + " the computer chose " + f'{roles[index]}')
        elif user_choice == roles[index + 1][index] or user_choice == roles[index + 1]:
            print(red("NOOO...!!"), emojize(":crying_face:"),
                  red("\nTHE SNAKE DRANK YOUR WATER :("))
            logger.info(
                "the user chose " + f'{roles[index + 1]}'
                + " the computer chose " + f'{roles[index]}')
            computer_points += 1
        elif user_choice == roles[index + 2][index] or user_choice == roles[index + 2]:
            print(green("YEAH...!!"), emojize(":victory_hand:"),
                  green("\nYOU SHOT THE SNAKE BY GUN  :)"))
            logger.info(
                "the user chose " + f'{roles[index + 2]}'
                + " the computer chose " + f'{roles[index]}')
            user_points += 1
        else:
            print("!!कृपया सही विकल्प चुनें!!")
            logger.warning("the user entered the selected item incorrectly")
            flag = 1
    elif computer_choice == roles[index + 1]:
        if user_choice == roles[index][index] or user_choice == roles[index]:
            print(green("YEAH...!!"), emojize(":victory_hand:"),
                  green("\nYOUR SNAKE DRANK THE WATER :)"))
            logger.info(
                "the user chose " + f'{roles[index]}'
                + " the computer chose " + f'{roles[index + 1]}')
            user_points += 1
        elif user_choice == roles[index + 1][index] or user_choice == roles[index + 1]:
            print(yellow("AWWW...!!"), emojize(":neutral_face:"),
                  yellow("\nWATER IS INCREASED :/"))
            logger.info(
                "the user chose " + f'{roles[index + 1]}'
                + " the computer chose " + f'{roles[index + 1]}')
        elif user_choice == roles[index + 2][index] or user_choice == roles[index + 2]:
            print(red("NOOO...!!"), emojize(":crying_face:"),
                  red("\nYOUR GUN SANK INTO THE WATER :("))
            logger.info(
                "the user chose " + f'{roles[index + 2]}'
                + " the computer chose " + f'{roles[index + 1]}')
            computer_points += 1
        else:
            print("!!कृपया सही विकल्प चुनें!!")
            logger.warning("the user entered the selected item incorrectly")
            flag = 1
    elif computer_choice == roles[index + 2]:
        if user_choice == roles[index][index] or user_choice == roles[index]:
            print(red("NOOO...!!"), emojize(":crying_face:"),
                  red("\nYOUR SNAKE WAS SHOT BY THE GUN :("))
            logger.info(
                "the user chose " + f'{roles[index]}'
                + " the computer chose " + f'{roles[index + 2]}')
            computer_points += 1
        elif user_choice == roles[index + 1][index] or user_choice == roles[index + 1]:
            print(green("YEAH...!!"), emojize(":victory_hand:"),
                  green("\nYOUR WATER HAD SUNK THE GUN INTO IT :)"))
            logger.info(
                "the user chose " + f'{roles[index + 1]}'
                + " the computer chose " + f'{roles[index + 2]}')
            user_points += 1
        elif user_choice == roles[index + 2][index] or user_choice == roles[index + 2]:
            print(yellow("AWWW...!!"), emojize(":neutral_face:"),
                  yellow("\nTWO GUNS FIRED AT EACH OTHER :/"))
            logger.info(
                "the user chose " + f'{roles[index + 2]}'
                + " the computer chose " + f'{roles[index + 2]}')
        else:
            print("!!कृपया सही विकल्प चुनें!!")
            logger.warning("the user entered the selected item incorrectly")
            flag = 1


def replay_game():
    """
    Function to ask and store the choice of the user for replaying the game
    """
    while 1: 
        logging.info("DO YOU WANT TO PLAY AGAIN ? \nENTER Y FOR YES AND N FOR NO")
        global replay  
        replay = input().lower() 

        if replay == "y" or replay == "yes":
            break  
        elif replay == "n" or replay == "no":
            break 
        else:
            logger.warning(
                f"invalid value has been entered for the repetition of the games")
            print(red("Please enter a valid input only"))
            continue  

while 1:  
    computer_points, user_points, flag, chance = 0, 0, 0, 0  
    computer_choice, user_choice, replay = "", "", ""  

    try:
        n = int(input("HOW MANY CHANCES DO YOU WANT TO PLAY ?\n"))
        if n < 1:
            print(red('Please enter only natural number', 'bold'))
            continue

    except Exception as e:
        print(red('Please enter only natural number', 'bold'))
        continue

    while chance < n: 
        choices() 
        results() 
        if flag == 0: 
            chance += 1

    print("\n\t\t\tYOUR SCORE :", user_points)
    print("\n\t\t\tCOMPUTER'S SCORE :", computer_points)         
    
    if computer_points > user_points:
        print(red("\n\t\t\tYOU LOST THE GAME !!"),
                emojize(":loudly_crying_face:"), red("YOU LOST THE GAME"))
        logger.info("output of results: computer won")
    elif user_points > computer_points:
        print(green("\n\t\t\tHURRAH !!"),
                  emojize(":smiling_face_with_sunglasses:"),
                  green("YOU WON THE GAME"))
        logger.info("output of results: user won")
    else:
        print(yellow("\n\t\t\t!! TIE !!"),
                emojize(":disappointed_face:"),
                yellow("!! TRY AGAIN !!"))
        logger.info("output of results: tie")
    replay = ""
    replay_game()
    if replay == "n" or replay == "no":
        print(red("\n\t\t\tSAD TO SEE YOU GO !!", 'bold'),
                emojize(":disappointed_face:"))
        logger.info("the decision to continue the game: the game is over")
        exit()
    if replay == "y" or replay == "yes":
        print(green("\n\t\t\tYO LET'S PLAY AGAIN", 'bold'),
                emojize(":smiling_face_with_smiling_eyes:"))
        logger.info(
            "the decision to continue the game: continuation of the game")