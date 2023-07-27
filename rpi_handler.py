import requests
import os, sys, io
import RPi.GPIO as GPIO
import time
import picamera
import configparser
from bs4 import BeautifulSoup

BUTTON_P = 8
BUTTON_M = 10
BUTTON_STOP = 12
DELAY_SEC = 0.05

rqs = requests.Session()

prev_p, cur_p = False, False
prev_m, cur_m = False, False

s = sys.stdin.read()

config = configparser.ConfigParser()
config.read_file(io.StringIO(s))

URL = config["system-data"]['url']

LOGIN = config["user-data"]["login"]

PASSWORD = config["user-data"]["password"]

APP_ROOT = config["system-data"]["root"]


camera = picamera.PiCamera()

def write_to_log(text):
    f = open(f"{APP_ROOT}/log", "a")
    f.write(text)
    f.close()

def setup():
    camera.resolution = (480, 320)

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTON_P, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_M, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_STOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def image_request(mark):
    camera.stop_preview()
    print(f'Button {mark} pressed')

    camera.resolution = (2160, 1440)

    r = rqs.post(URL + 'login', data={'login': LOGIN, 'password': PASSWORD})
    
    camera.capture(APP_ROOT + '/rpi_image_cache/cached.jpg')
    print("Photo saved")
    
    img = open(APP_ROOT + '/rpi_image_cache/cached.jpg', 'rb')

    files = {'photo': img}

    r = rqs.post(URL + 'lk/put_mark', files=files, data={'mark': mark})

    img.close()
    os.remove(APP_ROOT +'/rpi_image_cache/' + 'cached.jpg')
    camera.resolution = (480, 320)

    s = r.text
    soup = BeautifulSoup(s, 'html.parser')

    data = soup.findAll('b')
    if len(data) == 0:
        print('Система не смогла распознать ученика в камере')
        write_to_log("Cannot classify\n")
    else:
        print(f'Имя ученика: {data[0].text}')
        write_to_log(f"Name: {data[0].text} Mark: {mark}\n")
    
    time.sleep(5)
    camera.start_preview()



if True:

    setup()

    camera.start_preview()
    
    while True:
        cur_p = GPIO.input(BUTTON_P)
        cur_m = GPIO.input(BUTTON_M)

        if GPIO.input(BUTTON_STOP):
            os.system(f'lxterminal -e "python3 {APP_ROOT}/mainloop.py < {APP_ROOT}/conf.ini"')
            exit()

        if not prev_p and cur_p:
            time.sleep(DELAY_SEC)
            cur_p = GPIO.input(BUTTON_P)
            if not prev_p and cur_p:
                image_request('+')
            
        elif not prev_m and cur_m:
            time.sleep(DELAY_SEC)
            cur_m = GPIO.input(BUTTON_M)
            if not prev_m and cur_m:
                image_request('-') 

        prev_p = cur_p
        prev_m = cur_m
