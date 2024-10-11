import pyautogui
import numpy as np
import time
from pynput import keyboard
from pynput.mouse import Controller
import cv2
keyboard = keyboard.Controller()
mouse = Controller()
from paddleocr import PaddleOCR
# 创建PaddleOCR对象 # 设置语言为中文
ocr = PaddleOCR(lang='ch')
def oocr(img):
    result = ocr.ocr(img)
    lis = []
    for i in range(100):
        try:
            # print(result[0][i][1])
            x, y = result[0][i][1]
            lis.append(x)
        except:
            continue
    return lis
# 屏幕截图
def screenshot(region):
    im = pyautogui.screenshot(region=region)
    # 将PIL图像转换为OpenCV图像
    im = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)

    return im
def xiaoyu():
    start_x, start_y = 163, 542
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()

    # 第一部分绘制
    pyautogui.dragRel(-10, 10,duration=0.01)

    # 第二部分绘制
    pyautogui.dragRel(10, 0,duration=0.01)

    pyautogui.mouseUp()
def dayu():
    start_x, start_y = 163, 542
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()

    # 第一部分绘制
    pyautogui.dragRel(10, 10,duration=0.01)

    # 第二部分绘制
    pyautogui.dragRel(-10, 0,duration=0.01)

    pyautogui.mouseUp()
def test():
    start_x, start_y = 163, 542
    length = 40
    for i in range(length):
        pyautogui.moveTo(start_x+i, start_y-i)
        pyautogui.click()
def show(img):
    cv2.imshow('img',img)
    cv2.waitKey(0)
while True:
    try:
        #截图
        region = (107,147,154,65)
        img = screenshot(region)
        lis = oocr(img)
        #lis = ['82-11-1 =']
        num = lis[0]
        #替换
        num = num.replace(' ','')
        num  = num.replace('=','')
        jieguo = eval(num)
        print(jieguo)
        write(jieguo)
        # try:['56-53-3：']
        #
        #     if lis_1[0] == "利余":
        #         time.sleep(3)
        #         print('余')
        #         pyautogui.moveTo(248,436)
        #         pyautogui.click()
        #         time.sleep(1)
        #         pyautogui.moveTo(320,796)
        #         pyautogui.click()
        #         time.sleep(1)
        #         pyautogui.moveTo(259,697)
        #         pyautogui.click()
        #         time.sleep(5)
        #         continue
        # except:
        #     pass

        # if len(lis_1) == 0:
        #     first = 1
        # else:
        #     first = int(lis_1[0])
        # if len(lis_2)==0:
        #     second = 1
        # else:
        #     second = int(lis_2[0])
        # print(first,second)
        #

        # first = int(lis[0])
        # second = int(lis[1])
        #lis_1 = ['余']
        # if first > second:
        #     dayu()
        # elif first < second:
        #     xiaoyu()
        # else:
        #     print("NULL")
        time.sleep(3)
    except:
        pass