import requests
import time

url = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=393308235fd0470bbc6ac2ad5eb952be&count=5&expiryDate=0' \
      '&format=2&newLine=2 '

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '78.0.3904.87 Safari/537.36'
}


def get_ips():
    list_temp = []
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        # print(res.text)
        for line in res.text.splitlines():
            # print(line)
            list_temp.append(line)
        return list_temp
    elif res.status_code == 3001:
        print("appkey提取频繁，请按照所购买订单规定的频率进行合理提取。")
        time.sleep(10)
        return get_ips()
    else:
        print("获取代理ip失败")
        return []


if __name__ == '__main__':

    tem = get_ips()
    print(tem)
