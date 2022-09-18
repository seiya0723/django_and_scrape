import requests,bs4
import time

import csv


TARGET_URL  = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=080&bs=040&ra=034&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&rn=6015"

TIMEOUT     = 10
HEADER      = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}

try:
    result  = requests.get(TARGET_URL, timeout=TIMEOUT, headers=HEADER)
    result.raise_for_status()
except Exception as e:
    print("ERROR_DOWNLOAD:{}".format(e))
else:
    soup    = bs4.BeautifulSoup(result.content, "html.parser")

    """
    lists   = soup.select("#js-bukkenList")
    for l in lists:
        print(l)
    """
    

    titles      = soup.select(".cassetteitem_content-title")
    images      = soup.select(".cassetteitem_object-item > img")
    addresses   = soup.select(".cassetteitem_detail-col1")
    stations    = soup.select(".cassetteitem_detail-col2")


    #物件が貸出中の部屋
    items   = soup.select(".cassetteitem-item")


    data    = []

    #要素数が同じであれば、zipでまとめてループできる。
    for title,image,address,station,item in zip(titles,images,addresses,stations,items):

        print("=====================================")


        print(title.text)
        print(image["rel"]) #属性の参照
        print(address.text)
        print(station.text.split())

        row = []
        row.append(title.text)
        row.append(image["rel"]) #属性の参照
        row.append(address.text)
        row.append(station.text.split())

        

        #一度スクレイピングした要素を更にスクレイピングする。
        #https://noauto-nolife.com/post/startup-python3-beautifulsoup4/

        item_soup   = bs4.BeautifulSoup(str(item), "html.parser")

        #tbodyの中のtdは部屋の情報。割り算(9で割った余り)をして階や間取り、賃料などの情報を取得する。
        item_elems  = item_soup.select("table > tbody > tr > td ")
        item_length = len(item_elems)

        for i in range(item_length):

            # 賃料は4番目(インデックス番号は3)なので、9で割った余りが3の時に出力できる
            if i%9 == 3:
                print(item_elems[i].text.split()) #空白を除去するため、.split()をつかう

            #TODO:この割り算方式を使って、間取りの画像、階、敷金礼金の情報、間取りを取得してみましょう。


        data.append(row)

        print("=====================================")

    #CSVへ書き込み
    #https://note.nkmk.me/python-csv-reader-writer/
    with open("./suumo.csv", "w") as f:
        writer  = csv.writer(f)
        writer.writerows(data)



