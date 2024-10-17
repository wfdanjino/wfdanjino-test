import streamlit as st
import pandas as pd

# ログイン関数
def login(password):
    # 仮のパスワード "password123" と比較
    return password == "password123"

# パスワード入力
password_input = st.text_input("Enter Password", type="password")

# ログイン処理
if password_input:
    if login(password_input):
        st.success("Login successful!")
    else:
        st.error("Incorrect password. Please try again.")
        st.stop()  # パスワードが正しくない場合はアプリを停止

# ログイン後の処理
# ここから下はログイン成功後に実行される
st.title("Note Management App")

# ノートの選択
selected_note = st.sidebar.selectbox("Select Note", ["Note 1", "Note 2", "Note 3"])

# ノートの編集
note_content = st.text_area("Edit Note", key=selected_note)

# リアルタイムで記載した内容が保存されると仮定して、ここで保存処理を行う
# 実際にはデータベースやファイルに保存する必要があります
# 例: ファイルに保存
with open(f"{selected_note}.txt", "w", encoding="utf-8",errors="ignore") as file:
    file.write(note_content)

# ノートをテキストでエクスポートするボタン
if st.button("Export Note"):
    st.download_button(
        label="Download Note",
        data=note_content,
        file_name=f"{selected_note}_export.txt",
        key=selected_note,
    )
