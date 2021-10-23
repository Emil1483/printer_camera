from flask import Flask, Response, send_file
import RPi.GPIO as GPIO
import os

from led import *

app = Flask(__name__)

@app.route('/live', methods=['GET'])
def main():
    lights_on()

    os.system('fswebcam -r 1280x720 img.jpg')
    
    return send_file('img.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    try:
        import logging
        logging.basicConfig(filename='server.log',level=logging.DEBUG)

        app.run('0.0.0.0', port = 80, debug = True)
    finally:
        GPIO.cleanup()
