from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
time_stamp = datetime.datetime.now()
file_name = f'recording-{time_stamp.day}-{time_stamp.month}-{time_stamp.year}-{time_stamp.hour}-{time_stamp.minute}-{time_stamp.second}.mp4'
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
captured_video=cv2.VideoWriter(file_name,fourcc,10.0,(width,height))
while True:
    img = ImageGrab.grab(bbox=(0,0,width,height))
    img_np =np.array(img)
    img_final = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    cv2.imshow('Recorder',img_final)
    captured_video.write(img_final)
    if cv2.waitKey(1) == ord('q'):
        break