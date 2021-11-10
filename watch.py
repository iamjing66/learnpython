import datetime

import requests



def get_message():
    url = "https://www.ems.com.cn/apple/getMailNoRoutes"

    data = {
        "mailNum": "EZ341746550CN"
        }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
        "contentType": "application/x-www-form-urlencoded;charset=utf-8"
        }

    # res = requests.get(url=url, headers=headers, json=data)
    res = requests.post(url, headers=headers, data=data).json()
    result = res["trails"][0]
    url_data = {
        "mail_no": "",
        "optime": "",
        "opcode": "",
        "opreate_type": "",
        "process": "",
        }
    i = result[0]
    url_data["optime"] = i["optime"]
    url_data["opcode"] = i["opCode"]
    url_data["opreate_type"] = i["opreateType"]
    url_data["process"] = i["processingInstructions"]
    msg = str(url_data['optime'])+'\n'+url_data['opreate_type']+'\n'+url_data['process']
    bark_Url = f"https://api.day.app/cSUVV3HyLE5Fkw4Jx33EW8/{'iphone13 pro 快递'}/{msg}"
    requests.get(bark_Url)
    print((datetime.datetime.now()).strftime("%dd %H:%M:%S"))


if __name__ == "__main__":
    get_message()
