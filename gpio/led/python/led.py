#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO	        # 載入模組
import time				

GPIO.setmode(GPIO.BCM)          # 選擇系統
LED_PIN = 4
GPIO.setup(LED_PIN, GPIO.OUT)   # 定義腳位

while True:
        print("LED is on")
        GPIO.output(LED_PIN, GPIO.HIGH)         # 讀取輸入/寫入輸出
        time.sleep(1)
        print("LED is off")
        GPIO.output(LED_PIN, GPIO.LOW)          # 讀取輸入/寫入輸出
        time.sleep(1)

GPIO.cleanup()                 # 回收
