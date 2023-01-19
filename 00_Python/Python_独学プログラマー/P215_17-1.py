# -*- coding: utf-8 -*-
import re

sentences = "The ghost that says boo haunts the loo."
m = re.findall(".oo", sentences)
print(m)
