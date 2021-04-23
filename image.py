#下载百度api库：pip install baidu-aip
#百度文字处理，调用端口
import json
from aip import AipOcr
import requests
import time # 获取文字处理时间
#读取文件,提交本地文件路径
def read_file(image_path):
    f=None
    try:
        f=open(image_path,"rb")
        result= ocr.basicGeneral(f.read(),options)
        return result
    except:
        print("read image file fail")
    finally:
        if f:
            f.close()
#调用远程url，提供url和先关data
def requests_img(url):
    header={
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.128Safari / 537.36"
    }
    try:
        img=requests.get(url=url,headers=header).content
        result=ocr.basicGeneral(img,options)


        return result
    except:
        print("img get error")
def choose():
    n = int(input("若你要输入系统本地地址--输入0\n若你要输入图片URL--输入1\n"))
    if n==0:
        # 直接读取系统文件
        path=input("请输出文件地址以及文件名称：例如：D:/1.png")
        result=read_file(path)
        return result
    elif n==1:
        url = input("输入图片url")
        result_request = requests_img(url)
        return result_request
    else:
        print("您输出的选项错误，请重新输入")
        choose()

#设置主函数
if __name__ =="__main__":
    """ 你的 APPID AK SK """
    APP_ID = '24053178'
    API_KEY = 'HZbSPqr014lGtvgcOjlB9Y2B'
    secretkey = 'S5Zq0MHV4Tks2g0l4kvkSsw1K3IyW7oZ'
    #设置图片URl，也可以设置本地图片
    """ 如果有可选参数 """
    options = {}
    options["language_type"] = "ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"
    #以上为可选参数
    ocr=AipOcr(APP_ID,API_KEY,secretkey)
    bagin_time=time.perf_counter()
    text=" "
    # 输入文件选择函数
    result_request=choose()

    # 解析返回结果
    for words_result in result_request["words_result"]:
        text=text+words_result["words"]
    #打印文字
    print(text)
    end_time=time.perf_counter()
    #输出处理时间
    print("处理时间:"+"%.2f"%(end_time-bagin_time)+"秒")
    #调用通用物体识别

