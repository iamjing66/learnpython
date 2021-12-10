import datetime

import requests



def get_message():
    url = "https://m.kuaidi100.com/query"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Cookie": "csrftoken=dWbSdIkipfja3EilDuGRecAYQtsJP3QVLbQhyUvN2NA; WWWID=WWWB8870091F52FA59F771F801FE5040595",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = {
        "postid": "JDX006601212979",
        "id": "1",
        "valicode": "",
        "temp": "0.4556408500954994",
        "type": "jd",
        "phone": "",
        "token": "",
        "platform": "MWWW"
    }
    res = requests.post(url, headers=headers, data=data).json()
    order = res["nu"]
    last_time = res["data"][0]["time"]
    last_info = res["data"][0]["context"]
    msg = f"订单号：{}\n最新时间：{}\n最新信息：{}".format(order, last_info, last_time)
    bark_Url = f"https://api.day.app/cSUVV3HyLE5Fkw4Jx33EW8/{'AirPods pro'}/{msg}"
    requests.get(bark_Url)
    print((datetime.datetime.now()).strftime("%dd %H:%M:%S"))


if __name__ == "__main__":
    get_message()
