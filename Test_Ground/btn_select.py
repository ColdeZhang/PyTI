import sys
import os
import time
import keyboard
import threading

def keyboard_detect():
    '[可用]键盘侦测测试'
    if keyboard.is_pressed("left"):
        time.sleep(0.05)
        return "left"
    elif keyboard.is_pressed("right"):
        time.sleep(0.05)
        return "right"
    elif keyboard.is_pressed("enter"):
        time.sleep(0.05)
        return "enter"


def btn(btn_name, state):
    '生成按钮'
    if state == 0:
        btn = ">" + btn_name + "<"
        btn = "\33[0m" + btn + "\33[0m"
        return btn
    elif state == 1:
        btn = ">" + btn_name + "<"
        btn = "\33[7m" + btn + "\33[0m"  
        return btn

def input_scan():
    '切换按钮id'
    while True:
        if keyboard_detect() == "left":
            if consts.btn_id == 1:
                consts.btn_id = 0
            else:
                consts.btn_id = 1
        if keyboard_detect() == "right":
            if consts.btn_id == 0:
                consts.btn_id = 1
            else:
                consts.btn_id = 0

def page_fresh():
    '页面更新'
    while True:
        if consts.btn_id == 1:
            consts.page = "\t\t\t" + btn("CONFERM", 0) + "\t" + btn("CANCEL", 1) + "\n\n\n\n\n\n\n\n\n\n"
        elif consts.btn_id == 0:
            consts.page = "\t\t\t" + btn("CONFERM", 1) + "\t" + btn("CANCEL", 0) + "\n\n\n\n\n\n\n\n\n\n"

def main():
    while True:  
        if consts.page != consts.page_current:
            consts.page_current = consts.page 
            os.system('clear')     
            sys.stdout.write(consts.page_current)
            sys.stdout.flush()
# os.system('clear')
# sys.stdout.write("\33[7m>CONFIRM<\33[0m")
# sys.stdout.flush()

class consts():
    '存储共有变量'
    btn_id = 0
    page = ""
    page_current = ""

# t = threading.Thread(target=keyboard_detect)  
# t.start()
# t.join()
os.system('clear')
consts.page = "\t\t\t" + btn("CONFERM", 0) + "\t" + btn("CANCEL", 1) + "\n\n\n\n\n\n\n\n\n\n"
consts.page_current = consts.page
sys.stdout.write(consts.page_current)
sys.stdout.flush()


threads = []

t = threading.Thread(target=input_scan)
threads.append(t)
t = threading.Thread(target=page_fresh)
threads.append(t)
t = threading.Thread(target=main)
threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()

