import sys
import os
import time


def refresh_page_test1():
    '刷新显示实例'
    i = 0
    while i < 10:
        os.system('clear')
        sys.stdout.write ("+----------------------+\n|                      |\n|           {0}          |\n|                      |\n+----------------------+".format(i))
        i = i + 1
        time.sleep(1)

def get_consel_size_test():
    '获取窗口行列大小'
    num = 1
    terminal_width = os.get_terminal_size().columns
    terminal_height = os.get_terminal_size().lines-2

    #上下窗口边线
    top_botton_line = ""
    top_botton_line = top_botton_line + "+"
    for j in range(terminal_width - 2):
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

get_consel_size_test()