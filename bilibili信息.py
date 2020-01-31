import requests
from lxml import etree
import pymongo

conn = pymongo.MongoClient('mongodb://127.0.0.1:27017')
mydb = conn['spider']
myset = mydb['bilibilirank']

url = 'https://www.bilibili.com/ranking'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

res = requests.get(url=url,headers=headers).text
ele = etree.HTML(res)
# img = ele.xpath("//div[@class='img']/text()")
imgs = ele.xpath("//div[@class='lazy-img cover']/img/@original")
print(imgs)
# names = ele.xpath("//div[@class='info']/a[@class='title']/text()")
# ranks = ele.xpath("//div[@class='num']/text()")
# hrefs = ele.xpath("//div[@class='info']/a[@class='title']/@href")
# imgs = ele.xpath("//div[@class='lazy-img cover']/img/@src")
# for name in names:
#     i = names.index(name)
#     rank = ranks[i]
#     href = hrefs[i]
#     ok = href.split('/')[-1]
#     av = ok[2:]
#     img = imgs[i]
#     print(rank,name)
#     myset.insert({'排名':rank,'视频名':name,'av号':av,'地址':href,'封面':img})