import streamlit as st

st.title("레이아웃 구성하기")

# 1. 컬럼 레이아웃
st.header("1. 컬럼 레이아웃")
col1, col2 = st.columns(2)

with col1:
    st.write("왼쪽 컬럼")
    st.button("버튼 1")

with col2:
    st.write("오른쪽 컬럼")
    st.button("버튼 2")

# 2. 사이드바
st.sidebar.title("설정")
sidebar_option = st.sidebar.selectbox("옵션:", ["옵션1", "옵션2", "옵션3"])
st.sidebar.write(f"선택: {sidebar_option}")

# 3. 확장 가능한 섹션
st.header("3. 확장 섹션")
with st.expander("자세히 보기"):
    st.write("여기는 숨겨진 내용입니다!")
    st.code("print('숨겨진 코드')")

# 4. 탭
st.header("4. 탭")
tab1, tab2, tab3 = st.tabs(["탭1", "탭2", "탭3"])

with tab1:
    st.write("첫 번째 탭")
with tab2:
    st.write("두 번째 탭")
with tab3:
    st.write("세 번째 탭")
