# -*- coding: utf-8 -*-
# 必要なライブラリの呼び出し
import pandas as pd    #スクレイピング結果をデータフレーム形式でcvsファイルに保存するため
import pprint    #データフレームの一部を表示するため
from bs4 import BeautifulSoup  #取得したWebページの情報の解析と抽出
import requests     #Webページの情報の取得
import urllib       #キーワードのurlエンコード取得

#検索ワード「タピる」を文字変換して検索結果ページのurlの間に挿入
s = "タピる"
s_quote = urllib.parse.quote(s)
url_b4 = 'https://news.google.com/search?q=' + s_quote + '&hl=ja&gl=JP&ceid=JP%3Aja'

#検索結果ページの情報を取得
res = requests.get(url_b4)
soup = BeautifulSoup(res.content, "html.parser")

#すべての記事部の情報を選択
articles = soup.select(".xrnccd")

#各記事の情報をfor　～　enumerate分で繰り返し取得してリストに代入
news = list()   #代入のための空のリストを作成

for i, entry in enumerate(articles, 1):
    title = entry.find("h3").text
    summary = entry.find("span").text
    summary = title + "。" + summary
    #url_elm = entry.find("a")を下記に変更
    url_elm = entry.find("article")
    link = url_elm.get("jslog")
    link = link.lstrip("85008; 2:")     #左端削除
    link = link.rstrip("; track:click") #右端削除
    time_elm = entry.find("time")
    try:    #例外処理
        ymd = time_elm.get("datetime")
    except AttributeError:
        ymd = "0000-00-00"
    ymd = ymd[0:10]
    ymd = ymd.replace("-", "/")     #置換
    sortkey = ymd[0:4] + ymd[5:7] + ymd[8:10] #年月日でのソート用

    tmp = {             #辞書型で格納
        "title": title,
        "summary": summary,
        "link": link,
        "published": ymd,
        "sortkey": sortkey
        }

    news.append(tmp)  #各記事の情報をリストに追加

    #データフレームに変換してcsvファイルで保存
    news_df = pd.DataFrame(news)
    pprint.pprint(news_df.head())  #最初の5行を表示してデータ確認 
    filename = s + ".csv"
    news_df.to_csv(filename, encoding='utf-8-sig', index=False) 
