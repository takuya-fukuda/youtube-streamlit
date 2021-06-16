from typing import Text
import PIL.Image
from PIL.Image import Image
import streamlit as st
import numpy as np
import pandas as pd
import random
import time

st.title('streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df)

st.table(df)

# st.table(df.style.highlight_max(axis=0))
"""
# 章
## 節
### コードの表示の仕方
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

df

"""
### 折れ線グラフ
"""
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

"""
###mapping
####新宿付近の情報のマッピング
"""
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
df
st.map(df)

"""
###画像表示
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
#left_column, right_column = st.beta_columns(2)
#button = left_column.button('右カラムに文字を表示')
#if button:
#    right_column.write('ここは右カラム')

#intesractiveなウィジェット
#sidebarを使うと左横に表示される
#text = st.text_input('あなたの趣味を教えてください')
#50はスタートの値
#condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#'あなたの趣味：', text
#'コンディション：', condition

#sidebarを使うと左横に表示される
#text = st.sidebar.text_input('あなたの趣味を教えてください')
#condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
#'あなたの趣味：', text
#'コンディション：', condition


#selectboxで指定した数字がプルダウンできる。
#option = st.selectbox(
#    'あなたが好きな数字を教えてください',
#    list(range(1,11))
#)
#'あなたの好きな数字は、', option, 'です'

#チェックボックスで画像を表示する
#if st.checkbox('Show Image'):
#    im = PIL.Image.open("sample.jpg")
#    st.image(im, caption='sample', use_column_width=True)














