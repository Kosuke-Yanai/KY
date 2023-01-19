# -*- coding: utf-8 -*-

myself = {"身長":"173.0", 
          "体重":"58.0", 
          "好きな色":"緑"}

inquiry = input("何が知りたい？:")

if inquiry not in myself:
    print("それは教えられない")    
else:
    print(myself[inquiry])
