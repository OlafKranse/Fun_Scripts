### spams a message affter a certain input for n amount of times ###
import pyperclip
import time
import pyautogui

file = "in.txt"

n = 5
start = input()
time.sleep(5)
for things in range(1,n):
    with open(file, "r",encoding="utf8") as f:
        for lines in f:
            message = lines
            pyperclip.copy(message)
            #print(pyperclip.paste())
            #print(things)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')
            time.sleep(60)
