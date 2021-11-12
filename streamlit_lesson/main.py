import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Stremlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

'Hi'
time.sleep(1)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

# df = pd.DataFrame(
#    np.random.rand(100,2)/[50, 50] +[35.69, 139.70],
#    columns=['lat', 'lon']
# )

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)
# st.table(df.style.highlight_max(axis=0))

# st.line_chart(df)
# st.map(df)

# if st.checkbox('Show Image'):
#    img = Image.open('pictures/liverpool.jpg')
#    st.image(img, caption='Liverpool', use_column_width=True)


# option = st.selectbox(
#    'Select Number',
#    list(range(1,11))
# )
# 'Your number is', option

st.sidebar.write('Sidebar')
text = st.sidebar.text_input('What is your hobby?')
condition = st.sidebar.slider('How about your condition', 0, 100, 50)

'Your hobby is', text
'Your condition is', condition

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ回答1')
expander.write('問い合わせ回答2')

"""
# 章
## 節
### 項

```python
a = np.array([1,2])
```

"""