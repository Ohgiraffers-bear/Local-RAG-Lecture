import streamlit as st
from datetime import datetime
from rag_system import setup_everything, ask_question

# 화면 설정
st.set_page_config(
    page_title="군 관련 AI 챗봇",
    page_icon="🎖️",
    layout="wide"
)

# 앱 상태 관리
if "messages" not in st.session_state:
    st.session_state.messages = []

if "qa_system" not in st.session_state:
    st.session_state.qa_system = None

if "is_ready" not in st.session_state:
    st.session_state.is_ready = False

# PDF 파일 위치
PDF_FILES = [
    "data/Soldier-Benefits-Guide.pdf"
]

# AI 시스템 자동 준비하기
@st.cache_resource
def auto_start_system():
    qa_system, searcher, db, embeddings = setup_everything(PDF_FILES)
    return qa_system, searcher, db, embeddings

# AI에게 질문하기
def get_ai_answer(question):
    return ask_question(st.session_state.qa_system, question)

# 메인 화면
st.title("🎖️ 병 복지 길라잡이 AI 챗봇")
st.caption("2025 병 복지 길라잡이 기반 AI 어시스턴트")

# 시스템 자동 시작
if not st.session_state.is_ready:
    with st.spinner("🤖 AI 챗봇을 준비하는 중입니다... 잠시만 기다려주세요!"):
        try:
            qa_system, searcher, db, embeddings = auto_start_system()
            
            # 준비 완료
            st.session_state.qa_system = qa_system
            st.session_state.is_ready = True
            
            # 첫 인사말
            welcome = {
                "role": "assistant",
                "content": "안녕하세요! 🎖️\n\n군 관련 문서 AI 챗봇입니다.\n\n• 2025 병 복지 길라잡이\n\n무엇이든 궁금한 것을 물어보세요!",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            }
            st.session_state.messages.append(welcome)
            
            st.success("✅ AI 챗봇 준비 완료!")
            st.rerun()
            
        except Exception as e:
            st.error(f"❌ 시스템 준비 중 문제가 발생했습니다: {str(e)}")
            st.info("페이지를 새로고침해서 다시 시도해주세요.")

# 사이드바
with st.sidebar:
    st.title("🎖️ 설명")
    
    # 병 복지 길라잡이 설명
    with st.expander("📖 2025 병 복지 길라잡이란?"):
        st.markdown("""
        ### 2025 병 복지 길라잡이
        
        **병 복지 길라잡이**는 장병들의 군 생활에 도움이 되는 다양한 복지제도와 
        혜택을 안내하는 종합 가이드북입니다.
        
        #### 활용 방법
        이 챗봇을 통해 병 복지 길라잡이의 내용에 대해 
        자유롭게 질문하실 수 있습니다.
        
        예시 질문:
        - 병사 월급은 얼마인가요?
        - 자기개발 지원제도에는 어떤 것들이 있나요?
        - 군 복무 중 학점 이수는 어떻게 하나요?
        """)

    # 상태 보기
    if st.session_state.is_ready:
        st.success("✅ 준비됨")
    else:
        st.info("🤖 준비 중...")
    
    st.divider()
    st.caption("made by bear.ohgiraffes")

# 채팅 화면
if st.session_state.is_ready:
    chat_box = st.container(height=600)
    
    with chat_box:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
                st.caption(f"⏰ {msg['timestamp']}")
    
    # 질문 입력
    if question := st.chat_input("질문을 입력하세요..."):
        # 사용자 질문 추가
        time_now = datetime.now().strftime("%H:%M:%S")
        user_msg = {
            "role": "user",
            "content": question,
            "timestamp": time_now
        }
        st.session_state.messages.append(user_msg)
        
        # AI 답변 생성p
        with st.spinner("🤔 답변을 생각하는 중..."):
            answer = get_ai_answer(question)
        
        # AI 답변 추가
        ai_time = datetime.now().strftime("%H:%M:%S")
        ai_msg = {
            "role": "assistant",
            "content": answer,
            "timestamp": ai_time
        }
        
        st.session_state.messages.append(ai_msg)
        
        # 화면 새로고침
        st.rerun()
else:
    # 준비 중일 때 표시할 내용
    st.info("🤖 AI 챗봇을 준비하고 있습니다. 곧 이용하실 수 있습니다!")
