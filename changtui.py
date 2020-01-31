import requests
from lxml import etree
from urllib import request
import os

name = 1
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'referer': 'https://www.zhihu.com/question/27098131'
}
for x in range(0,10001,5):

    url = 'https://www.zhihu.com/api/v4/questions/27098131/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset='+str(x)+'&platform=desktop&sort_by=default'
# res = requests.get(url=url,headers=headers).json()
# data = res['data']
# print(data)
    try:
        res = requests.get(url=url,headers=headers).json()
        data = res['data']
        for i in data:
            num = 0
            user = i['author']['name']
            author = user+str(name)
            ele = etree.HTML(i['content'])
            pic1 = ele.xpath("//img/@data-original")
            pic2 = set(pic1)
            pic = list(pic2)
            os.mkdir('C:\\Users\\jingy\\Desktop\\pic\\萌萌\\'+author)
            name+=1
            for j in range(0,len(pic)):
                request.urlretrieve(pic[j],'C:\\Users\\jingy\\Desktop\\pic\\萌萌\\'+author+'\\'+str(num)+'.jpg')
                num+=1
                # print(pic[j])
            print(author)
    except: 
        continue