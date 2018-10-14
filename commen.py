import requests
#登录接码平台
#专业提供验证码服务
#平台地址http://39.104.119.179:9180/
userid = 'gd29'#取码账号
password = '123.....'取码密码

def login(userid,password):
    url = f'http://39.104.119.179:9180/service.asmx/UserLoginStr?name={userid}&psw={password}'
    token = requests.get(url).text
    print(token)
    return token
def getphone(token):
    data = {
        'token':token,
        'xmid': '3772',
        'sl':   '1',
        'ks':   '0',
        'rj':   'gd2941'
    }
    url = 'http://39.104.119.179:9180/service.asmx/GetHM2Str?'
    hm = requests.get(url,params=data,timeout=60).text#使用params自动拼接URL
    print(hm)
    if len(hm) != 11:
        print('获取号码出现错误')
        if int(hm) == int(-8):
            print('余额不足')
            exit(1)#退出
    else:
        print(f'正常获取号码，号码为：{hm}')
        return hm
def getmsg(token,hm):
    xmid = '3772'
    url = 'http://39.104.119.179:9180/service.asmx/GetYzm2Str?'
    data = {
        'token':token,
        'xmid': xmid,
        'hm': hm,
        'sf': 1 # sf为0不释放号码，为1继续占用号码
    }
    resp = requests.get(url, params=data).text
    return resp  #这里直接返回验证码 ，若获取不到验证，请在实例化的时候自行判断

def sfhm(token,hm):#释放号码，当获取不到验证码时使用
    URL = 'http://39.104.119.179:9180/service.asmx/sfAllStr?'
    data = {
        'token':token,
        'hm': hm
    }
    resp = requests.get(URL,params=data).text
    if resp == '1':
        print(f'成功释放号码，号码为{hm}：')
