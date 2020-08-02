# -*- coding: utf-8 -*-
import csv

list = [["Top Gun", "Risky Business", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"], 
        ["Training Day", "Man of Fire", "Fight"]]

with open("9-3.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    for row in list:
        w.writerow(row)