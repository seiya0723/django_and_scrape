import requests,bs4

ID      = "asahina"
PASS    = "seiya0723"

URL     = "http://127.0.0.1:8000/"
LOGIN   = URL + "admin/login/?next=/admin/"


TIMEOUT = 10
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}


#TIPS:Djangoに対してrequestsライブラリからPOST文を送信する方法
#参照元:https://www.it-swarm-ja.com/ja/python/python-requests%e3%81%a7csrftoken%e3%82%92%e6%b8%a1%e3%81%99/1070253083/

#(1) セッションを維持する(セッションメソッドからオブジェクトを作る)
client = requests.session()
client.get(LOGIN,timeout=TIMEOUT,headers=HEADERS)


#(2) CSRFトークンを手に入れ、投稿するデータを辞書型で生成
if 'csrftoken' in client.cookies:
    csrftoken = client.cookies['csrftoken']

login_data   = { "csrfmiddlewaretoken":csrftoken,
                 "username":ID,
                 "password":PASS
                 }

#(3) ログインする
r   = client.post(LOGIN,data=login_data,headers={"Referer":LOGIN})
print(r)



#(4) 管理サイトからデータを投稿する

#CSRFトークンを入れ直す。
if 'csrftoken' in client.cookies:
    csrftoken = client.cookies['csrftoken']

post_data   = { "csrfmiddlewaretoken":csrftoken,
                "name":"requestより",
                "comment":"こんなふうにrequestsからコメントを送信できる"
                }

r   = client.post("http://127.0.0.1:8000/admin/bbs/topic/add/" , data=post_data)
print(r)

