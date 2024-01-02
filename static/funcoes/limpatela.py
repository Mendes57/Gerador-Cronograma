import os
import time

def clear():
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.1)