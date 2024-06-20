import streamlit as st
from gtts import gTTS
import os

# キャッシュディレクトリを作成
if not os.path.exists("cache"):
    os.makedirs("cache")

# Streamlit アプリの構成
st.title('テキスト読み上げアプリ')

# テキスト入力
text_input = st.text_area("テキストを入力してください:")

# 再生ボタン
if st.button('再生'):
    if text_input:
        tts_file = f"cache/{hash(text_input)}.mp3"
        if not os.path.exists(tts_file):
            try:
                tts = gTTS(text=text_input, lang='ja', slow=False)
                tts.save(tts_file)
            except Exception as e:
                st.error(f"音声生成に失敗しました: {e}")
                tts_file = None
        if tts_file:
            audio_file = open(tts_file, "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
            audio_file.close()

# 停止ボタン
if st.button('停止'):
    st.warning("停止機能はサポートされていません。")











