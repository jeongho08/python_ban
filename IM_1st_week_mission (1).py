# python 중급반 1주차 정규수업(10:00~12:00) mission
# -*- coding: utf-8 -*-

'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[기초반 마지막 시간 복습]
1. .super() 명령과 클래스 변수
2. 예외처리
'''

# [예외처리 이어서...]
## 에러 발생시키기 연습문제

## 예외처리 Mission: 영어단어 공부하기 문제를 'while문 + 예외 처리'로 풀어보자
'''
word_list = ['apple', 'banana', 'peach']

count = 0
i = 0
while True:
    word = input(word_list[i]+'\n')
    if word == word_list[i]:
        count += 1
    i += 1   



print("전체 문제 개수: ", len(word_list))
print("맞은 문제 개수: ", count)
print("틀린 문제 개수: ", len(word_list)-count)
'''
# [파일 입출력]
## 파일 입출력 연습문제1: 파일 쓰기(w: 새로쓰기 혹은 덮어쓰기)
file = open('/Users/yooeunju/python_ban/text.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    data = f'{i}번째 줄입니다.\n'
    file.write(data)
file.close()

## 파일 입출력 연습문제2: 파일 추가하기(a: 추가하기)


## 파일 입출력 연습문제3: 파일 읽기(r: 읽기)
## way1) readline 함수 사용(한 줄 씩 읽어오기)
file = open('/Users/yooeunju/python_ban/text.txt', 'w', encoding='utf-8')
while True:
    data = file.readline()
    print data == '':
    if data == '':
        break
## way2) readlines 함수 사용(모든
# 줄을 읽어와, 각 줄을 리스트의 요소로 반환)

file = open('/Users/yooeunju/python_ban/text.txt', 'w', encoding='utf-8')
datas = file.readlines()

file.close()
## way3) read 함수 사용(문서 전체를 하나의 문자열로 가져오기)
file = open('/Users/yooeunju/python_ban/text.txt', 'w', encoding='utf-8')
data = file.read()
print(data)
file.close()
print(type(data))
# [이벤트 처리]
## turtle 마우스 이벤트 처리 연습문제
## : 마우스로 랜덤한 turtle 스탬프를 찍는 프로그램을 작성해보자.
'''

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    
# turtleStamp 핸들링 함수: 거북이 스탬프 모양을 찍는 함수
def turtleStamp(x, y):
    # 거북이 숨기기
    # (x,y)좌표로 거북이 이동
    # 랜덤하게 거북이의 머리 방향 지정(0~360도)
    # 랜덤하게 거북이의 크기 설정(1~10)
    # 랜덤 r,g,b 값 가져오기(randomColor 함수 사용하기)
    # 스템프 색상 설정(랜덤 r,g,b 값 넣기)
    # 스템프 테두리 색성 설정(랜덤 r,g,b 값 넣기)
    # 스템프 찍기 명령

# 제목 달기 "거북이 도장 찍기"
# 도장 모양을 turtle으로 설정
# 속도 설정
# 펜 들기

# 왼쪽 마우스 클릭 시, 스탬프 찍기


'''

## turtle 마우스 이벤트 처리 Mission
## : 오른쪽 마우스 클릭 시 화면이 지워지는 기능을 추가해보자.
## turtle 마우스 이벤트 처리 Mission


## turtle 키보드 마우스 처리 연습문제
'''
import turtle as t
import random

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

# 방향키 위를 눌렀을 때의 핸들링 함수
def up():
    # 가려는 방향에 맞게 방향설정
    # 랜덤 색상 r,g,b 가져오기
    # 펜 색상 설정
    # 거북이의 색상도 같이 설정
    # 10만 큼 이동

# 방향키 아래키를 눌렀을 때의 핸들링 함수
def down():


# 제목 설정 "마리오의 별을 훔쳐먹은 거북이"
# 배경색을 검정(black)으로 설정하기
# 모양을 'turtle'로 설정
# 펜사이즈 10 설정

# up 이벤트 설정
# donw 이벤트 설정
# listen을 실행시켜 주어야 키 입력 모두가 실행되어 입력키에 반응함.


'''

## turtle 키보드 마우스 처리 Mission

