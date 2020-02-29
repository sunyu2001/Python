import keyboard
from PIL import ImageGrab
import time
import sys
from baidu import BaiduApi
import pyperclip

def screenShot():
    '''用于截图保存'''
    if keyboard.wait(hotkey='ctrl+shift+print screen')==None:#截图开始，我的截图的快捷键是ctrl+shift+PrtSc，可根据实际更改
        if keyboard.wait(hotkey='enter')==None:#可作为截图复制成功标志，可删除
            im=ImageGrab.grabclipboard()
            im.save('Picture.png')#保存文件
if __name__ == "__main__":
    baiduapi=BaiduApi('password.ini')#读取使用的百度云接口数据
    for i in range(10):#运行次数
        screenShot()
        pyperclip.copy(baiduapi.picture2text('Picture.png'))