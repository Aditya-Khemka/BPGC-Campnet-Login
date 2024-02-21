import tkinter as tk
from tkinter import simpledialog
import json

def save_credentials(username, password):
    credentials = {"username": username, "password": password}
    with open("credentials.json", "w") as f:
        json.dump(credentials, f)
    print("Credentials saved successfully.")

def get_credentials():
    root = tk.Tk()
    root.withdraw()
    username = simpledialog.askstring("Input", "Enter your username:")
    password = simpledialog.askstring("Input", "Enter your password:", show='*')
    return username, password

if __name__ == "__main__":
    username, password = get_credentials()
    save_credentials(username, password)
