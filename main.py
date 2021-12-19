from flask import Flask, Response
import RPi.GPIO as GPIO
import os
from time import sleep
import cv2

from led import *

app = Flask(__name__)
camera = cv2.VideoCapture(0)

@app.route('/frame', methods=['GET'])
def frame():
    lights_on()

    success, frame = camera.read()
    if not success: return 500, 'could not read camera'

    ret, buffer = cv2.imencode('.jpg', frame)
    frame = buffer.tobytes()
    
    return Response(frame, mimetype='image/jpeg')

@app.route('/notify', methods=['POST'])
def notify():
    delay = 0.1

    for _ in range(2):
        lights_on()
        sleep(delay)
        lights_off()
        sleep(delay)

    return 'You did it. You flickered the lights'

if __name__ == '__main__':
    try:
        import logging
        logging.basicConfig(filename='server.log', level=logging.DEBUG)

        app.run('0.0.0.0', port=80)
    finally:
        GPIO.cleanup()
