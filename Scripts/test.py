from GInput import *
import time
import keyboard as kb
from multiprocessing import Process, Manager
from pynput.mouse import Button
from pynput.mouse import Controller as ControllerM
from pynput.keyboard import Controller as ControllerK
from time import perf_counter, sleep

mouse = ControllerM()
keyboard = ControllerK()

def Sleep(s_time):
    __start = perf_counter()
    sleep(s_time - 0.1) if s_time > 0.2 else None
    while perf_counter() - __start < s_time:
        pass

def click_press(Button, Delay):
    Sleep(Delay)
    mouse.press(Button)

def click_release(Button, Delay):
    Sleep(Delay)
    mouse.release(Button)

def on_move(x, y, Delay):
    Sleep(Delay)
    mouse.position = (x, y)

def on_press(ButtonK, Delay):
    Sleep(Delay)
    keyboard.press(ButtonK)

def on_release(ButtonK, Delay):
    Sleep(Delay)
    keyboard.release(ButtonK)


def kblist(run):
    while True:
        if kb.is_pressed('b'):
            if run.value == True:
                run.value = False
                time.sleep(1)
                print(run)
            else:
                run.value = True
                time.sleep(1)
                print(run)

def Presser(run):
    while True:
        if run.value:
            on_press('v', 0.1)
            on_release('v', 0.1)
            click_press(Button.left, 0)
            click_release(Button.left, 0.1)

def Start():
    run = Manager().Value(bool, False)
    p = Process(target=kblist, args=(run, ))
    p.start()
    Presser(run)

if __name__ != '__mp_main__':
    Start()