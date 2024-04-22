#All Imports
import time
import os
import random 
import game #A module coded & created by me.

# An area to initialize variables.
score = 0
dead_people = 0

# Imports
username = game.start()
game.intermission()

def question_one(score=0):
    '''

    A function which prompts the first question within the game.

    Arguements:
        score (int): The score to be incremented throughout the game.
    
    '''
    while True:
        try:
            answer = input("Q:1: Would you steal if you had no repercussions? (Y/N): ")
            if answer.upper() not in ("Y", "N"):
                raise ValueError("Please enter 'Y' or 'N'.")
            answer = answer.upper()

            if answer == "Y":
                print('Shaking my head. . .')
            elif answer == "N":
                score += 1 #Increments score--signaling the ethical choice.

            break
        except ValueError as e:
            print(e) #Prints the value-error

    time.sleep(1)
    print("\nNow, moving onto the next question...")
    time.sleep(2)
    os.system('cls')

    return score
    
def question_two(score=0, dead_people=0):
    '''

    A function which prompts the second question within the game.

    Arguements:
        score (int): The score to be incremented throughout the game.
        dead_people (int): A random number between 1 and 1 million, which is stored as a consequence of picking "Y".
    
    '''
    while True:
        try:
            answer = input("Q:2: If you were awarded ten million dollars for pressing a button which killed a certain amount of people, would you do it? (Y/N): ")
            if answer.upper() not in ("Y", "N"):
                raise ValueError("Please enter 'Y' or 'N'.")
            answer = answer.upper()

            if answer == "Y":
                print('Wow, you monster.')
                dead_people = random.randint(1, 1_000_000)
            elif answer == "N":
                score += 1 #Increments score--signaling the ethical choice.

            break
        except ValueError as e:
            print(e) #Prints the value-error

    time.sleep(1)
    print("\nNow, once again, let us move on...")
    time.sleep(2)
    os.system('cls')

    return score, dead_people

def question_three(score):
    '''

    A function which prompts the third & final question in the game.

    Arguements:
         score (int): The score to be incremented throughout the game.
    
    '''
    chosen_scenario = ""
    while True:
        try:
            answer = input("Q:3: Imagine you are at your best-friend's wedding. Before the ceremony, you discover their spouse-to-be cheating on them.Would you tell them? (Y/N): ")
            if answer.upper() not in ("Y", "N"):
                raise ValueError("Please enter 'Y' or 'N'.")
            answer = answer.upper()

            if answer == "Y":
                score += 1 #Increments score--signaling the ethical choice.
            elif answer == "N":
                scenarios = [
                "friend never finds out--lives happy life.",
                "friend finds out--ends up heartbroken.",
                "friend finds out--ten years later, ends up homeless."
            ]
            
                chosen_scenario = random.choice(scenarios)

                if chosen_scenario == scenarios[0]:
                    score += 1 #Increments score--signaling the ethical choice.
                elif chosen_scenario == scenarios[2]:
                    score -= 1 #Decrements score--signalling the unethical choice.

            print("\nLet's hope you made the right choice. . .")
            break
            
        except ValueError as e:
            print(e) #Prints the value-error

    time.sleep(1)
    os.system('cls')
    time.sleep(1)

    return score, chosen_scenario

def game_done(score, dead_people, chosen_scenario, answer_q3):
    '''

    A function which concludes the game with results & writes those results to file.

    Arguements:
         score (int): The score to be incremented throughout the game.
         dead_people (int): A random number between 1 and 1 million, which is stored as a consequence of picking "Y".
         chosen_scenario (str): A scenario returned from question three, which serves to return a funny result at the end, if user picks "N".
         answer_q3 (str): A variable which serves to ensure the printing of chosen_scenario works.

         
    
    '''
    with open("ethical_game_results.txt", "w") as f:
        f.write(f"Score: {score} out of three.\n")
        if dead_people > 0:
            f.write(f"\nBy the way, you killed {dead_people} people. We hope the money was worth it.\n")
        if answer_q3 == "N":
            f.write(f"\nFinally, in regards to your poor friend, your chosen scenario is: {chosen_scenario}")

    print("Score: ", score, "out of three.")
    if dead_people > 0:
        print(f"\nBy the way, you killed {dead_people} people. We hope the money was worth it.")
    if answer_q3 == "N":
        print("\nFinally, in regards to your poor friend, your", chosen_scenario)

#Order of execution; handling variable transitions from functions
score = question_one()
score, dead_people = question_two(score)
score, chosen_scenario = question_three(score)
game.credits(username) #Peer-Programming Credits
answer_q3 = input("Did you choose to keep quiet at your friend's wedding (Y/N)?: ").upper()
os.system('cls')
game_done(score, dead_people, chosen_scenario, answer_q3)
