# -*- coding: utf-8 -*-
import csv

list = [["トップガン", "リスキービジネス", "マイノリティ・リポート"],
        ["タイタニック", "ザレブナント", "インセプション"], 
        ["トレーニングデイ", "マンオブファイア", "ファイト"]]

with open("9-4.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for row in list:
        w.writerow(row)