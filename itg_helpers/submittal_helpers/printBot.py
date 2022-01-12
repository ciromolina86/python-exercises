import os
import time

import pyautogui


if __name__ == '__main__':
    retries = 0

    while retries < 10:
        try:
            if pyautogui.locateOnScreen('./img/CutePDF Writer - Title Bar.PNG'):
                targetCoordinates = pyautogui.locateCenterOnScreen('./img/CutePDF Writer - Save Button.PNG')
                pyautogui.click(targetCoordinates)
                print(targetCoordinates)
            else:
                retries += 1

        except:
            pass
        
        finally:
            print(retries)

        time.sleep(1)
