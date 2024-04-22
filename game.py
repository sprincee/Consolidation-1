import os
import time


def display_rules():
    print("\nRules:")
    print("Simply put, the Ethics game will ask you five questions, depending on your answer, you will score points!\nAt the end, you will be given your score and an assessment of how ethical you are!\nIf you have no questions, we can begin.")
    time.sleep(2)

def start():
    username = str(input("Enter a username: "))
    os.system('cls')
    time.sleep(0.5)
    print(f"Welcome, {username}, to the Ethic's game!")
    time.sleep(1)
    while True:
        try:
            user_exp = input("\nWe're glad you're here! Would you like to hear the rules? (Y/N): ").upper()
            if user_exp not in ("Y", "N"):
                raise ValueError("Please, input only 'Y' or 'N'.")
            break
        except ValueError as e:
            print(e)

    if user_exp.upper() == "N":
        os.system('cls')
        print("Well, well, well. . .")
        time.sleep(2)
        print("Someone's smart, huh? We'll see how you feel after this game.")
        time.sleep(3)
        os.system('cls')
    else:
        display_rules()
        input("\nPress Enter to continue...")
        os.system('cls')

    return username



def intermission():
    print('Beginning with the first question. . .')
    time.sleep(3)
    os.system('cls')

    
    
    
def credits(username):
    print(f"Hello, {username}, this concludes the Ethics game!\nThank you for playing!")
    print('Before we display your score, please allow for a brief rolling of our credits.')
    time.sleep(2)
    os.system('cls')
    print("Credits:")
    print("  ")
    print("Creative Director: Inaya Siddiqi")
    time.sleep(0.5)
    print("VSCode Debugger: Mahad Khan")
    time.sleep(0.5)
    print('Lead Developers: Inayah Siddiqi & Mahad Khan')
    time.sleep(3)
    os.system('cls')


if __name__ == "__main__":
    start()