import streamlit as st
import pyttsx3
import threading
import queue

# グローバル変数
q = queue.Queue()
is_playing = False

# テキスト読み上げ関数
def speak_text():
    global is_playing
    while True:
        text, rate = q.get()
        if text is None:
            break
        is_playing = True
        engine = pyttsx3.init()  # エンジンの再初期化
        engine.setProperty('rate', rate)
        engine.say(text)
        engine.runAndWait()
        is_playing = False
        q.task_done()

# スレッドの開始
threading.Thread(target=speak_text, daemon=True).start()

# Streamlit アプリの構成
st.title('テキスト読み上げアプリ')

# テキスト入力
text_input = st.text_area("テキストを入力してください:")

# 音声速度の調整
rate = st.slider('音声のスピードを調整してください', min_value=50, max_value=300, value=150)

# 再生ボタン
if st.button('再生'):
    if not is_playing:
        q.put((text_input, rate))

# 停止ボタン
if st.button('停止'):
    if is_playing:
        q.put((None, None))  # キューに終了シグナルを追加
        is_playing = False








