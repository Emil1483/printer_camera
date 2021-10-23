from flask import Flask, Response, send_file
import RPi.GPIO as GPIO
import os
import threading
import time

from led import *
from reset_timer import *

app = Flask(__name__)

def current():
    return int(time.time())

delay = 20
pref = current() - delay

s = False
def update_lights(x=1):
    time_since_last = current() - pref

    sleep_time = delay - time_since_last

    print(sleep_time)

    if sleep_time > 0: time.sleep(sleep_time)

    time_since_last = current() - pref
    if time_since_last >= delay: lights_off()

    threading.Timer(10, update_lights).start()

@app.route('/live', methods=['GET'])
def main():
    global pref

    lights_on()

    pref = int(time.time())

    os.system('fswebcam -r 1280x720 img.jpg')
    
    return send_file('img.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    try:
        import logging
        logging.basicConfig(filename='server.log',level=logging.DEBUG)

        update_lights(0)

        app.run('0.0.0.0', port = 80, debug = True)
    finally:
        GPIO.cleanup()
