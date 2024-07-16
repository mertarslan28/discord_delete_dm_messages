import pyautogui
import time

count = 100
x = 797 
y = 820

for _ in range(count):
    pyautogui.click(x, y)

    pyautogui.press('up')
    time.sleep(0.3)

    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.3)

    pyautogui.press('delete')
    time.sleep(0.3)

    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1)


