import pyautogui, time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{bcolors.HEADER}********************* Spam Bot *********************{bcolors.ENDC}")



print("Options:")

print("1. I am a Hacker")
print("2. Blindtext - 200 Wörter")
print("3. Blindtext - 500 Wörter")
print("4. Bee Movie Script")


option = input("Your Option (1, 2, 3, 4): ")

if option == "1":

    länge = input("For how long? (up to 200sec) ")
    if int(länge) in range(1, 201):
        timeout = time.time() + int(länge)
        time.sleep(5)
        while True:
            pyautogui.typewrite("i am a hacker")
            pyautogui.press("enter")

            if time.time() > timeout:
                break
    else:
        print(f"{bcolors.FAIL}Invalid Input{bcolors.ENDC}")

elif option == "2":
    time.sleep(5)
    f = open("spamtext1")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")


elif option == "3":
    time.sleep(5)
    f = open("spamtext2")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

elif option == "4":
    time.sleep(5)
    f = open("spamtext3")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

else:
    print(f"{bcolors.FAIL}Invalid Input{bcolors.ENDC}")






