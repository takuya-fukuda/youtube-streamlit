from typing import Text
import PIL.Image
from PIL.Image import Image
import streamlit as st
import numpy as np
import pandas as pd
import random
import time

st.title('streamlit 超入門')

"""
# １章
"""

"""
## 準備
"""

"""
### streamlitでよく使用するモジュールライブラリ
```python
import PIL.Image
from PIL.Image import Image
import streamlit as st
import numpy as np
import pandas as pd
import random
import time
```
"""
st.write('あらかじめimportしておくことを推奨する')
st.write('上記コマンドの前にpipでライブラリのインストールが必要')

"""
# 2章
"""
"""
## streamlitの様々な使用方法
"""
"""
### 1.dataframeを使ってデータを表形式で出力してみる
```python
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df)
```
"""
st.write('実際になにか試しにデータを作成してみた。以下のように画面表示される')
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df)

"""
### 2.tableを使って表形式で出力してみる
```python
st.table(df)
```
"""
st.write('以下のように画面表示される')
st.table(df)

#以下は最大値にマーキングを施す
# st.table(df.style.highlight_max(axis=0))

"""
### 3.折れ線グラフのためのデータ準備
```
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

df
```
"""
st.write('以下の表示であればOK')
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

df

"""
### 折れ線グラフ
```python
st.line_chart(df)
```
"""
st.line_chart(df)
"""
### エリアチャート
```python
st.area_chart(df)
````
"""
st.area_chart(df)
"""
### 棒グラフ
```python
st.area_chart(df)
````
"""
st.bar_chart(df)

"""
### mappingの使用
#### 新宿付近の情報のマッピング
```python
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
df
st.map(df)
```
"""
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
df
st.map(df)

"""
### 画像表示
"""
#   st.write('Display Image')


im = PIL.Image.open("sample.jpg")
st.image(im, caption='sample', use_column_width=True)

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!!!'

#expanderの使い方
st.write('FAQ')
expander1 = st.beta_expander('問い合わせ1')
expander1.write('回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('回答')

#カラムレイアウト
left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

#intesractiveなウィジェット
#sidebarを使うと左横に表示される
#text = st.text_input('あなたの趣味を教えてください')
#50はスタートの値
#condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#'あなたの趣味：', text
#'コンディション：', condition

#sidebarを使うと左横に表示される
text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'あなたの趣味：', text
'コンディション：', condition


#selectboxで指定した数字がプルダウンできる。
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)
'あなたの好きな数字は、', option, 'です'

#チェックボックスで画像を表示する
if st.checkbox('Show Image'):
    im = PIL.Image.open("sample.jpg")
    st.image(im, caption='sample', use_column_width=True)














