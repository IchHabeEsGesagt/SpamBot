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


print(f"{bcolors.OKBLUE}{bcolors.BOLD}Visit github.com/IchHabeEsGesagt/SpamBot for Help{bcolors.ENDC}")
print(f"{bcolors.HEADER}********************* Spam Bot *********************{bcolors.ENDC}")

print("Options:")
print(" ")
print("1. Custom Text")
print("2. Blindtext - 200 Wörter")
print("3. Blindtext - 500 Wörter")
print("4. Bee Movie Script")


option = input("Your Option (1, 2, 3, 4): ")

if option == "1":

    word = input("Put in The custom Text here (up to 50 characters): ")
    s=len(word)
    if s in range(50):

        length = input("For how long? (up to 200sec): ")
        timeout = time.time() + int(length)
        if int(length) in range(1, 201):
            time.sleep(5)
            while True:
                pyautogui.typewrite(word)
                pyautogui.press("enter")

                if time.time() > timeout:
                    break
        else:
            print(f"{bcolors.FAIL}Max Time: 200sec your time: {length}{bcolors.ENDC}")
            print(f"Stopping...")
            time.sleep(2)
            print(f"{bcolors.BOLD}Stopped!{bcolors.ENDC}")
            time.sleep(1.3)
    else:
        print(f"{bcolors.FAIL}Max Character: 50 your length: {s}{bcolors.ENDC}")
        print(f"Stopping...")
        time.sleep(2)
        print(f"{bcolors.BOLD}Stopped!{bcolors.ENDC}")
        time.sleep(1.3)


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
    print(f"Stopping...")
    time.sleep(2)
    print(f"{bcolors.BOLD}Stopped!{bcolors.ENDC}")
    time.sleep(1.3)






