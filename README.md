# 프로세스 자원 소비 분석기 (Process Resource Monitor)

## 프로젝트 개요
이 프로그램은 실행 중인 프로세스들의 CPU와 RAM 사용량을 실시간으로 확인하고,
자원 소비가 높은 프로세스를 시각화하는 GUI 기반 시스템 모니터링 도구

## 주요 기능
- 1초 간격으로 자동 갱신되는 프로세스 목록
- 각 프로세스의 CPU 사용률 및 RAM 사용률 실시간 표시
- 자원 소비 상위 프로세스 기준 정렬
- System Idle Process 자동 제외
- CPU 사용률 0~100% 정규화 처리
- 버튼 클릭 시 CPU & RAM 시각화 (막대 + 선 그래프)

## GUI 화면
- tkinter 기반의 직관적인 사용자 인터페이스
- 실시간 자원 사용률을 표 형태로 표시

## 시각화 기능
- matplotlib으로 CPU 사용률을 막대그래프,
- RAM 사용률을 선그래프로 동시에 출력
- 그래프는 실시간이 아닌 정적 스냅샷 기반

## 사용 기술
- Python 3.x
- psutil (자원 수집)
- tkinter (GUI 구성)
- matplotlib (그래프 시각화)

## 파일 구성
- `processer.py` : 실행 코드

## 실행 방법
```bash
pip install psutil matplotlib


## 기타
- cross-platform 가능 (Windows, Mac, Linux)
- Python 설치만 되어 있으면 어디서든 실행 가능
