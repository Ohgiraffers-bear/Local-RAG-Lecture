import streamlit as st

# 기본 구조
st.title("Streamlit 기본")
st.write("Hello, Streamlit!")

# 즉시 실행해보기
if st.button("클릭하세요!"):
    st.success("버튼이 클릭되었습니다!")
