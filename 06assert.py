# 描述：利用断言处理请求异常；利用retrying模块重新请求
import requests
from retrying import retry

# 模拟浏览器headers
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
@retry(stop_max_attempt_number=3)
def _parse_url(url):
    r = requests.get(url, headers=headers, timeout=5)
    assert r.status_code == 200
    return r.content.decode() # 返回网页字符串

def parse_url(url):
    try:
        html = _parse_url(url)
    except Exception as e:
        print('出错了')
        html = None
    return html

if __name__  ==  '__main__':
    html = parse_url('http://www.baidu.com')
    if html is None:
        print(html)
        print('请求失败！')
    else:
        print(html)
        print('请求完成:)')