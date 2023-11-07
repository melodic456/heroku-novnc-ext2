#!/usr/bin/env python3
import os
import time
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests
try:
    os.system("pip3 install pyautogui")
    import pyautogui
except:
    pass
    # os.system("pip install pyautogui")

try:
    # pip3 install opencv-python
    os.system("pip3 install opencv-python")
except:
    pass
    # os.system("pip install opencv-python")

from time import sleep
if __name__ == "__main__":
    time.sleep(30)
    location = pyautogui.locateOnScreen("/apps/python/extension_icon.png", grayscale=True, confidence=0.9)
    print(location)
    pyautogui.click(location)
    time.sleep(5)
    location = pyautogui.locateOnScreen("/apps/python/open_extension.png", grayscale=True, confidence=0.9)
    print(location)
    pyautogui.click(location)
    # location = pyautogui.locateOnScreen("F:\python\outlook-account-generator-master\src\write.png", grayscale=True, confidence=0.9)
    # print(location)
    # pyautogui.click(location)
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.write("9bf7f2eb08d70edc70b372a7b3dfd0c0")
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('esc')
    if os.getenv("NO_SLEEP") == "1":
        if "APP_NAME" not in os.environ:
            print("APP_NAME unset, terminating...")
            exit()
        app_name = os.getenv("APP_NAME")
        while True:
            try:
                requests.get(f"https://{app_name}.herokuapp.com")
            except:
                print("Ping failed, retrying...")
                try:
                    requests.get(f"https://{app_name}.herokuapp.com")
                except:
                    print("Cannot ping app, terminating...")
            sleep(25*60)
