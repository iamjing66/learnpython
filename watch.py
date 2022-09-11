import datetime

import requests


def get_cookie():
    url = "https://m.kuaidi100.com/result.jsp"
    res = requests.get(url)
    cookiejar = res.cookies
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    return cookiedict



def get_message():
    cookie = get_cookie()
    
    url = "https://m.kuaidi100.com/query"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Cookie": f"csrftoken={cookie['csrftoken']}; WWWID={cookie['WWWID']}",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = {
        "postid": "JDX011037518700",
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
    msg = f"订单号: {order}\n最新时间: {last_time}\n最新信息: {last_info}"
    bark_Url = f"https://api.day.app/fNDe4yZko9tnRopxuXXXsT/{'刃9000K'}/{msg}"
    requests.get(bark_Url)
    print((datetime.datetime.now()).strftime("%dd %H:%M:%S"))


if __name__ == "__main__":
    get_message()
