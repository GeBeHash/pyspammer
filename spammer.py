import pyautogui
import time

text_file = input("Read from text file ( 1 ) or input ( 2 ) ? ")
if text_file == "1":
    script = open("input.txt", "r")
    count = 5
    while count != 0:
        print(count)
        time.sleep(1)
        count -= 1
    print("Fire in the hole!")
    for word in script:
        pyautogui.typewrite(word + '\n')
elif text_file == "2":
    msg = input("Message = ")
    n = input("How many? ")
    print("t minus ")
    count = 5
    while count != 0:
        print(count)
        time.sleep(1)
        count -= 1
    print("Fire in the hole!")
    for i in range(0, int(n)):
        pyautogui.typewrite(msg + '\n')
