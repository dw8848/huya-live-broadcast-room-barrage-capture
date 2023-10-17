import requests
import time
now_time = int(time.time() * 1000)
url = f'https://cxt.huya.com/open/danmu/timelist.do?vid=431927895&beginTime=0&_={now_time}'

while True:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    html_data = response.json()
    if html_data:
        nextBeginTime = html_data['nextBeginTime']
        lis = html_data['list']
        for li in lis:
            barrage = li['text']
            with open('hy弹幕.txt', mode='a', encoding='utf-8') as f:
                f.write(barrage)
                f.write('\n')
        url = f'https://cxt.huya.com/open/danmu/timelist.do?vid=431927895&beginTime={nextBeginTime}&_={now_time}'
        print(nextBeginTime)
    else:
        break
