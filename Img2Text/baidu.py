from aip import AipOcr
import configparser#读取配置文件
class BaiduApi():
    '''图片文字识别'''
    def __init__(self,filepath):#初始化方法
        target=configparser.ConfigParser()
        target.read(filepath,encoding='utf-8')#读取配置文件
        app_id=target.get('我的工单','APP_ID')
        api_key=target.get('我的工单','API_KEY')
        secret_key=target.get('我的工单','SECRET_KEY')
        self.client=AipOcr(app_id,api_key,secret_key)#加self全局可用
   
    def picture2text(self,filepath):
        image=self.getPicture(filepath)#读取图片
        texts=self.client.basicGeneral(image)#调用封装好的AipOcr
        allTexts=''#得到的结果是字典类型，下面转化为字符串类型
        for word in texts['words_result']:
            allTexts=allTexts+word.get('words')
        return allTexts

    @staticmethod
    def getPicture(filepath):#打开图片，得到二进制文件
        with  open(filepath,'rb') as fp:
            return fp.read()

if __name__ == "__main__":
    baiduapi=BaiduApi('password.ini')
    print(baiduapi.picture2text('Picture.png'))