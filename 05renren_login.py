import requests

# 模拟登录人人网
session = requests.session()

post_url = 'http://www.renren.com/PLogin.do'
post_data = {'email':'mr_mao_hacker@163.com','password':'alarmchime'}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}

session.post(post_url, data=post_data, headers=headers)
r = session.get('http://www.renren.com/327550029/profile')
f = open('renren.html', 'w', encoding='utf-8')
f.write(r.content.decode())
f.close()