# Python 개발환경 설정 가이드
이 문서는 Python 개발을 위한 환경을 설정하는 단계별 가이드입니다.
---

## 목차
1. Miniforge 환경설정
2. VSCode 설치
3. Jupyter Notebook 설치
---

## 1. Miniforge 환경설정

### 1.1 Miniforge란?

Miniforge는 오픈소스 중심의 `conda-forge` 채널을 사용하는 경량화된 Python 패키지 및 환경 관리 도구입니다.

### 1.2 설치

아래의 링크에서 필요한 파일 다운로드

[Miniforge공식사이트](https://conda-forge.org/download/)


### 1.3 가상환경 생성 및 관리
```bash
# 새로운 가상환경 생성 (예: dev_env)
conda create -n dev_env python=3.11 -y

# 가상환경 활성화
conda activate dev_env

# pip으로 설치
pip install jupyter notebook

# 가상환경 비활성화
conda deactivate
```

---
## 2. VSCode 설치
### 2.1 설치
[공식 사이트](https://code.visualstudio.com/)에서 설치 가능합니다.

### 2.2 필수 확장(Extensions) 설치
- python
- jupyter

---