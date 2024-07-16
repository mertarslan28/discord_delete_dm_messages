import pyautogui
import time

def get_click_position():
    print("Lütfen tıklamak istediğiniz yere fare ile tıklayın...")
    time.sleep(2)  # Kullanıcıya tıklama yapması için 2 saniye süre veriyoruz
    x, y = pyautogui.position()
    return x, y

# Kullanıcıya tıklama yapması için süre veriyoruz ve sonra koordinatları alıyoruz
x, y = get_click_position()
print(f"Tıkladığınız noktanın koordinatları: x={x}, y={y}")
