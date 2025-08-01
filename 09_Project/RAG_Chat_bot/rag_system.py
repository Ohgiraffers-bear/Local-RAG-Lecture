import yaml
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# PDF 파일을 읽어오는 함수
def load_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    return docs

# 여러 PDF 파일들을 모두 읽어오는 함수
def load_all_pdfs(file_list):
    all_docs = []
    for file_path in file_list:
        docs = load_pdf(file_path)
        all_docs.extend(docs)
    return all_docs

# 긴 문서를 작은 조각으로 나누는 함수
def split_text(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    chunks = splitter.split_documents(docs)
    return chunks

# 한국어 임베딩 모델
def make_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name="nlpai-lab/KURE-v1",
        model_kwargs={"device":"cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )
    return embeddings

# FAISS 벡터 DB
def make_databse(chunks, embeddings):
    db = FAISS.from_documents(chunks, embeddings)
    return db

# 문서 검색기 만들기
def make_searcher(db):
    searcher = db.as_retriever(search_kwargs={"k":4})
    return searcher


# LLM 모델 준비
def make_ai():
    ai = ChatOllama(
        model="midm-2.0-base-instruct-q5_k_m",
        temperature=0
    )
    return ai


# 프롬프트
def load_prompt_from_yaml(yaml_path="prompt/RAG.yaml"):

    with open(yaml_path, "r", encoding="utf-8") as file:
        prompt_data = yaml.safe_load(file)

    return prompt_data["system_prompt"]


# 질문->답변 시스템
def make_qa_system(searcher, ai):
    prompt_text = load_prompt_from_yaml()
    prompt = PromptTemplate.from_template(prompt_text)

    qa_chain = (
        {"context": searcher, "question": RunnablePassthrough()}
        | prompt
        | ai
        | StrOutputParser()
    )

    return qa_chain

# 질문하고 답변받기
def ask_question(qa_chain, question):
    answer = qa_chain.invoke(question)

    return answer


# 전체 시스템을 한번에 엮기
def setup_everything(pdf_files):

    # PDF 읽기
    docs = load_all_pdfs(pdf_files)

    # 텍스트 나누기
    chunks = split_text(docs)

    # 임베딩 준비
    embeddings = make_embeddings()

    # 벡터 db 만들기
    db = make_databse(chunks, embeddings)

    # 리트리버(검색기)
    searcher = make_searcher(db)

    # AI
    ai = make_ai()

    # 질문 답변 시스템
    qa_chain = make_qa_system(searcher, ai)

    return qa_chain, searcher, db, embeddings

