import streamlit as st
import random

st.title("じゃんけんゲーム")

choices = ["グー", "チョキ", "パー"]
user_choice = st.radio("あなたの選択", choices)

if st.button("勝負！"):
    computer_choice = random.choice(choices)
    st.write(f"コンピュータの選択: {computer_choice}")

    if user_choice == computer_choice:
        st.write("🤝 引き分け！")
    elif (user_choice == "グー" and computer_choice == "チョキ") or (user_choice == "チョキ" and computer_choice == "パー") or (user_choice == "パー" and computer_choice == "グー"):
        st.write("🎉 あなたの勝ち！")
    else:
        st.write("😢 あなたの負け！")
