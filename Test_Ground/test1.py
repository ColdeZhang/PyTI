import os
import sys
import threading
import time

import keyboard


def refresh_page_test1():
    '刷新显示实例'
    i = 0
    while i < 10:
        os.system('clear')
        sys.stdout.write ("+----------------------+\n|                      |\n|           {0}          |\n|                      |\n+----------------------+".format(i))
        i = i + 1
        time.sleep(1)

def get_consel_size_test():
    '[已废弃]获取窗口行列大小'
    num = 1
    terminal_width = os.get_terminal_size().columns
    terminal_height = os.get_terminal_size().lines-2

    #上下窗口边线
    top_botton_line = ""
    top_botton_line = top_botton_line + "+"
    for _ in range(terminal_width - 2):
        top_botton_line = top_botton_line + "-"
    top_botton_line = top_botton_line + "+\n"

    #左右边框
    unused_line = ""
    unused_line = unused_line + "|"
    for j in range(terminal_width - 2):
        unused_line = unused_line + " "
    unused_line = unused_line + "|\n"

    while num < 10:
            #生成内容
        content = ""
        content = content + top_botton_line
        for j in range(int(terminal_height/2)-2):
            content = content + unused_line
        content = content + "|"
        for j in range(int(terminal_width/2 -1 ) - 1):
            content = content + " "
        content = content + str(num)
        for j in range(int(terminal_width/2 -1)):
            content = content + " "
        content = content + "|\n"
        for j in range(int(terminal_height/2)):
            content = content + unused_line
        content = content + top_botton_line
        # for i in range(terminal_height-2):
        #     content = content + unused_line

        # content = content + unused_line
        # content = content + unused_line
        # content = content + top_botton_line

        os.system('clear')
        # sys.stdout.write ("{0}".format(terminal_height))
        # sys.stdout.write ("{0}".format(terminal_width))
        sys.stdout.write ("{0}".format(content))
        #print("{0}".format(content),end=" ")
        num = num + 1
        time.sleep(1)    

def get_terminal_size():
    '[可用]获取页面尺寸'
    terminal_width = os.get_terminal_size().columns
    terminal_height = os.get_terminal_size().lines-2
    return [terminal_width, terminal_height]

def instance_page():
    '[可用]生成页面'
    width = get_terminal_size()[0]
    height = get_terminal_size()[1]

    #生成顶部边线
    top_botton_line = ""
    top_botton_line = top_botton_line + "+"
    for _ in range(width - 2):
        top_botton_line = top_botton_line + "-"
    top_botton_line = top_botton_line + "+\n"

    #生成左右边线
    unused_line = ""
    unused_line = unused_line + "|"
    for _ in range(width - 2):
        unused_line = unused_line + " "
    unused_line = unused_line + "|\n"

    #将顶部边线与左右边线合并
    page = ""
    page = page + top_botton_line
    for _ in range(height-2):
        page = page + unused_line
    page = page + top_botton_line

    return page

def keyboard_detect():
    '[可用]键盘侦测测试'
    if keyboard.is_pressed("left"):
        time.sleep(0.2)
        return "left"
    elif keyboard.is_pressed("right"):
        time.sleep(0.2)
        return "right"
    elif keyboard.is_pressed("left"):
        time.sleep(0.2)
        return "enter"
    else:
        time.sleep(0.1)
        return "null"




def btn(btn_name, state):
    if state == 0:
        btn = ">" + btn_name + "<"
        btn = "\33[0m" + btn + "\33[0m"
        return btn
    elif state == 1:
        btn = ">" + btn_name + "<"
        btn = "\33[7m" + btn + "\33[0m"  
        return btn      

def input_scan():
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

# os.system('clear')
# sys.stdout.write("\33[7m>CONFIRM<\33[0m")
# sys.stdout.flush()

class consts():
    '存储共有变量'
    btn_id = 0
    page = ""

# t = threading.Thread(target=keyboard_detect)  
# t.start()
# t.join()
os.system('clear')
consts.page = "\t\t\t" + btn("CONFERM", 0) + "\t" + btn("CANCEL", 1) + "\n\n\n\n\n\n\n\n\n\n"
page_current = consts.page
sys.stdout.write(page_current)
sys.stdout.flush()


threads = []

t = threading.Thread(target=input_scan)
threads.append(t)
t = threading.Thread(target=page_fresh)
threads.append(t)
for t in threads:
    t.start()

for t in threads:
    t.join()

while True:  
    if consts.page != page_current:
        page_current = consts.page 
        os.system('clear')     
        sys.stdout.write(consts.page)
        sys.stdout.flush()

# os.system('clear')
# sys.stdout.write ("{0}".format(instance_page()))
# while True:
#     if get_terminal_size() != get_terminal_size():
#         os.system('clear')
#         sys.stdout.write ("{0}".format(instance_page()))




