import streamlit as st

st.title("위젯 사용하기")

# 1. 입력 위젯
st.header("1. 입력 위젯")
name = st.text_input("이름을 입력하세요:")
age = st.slider("나이:", 0, 100, 25)
color = st.selectbox("좋아하는 색:", ["빨강", "파랑", "초록"])

# 2. 버튼과 체크박스
if st.button("인사하기"):
    st.balloons()
    st.write("안녕하세요!")

agree = st.checkbox("동의합니다")
if agree:
    st.write("감사합니다!")
