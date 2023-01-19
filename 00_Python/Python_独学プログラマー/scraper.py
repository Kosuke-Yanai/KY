# -*- coding: utf-8 -*-
import feedparser
import urllib
import json
import pprint

s = "国内"
s_quote = urllib.parse.quote(s)
url = "https://news.google.com/news/rss/search/section/q/" + s_quote + "/" + s_quote + "?ned=jp&amp;hl=ja&amp;gl=JP"
d = feedparser.parse(url)
news = list()

for i, entry in enumerate(d.entries, 1):

    p = entry.published_parsed
    sortkey = "%04d%02d%02d%02d%02d%02d" % (p.tm_year, p.tm_mon, p.tm_mday, p.tm_hour, p.tm_min, p.tm_sec)

    tmp = {
        "no": i,
        "title": entry.title,
        "summary": entry.summary,
        "link": entry.link,
        "published": entry.published,
        "sortkey": sortkey
    }

    news.append(tmp)

pprint.pprint(news[0:1])