import pyautogui
import time

for _ in range(200):
    pyautogui.click(791, 872)

    pyautogui.press('up')
    time.sleep(0.3)

    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.3)

    pyautogui.press('delete')
    time.sleep(0.3)

    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1)


