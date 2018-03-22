#描述：requests模块post爬取 百度翻译接口
import requests
import json

post_url = 'https://fanyi.baidu.com/extendtrans'

en = input('请输入你要翻译的内容：')
post_data = {
    'query': en,
    'from': 'zh',
    'to': 'en'
}
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}

r = requests.post(post_url, headers=headers, data=post_data)

dict_response = json.loads(r.content.decode())
print('要翻译的内容是',en,'翻译为', dict_response['data']['st_tag'])
