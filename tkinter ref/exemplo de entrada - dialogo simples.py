import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

user_inp = simpledialog.askstring(title="Test", prompt="What's your Name?")

print("Hello " + user_inp)
