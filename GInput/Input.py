from pynput.mouse import Controller as ControllerM
from pynput.keyboard import Controller as ControllerK
import pickle
from copy import deepcopy
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


FuncList = {'on_move': lambda x, y, z: on_move(x, y, z),
            'on_press': lambda x, y: on_press(x, y),
            'on_release': lambda x, y: on_release(x, y),
            'on_clickT': lambda x, y: click_press(x, y),
            'on_clickF': lambda x, y: click_release(x, y)}

class Record():
    __slots__ = ('reader', )

    def __init__(self, ScriptName):
        with open('../../data/' + ScriptName + '.pickle', "rb") as file:
            self.reader = pickle.load(file)

        for i in range(len(self.reader)):
            func_name = self.reader[i][0]
            fargs = self.reader[i][1:]
            if func_name == 'on_click':
                fargs = self.reader[i][3], self.reader[i][5]
                if self.reader[i][4]:
                    func_name = 'on_clickT'
                else:
                    func_name = 'on_clickF'

            self.reader[i] = lambda func=FuncList[func_name], args=fargs: func(*args)

        self.reader = deepcopy(list(filter(lambda x: x != None, self.reader)))
    def __call__(self):
        for i in self.reader:
            i()