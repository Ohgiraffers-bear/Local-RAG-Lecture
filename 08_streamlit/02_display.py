import streamlit as st
import pandas as pd

st.title("텍스트와 데이터 출력")

# 1. 텍스트 출력
st.header("1. 텍스트 출력")
st.write("일반 텍스트")
st.markdown("**굵은 글씨** 와 *기울임* 글씨")
st.code("print('코드 블록')", language="python")

# 2. 알림 메시지
st.header("3. 알림 메시지")
st.success("성공 메시지")
st.info("정보 메시지")
st.warning("경고 메시지")
st.error("오류 메시지")
