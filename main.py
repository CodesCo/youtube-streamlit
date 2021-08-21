import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'



left_column, right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1=st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2=st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3=st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

# https://github.com/CodesCo/youtube-streamlit.git

# opt=st.text_input('あなたの趣味を教えてください。')
# condition=st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの好きな趣味：',opt
# 'コンディション：',condition

# if st.checkbox('Show Image'):
#     image=Image.open('ote.png')
#     st.image(image,caption='otemachi',use_column_width=True)


# ctrl k ctrl cでコメント化　ctrl k ctrl uでコメント解除
# st.writeとしなくても''で囲むだけで文字列を表示できる。,で区切ると変数を表示できる。