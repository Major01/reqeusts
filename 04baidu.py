#描述：requests模块post爬取 百度翻译接口
import requests
import json

post_url = ('http://fanyi.baidu.com/langdetect')

post_data = {
    'query':'人生苦短'
}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}

r = requests.post(post_url, headers=headers, data=post_data)

dict_response = json.loads(r.content.decode())
print(dict_response)
