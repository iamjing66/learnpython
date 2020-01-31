import requests
import json
import pymongo


conn = pymongo.MongoClient('mongodb://127.0.0.1:27017')
mydb = conn['spider']
myset = mydb['bilicontent']
myset1 = mydb['bilibilirank']
datas = myset1.find()
avs = []
for data in datas:
    avs.append(data['av号'])

for av in avs:
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    "Cookie": "_uuid=AEDC8F1E-546D-59D9-7257-AB9E34CF181596119infoc; buvid3=3D86E165-9802-425F-A477-275C8B8B1E9C190955infoc; LIVE_BUVID=AUTO8315744908493798; sid=bgljpv4v; CURRENT_FNVAL=16; laboratory=1-1; stardustvideo=1; rpdid=|(u~)YJJumY)0J'ul~RRmul)|; DedeUserID=11475660; DedeUserID__ckMd5=2a611ee7c426a0a7; SESSDATA=40047170%2C1580625037%2C32b68711; bili_jct=1538fa7625a6a19dd666749a3b97c60d; CURRENT_QUALITY=64; INTVER=1; bp_t_offset_11475660=345263878239648285; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1",
    "Host": "api.bilibili.com",
    'Referer': 'https://www.bilibili.com/video/av'+str(av)
}
    for page in range(1,1000):
        try:
            url = 'https://api.bilibili.com/x/v2/reply?pn='+str(page)+'&type=1&oid='+str(av)+'&sort=2'

            res = requests.get(url=url,headers=headers).content
            r= json.loads(res)
            r= r['data']['replies']

            for i in r:
                uname = i['member']['uname']
                uid = i['member']['mid']
                sex = i['member']['sex']
                level =i['member']['level_info']['current_level']
                content = i['content']['message']
                myset.insert({'用户id':uid,'用户名':uname,'性别':sex,'等级':level,'评论':content})
        except:
            break
    print(str(av)+'第'+str(page)+'页')


print('rank100完成')