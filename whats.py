import pyautogui as pg
import time

times = int(input("how many times you want to send the message? "))
message = input("enter the message: ")
print("Now go to your web.whatsapp site...")
time.sleep(5)
for i in range (times):
    pg.write(message)
    pg.press("Enter")
