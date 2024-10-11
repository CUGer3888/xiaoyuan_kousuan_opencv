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

def write():
    start_x, start_y = 163, 542
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.dragRel(0, 10, duration=0.01)
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
        time_1 = time.time()
        #截图
        region_1 = (145,208,60,58)
        img_1 = screenshot(region_1)

        region_2 = (251,212,54,57)
        img_2 = screenshot(region_2)
        #OCR
        # show(img_1)
        lis_1 = oocr(img_1)
        lis_2 = oocr(img_2)
        print(lis_1,lis_2)

        time_2 = time.time()
        print("识别数字用时：",time_2-time_1)
        try:

            if lis_1[0] == "剩余":
                time.sleep(3)
                print('余')
                pyautogui.moveTo(248,436)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(320,796)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(259,697)
                pyautogui.click()
                time.sleep(5)
                continue
        except:
            pass

        if len(lis_1) == 0:
            first = 1
        else:
            first = int(lis_1[0])
        if len(lis_2)==0:
            second = 1
        else:
            second = int(lis_2[0])
        print(first,second)
        #
        # region = (142,186,179,102)
        # img = screenshot(region)
        # lis = oocr(img)
        # print(lis)
        # first = int(lis[0])
        # second = int(lis[1])
        #lis_1 = ['余']
        if first > second:
            start_x, start_y = 163, 542
            pyautogui.moveTo(start_x, start_y)
            pyautogui.mouseDown()

            # 第一部分绘制
            pyautogui.dragRel(10, 10, duration=0.01)

            # 第二部分绘制
            pyautogui.dragRel(-10, 0, duration=0.01)

            pyautogui.mouseUp()
        elif first < second:
            start_x, start_y = 163, 542
            pyautogui.moveTo(start_x, start_y)
            pyautogui.mouseDown()

            # 第一部分绘制
            pyautogui.dragRel(-10, 10, duration=0.01)

            # 第二部分绘制
            pyautogui.dragRel(10, 0, duration=0.01)

            pyautogui.mouseUp()
        else:
            print("NULL")
        time_3 = time.time()
        print("点击用时：",time_3-time_2)
        time.sleep(0.5)
    except:
        pass