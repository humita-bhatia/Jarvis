'''
#to make electron window - used node js and so much more for this 

import eel

# Point to the folder containing HTML/CSS/JS
eel.init("www")

# Start the Eel server without opening a browser
eel.start(
    "index.html",
    mode=None,      # Prevent Eel from launching Chrome/Safari
    host="localhost",
    port=8000,
    block=True
)
'''

#Works fine : according to the video
import os
import platform
import eel
from engine import command
from engine.features import *
import threading
from engine.command import *

# Play startup sound without blocking the app launch
threading.Thread(target=play_startup_sound).start()

# point to this directory
eel.init("www")

# detect the operating system
system_name = platform.system()

url = "http://localhost:8000/index.html"

if system_name == "Windows":
    os.system(f'start msedge.exe --app="{url}"')
elif system_name == "Darwin":  # macOS
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    if os.path.exists(chrome_path):
        # Open in app mode like Edge
        os.system(f'"{chrome_path}" --app="{url}"')
    else:
        # Fallback to Safari
        os.system(f'open -a "Safari" {url}')
else:  # Linux or others
    os.system(f'xdg-open {url}')

# @eel.expose
# def start_listening():
#     text=command.takecommand()
#     command.speak(text)
#     return(text)

# start eel server
eel.start('index.html', mode=None, host='localhost', block=True)


"""
import os
import platform
import eel
import shutil

# point to this directory
eel.init("www")

# detect the operating system
system_name = platform.system()

url = "http://localhost:8000/index.html"

if system_name == "Windows":
    os.system(f'start msedge.exe --app="{url}"')

elif system_name == "Darwin":  # macOS
    if shutil.which("Google Chrome"):
        os.system(f'open -a "Google Chrome" {url}')
    else:
        os.system(f'open -a "Safari" {url}')

else:  # Linux or others
    os.system(f'xdg-open {url}')

# start eel server
eel.start('index.html', mode=None, host='localhost', block=True)

"""