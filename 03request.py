import requests

r = requests.get('https://www.baidu.com/img/bd_logo1.png')
# r.encoding = 'utf-8'
# print(r.text)
# print(r.content.decode())

f = open('baidu.png','wb')
f.write(r.content)
f.close()