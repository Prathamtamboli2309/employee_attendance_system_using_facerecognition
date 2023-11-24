import sqlite3 as sq
import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import pandas as pd
import csv

con=sq.connect("Face_details.db")
cur=con.cursor()

keyboard = Controller()#intialization of keyboard control
def send_whatsapp_message(employee_id, message):
    # Fetching employee data from the database
    # cur.execute("SELECT wh_no FROM Emp_details WHERE id = ?", (employee_id,))
    # whatsapp_no = cur.fetchone()
    
    try:
                print("hi")
                pywhatkit.sendwhatmsg_instantly(
                    phone_no=f"+919974343337",  # whatsapp_no is a tuple
                    message="hello",
                    tab_close=True)
                time.sleep(10)  # Wait for the message to send
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                # print(f"Message sent to Employee ID {employee_id} successfully!")
    except Exception as e:
                print(f"Failed to send message to Employee ID: {str(e)}")
        # else:
            # print(f"Employee ID {employee_id} not found in the database.")
    # else:
        # print(f"Employee ID {employee_id} not found in the database.")

if __name__ == "__main":
    while True:
        employee_id = input("Enter Employee ID (or 'q' to quit): ")
        if employee_id.lower() == 'q':
            break
msg="HEY,WHAT'S UP..!!!"
print("h2")
send_whatsapp_message(11,msg)   
