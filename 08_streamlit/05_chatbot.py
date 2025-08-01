import streamlit as st
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="AI 챗봇",
    page_icon="❤️",
    layout="wide"
)

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 메인화면
st.title("AI 챗봇")
st.caption("간단한 챗봇 인터페이스 데모입니다.")

# 사이드바
with st.sidebar:
    st.title("챗봇 설정")

    if st.button("채팅기록 삭제"):
        st.session_state.messages = []
        st.rerun

    st.divider() # 구분선
    st.caption("made by bear.ohgiraffers")

# 채팅 메시지 표시 영역
chat_container = st.container(height=600)


with chat_container:
    # 기존 메시지들 표시
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            st.caption(message["timestamp"])

# 메시지 입력 (채팅 외부)
if prompt := st.chat_input("메시지를 입력하세요 ..."):
    # 사용자 메시지 추가
    timestamp = datetime.now().strftime("%H:%M:s")
    user_message = {
        "role": "user",
        "content": prompt,
        "timestamp": timestamp
    }
    st.session_state.messages.append(user_message)


    # AI 응답 (항상 같은 응답)
    def generate_response(user_input):
        """간단한 응답 생성 함수 동작! 같은 응답 반복"""
        return "흥미로운 질문이네요~!" \
    
    # AI 응답 생성 및 세션에 추가
    respnose = generate_response(prompt)

    timestamp = datetime.now().strftime("%H:%M:s")

    ai_message = {
        "role": "ai",
        "content": prompt,
        "timestamp": timestamp
    }

    st.session_state.messages.append(ai_message)

    # 페이지 새로고침으로 채팅컨테이너에서 모든 메시지 표시
    st.rerun()