# Python
学习使用python,制作各种各样的项目。

password.ini 文件写入百度智能云参数（需要向百度智能云申请）。
需要运行screenShot.py开启全部代码。
## 两个模块分别独立。
baidu.py实现了智能云接口的调用，图片的识别，其中的picture2text方法返回了识别结果。
screenShot.py实现了监视键盘功能，当运用快捷键截图时，负责保存图片到指定位置；然后调用baidu.py进行识别，最后把文字复制到剪切板。
