# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 02:01:36 2023

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt

testcsv = pd.read_csv("yaprak\test.csv")
traincsv = pd.read_csv("yaprak\train.csv")
sample = pd.read_csv("yaprak\sample_submission.csv")

#kalsör içindeki verileri nasıl okuyacağımı bulamadım.
#ayrıca okusam bile nasıl tahmin yaptıracağımı anlamadım.