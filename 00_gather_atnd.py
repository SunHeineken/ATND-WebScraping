import fasttext as ft
import utils

titles, descs = utils.titles_desctiptions('DeepLearning')

titles_txt = ' '.join(titles)

t = utils._split_to_words(titles_txt, to_stem=True)

# 重複削除
uni_t = list(set(t))

# ユニークな文字ごとにカウントしたリストを作成
cnt = []
for word in uni_t:
    cnt.append(t.count(word))

##### 分析
# numpy

import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()
df['words']=uni_t
df['cnt']=cnt

# 並べ替え
df = df.sort_values('cnt', ascending=False)

# 上位20件抽出
df2 = df.iloc[:20, ]

df2.plot(x='words', y='cnt', kind='bar')
plt.show()