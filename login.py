import subprocess
import re
import sys
import time
import pyautogui
import json

def connect_ssid():
    result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True)
    ssids = re.findall(r"SSID\s+\d+\s+:\s(.+)", result.stdout)

    if ssids:
        for ssid in ssids:
            # Check if the SSID starts with "BPGC"
            if ssid.startswith("BPGC"):
                print("Connecting to:", ssid)
                subprocess.run(["netsh", "wlan", "connect", f'"{ssid}"'])
                return  # Connect to the first matching network and exit
        print("No BPGC networks found.")
        time.sleep(5)
        sys.exit(0)
    else:
        print("No WiFi networks found.")
        time.sleep(5)
        sys.exit(0)

def login_to_wifi(username, password):
    pyautogui.hotkey('winleft', 'r')
    pyautogui.typewrite('https://campnet.bits-goa.ac.in:8090/')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(2)
    pyautogui.press('tab', presses=2)
    pyautogui.typewrite(username)
    pyautogui.press('tab')
    pyautogui.typewrite(password)
    pyautogui.press('enter')

def load_credentials():
    try:
        with open("credentials.json", "r") as f:
            credentials = json.load(f)
            # print("Username: ",username,"\n")
            return credentials["username"], credentials["password"]
    except FileNotFoundError:
        print("No saved credentials found. Please check if both exe files are in the same folder")
        time.sleep(5)
        sys.exit(0)
        return None, None

if __name__ == "__main__":
    connect_ssid()
    print("\n do not interrupt operation. ETA: 15 sec")
    time.sleep(10)
    username, password = load_credentials()
    
    if username and password:
        login_to_wifi(username, password)
        print("login successful")
        time.sleep(5)
        sys.exit(0)
    else:
        print("Please save your credentials first. Do keep both exe files in the same folder")
        time.sleep(5)
        sys.exit(0)