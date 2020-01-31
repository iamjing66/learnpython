import requests
import pymongo



conn = pymongo.MongoClient('mongodb://127.0.0.1:27017')
mydb = conn['spider']
myset = mydb['biliallrank3day']

rid = [0,1,168,3,129,4,36,188,160,119,155,5,181]
for id in rid:

    url = 'https://api.bilibili.com/x/web-interface/ranking?rid='+str(id)+'&day=3&type=1&arc_type=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        "Cookie": "_uuid=AEDC8F1E-546D-59D9-7257-AB9E34CF181596119infoc; buvid3=3D86E165-9802-425F-A477-275C8B8B1E9C190955infoc; LIVE_BUVID=AUTO8315744908493798; sid=bgljpv4v; CURRENT_FNVAL=16; laboratory=1-1; stardustvideo=1; rpdid=|(u~)YJJumY)0J'ul~RRmul)|; DedeUserID=11475660; DedeUserID__ckMd5=2a611ee7c426a0a7; SESSDATA=40047170%2C1580625037%2C32b68711; bili_jct=1538fa7625a6a19dd666749a3b97c60d; CURRENT_QUALITY=64; bp_t_offset_11475660=345263878239648285; INTVER=1",
        'Referer': 'https://www.bilibili.com/ranking'
    }

    res = requests.get(url=url,headers=headers).json()
    rid = [0,1,168,3,129,4,36,188,160,119,155,5,181]
    if id == 0:
        a = '全站'
    elif id ==1:
        a= '动画'
    elif id ==168:
        a ='国创相关'
    elif id == 3:
        a = '音乐'
    elif id == 129:
        a = '舞蹈'
    elif id == 4:
        a ='游戏'
    elif id =='36':
        a = '科技'
    elif id == 188:
        a = '数码' 
    elif id == 160:
        a = '生活' 
    elif id == 119:
        a = '鬼畜' 
    elif id == 155:
        a = '时尚' 
    elif id == 5:
        a = '娱乐' 
    elif id == 181:
        a = '影视' 
    rank = res['data']['list']
    for i in rank:
        print('榜单名称'+a,'视频id'+str(i['aid']),'作者'+str(i['author']),'视频标题'+str(i['title']),'视频时长'+str(i['duration']),'播放量'+str(i['play']),'综合得分'+str(i['pts']),'弹幕量'+str(i['video_review']))
        myset.insert({'榜单名称':a,'视频id':i['aid'],'作者':i['author'],'视频标题':i['title'],'视频时长':i['duration'],'播放量':i['play'],'综合得分':i['pts'],'弹幕量':i['video_review']})
        # print('视频id'+i['aid']+'作者'+i['author'])