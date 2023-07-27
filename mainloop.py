import os, sys, io, configparser
import RPi.GPIO as GPIO

BUTTON_STOP = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_STOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

config = configparser.ConfigParser()
config.read_file(io.StringIO(sys.stdin.read()))

APP_ROOT = config['system-data']['root']

os.system(f"cat {APP_ROOT}/log")
open(f"{APP_ROOT}/log", "w").close()

while True:

    if GPIO.input(BUTTON_STOP):
        os.system(f'lxterminal -e "bash {APP_ROOT}/auto.sh"')
        exit()
