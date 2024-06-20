import streamlit as st
from gtts import gTTS
import os

# Streamlit アプリの構成
st.title('テキスト読み上げアプリ')

# テキスト入力
text_input = st.text_area("テキストを入力してください:")

# 再生ボタン
if st.button('再生'):
    if text_input:
        tts = gTTS(text=text_input, lang='ja', slow=False)
        tts.save("output.mp3")
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
        audio_file.close()
        os.remove("output.mp3")

# 停止ボタン
if st.button('停止'):
    st.warning("停止機能はサポートされていません。")









