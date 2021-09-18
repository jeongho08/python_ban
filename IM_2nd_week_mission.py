# -*- coding: utf-8 -*-

# [이벤트 처리]
## turtle 마우스 이벤트 처리 연습문제
## : 마우스로 랜덤한 turtle 스탬프를 찍는 프로그램을 작성해보자.

'''
import turtle as t
import random
# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

# turtleStamp 핸들링 함수: 거북이 스탬프 모양을 찍는 함수
def turtleStamp(x, y):
    t.hideturtle()      # 거북이 숨기기
    t.goto(x, y)       #
    t.setheading(random.randint(0, 360))
    t.shapesize(random.randint(1, 10))
    r, g, b = randomColor()
    t.fillcolor(r, g, b)
    t.pencolor(r, g, b)
    t.stamp()
def clear_bg(x, y):
    t.clear()

t.title('거북이 도장 찍기')  # 제목 달기 "거북이 도장 찍기"
t.shape('turtle')  # 도장 모양을 turtle으로 설정
t.speed(0)  # 속도 설정
t.penup()  # 펜 들기

t.onscreenclick(turtleStamp, 1)  # 왼쪽 마우스 클릭 시, 스탬프 찍기
t.onscreenclick(clear_bg, 3)
t.mainloop()

'''
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



## turtle 마우스 이벤트 처리 Mission
## : 오른쪽 마우스 클릭 시 화면이 지워지는 기능을 추가해보자.
## turtle 마우스 이벤트 처리 Mission
'''
<turtle 마우스 이벤트 처리 연습문제를 복사해온 뒤, 기능을 추가해보자.>
'''

## turtle 키보드 이벤트 처리 연습문제
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
    t.setheading(90)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)
    t.foward(10)

def down():
    t.setheading(270)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)
    t.foward(10)

    
t.title('마리오의 별을 훔쳐먹은 거북이')
t.bgcolor('black')
t.shape('turtle')
t.pensize(10)

t.onkeypress
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
# down 이벤트 설정
# listen을 실행시켜 주어야 키 입력 모두가 실행되어 입력키에 반응함.
'''

import turtle as t
import random


def randomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


def up():
    t.setheading(90)  # 가려는 방향에 맞게 방향설정
    r, g, b = randomColor()  # 랜덤 색상 r,g,b 가져오기
    t.pencolor(r, g, b)  # 펜 색상 설정
    t.fillcolor(r, g, b)  # 거북이의 색상도 같이 설정
    t.forward(10)  # 10만 큼 이동


def down():
    t.setheading(270)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)
    t.forward(10)


def left():
    t.setheading(180)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)
    t.forward(10)


def right():
    t.setheading(0)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)
    t.forward(10)


def clear_bg():
    t.clear()


def close_window():
    t.bye()


# pygame.init()

t.title('마리오의 별을 훔쳐 먹은 거북이')
t.bgcolor('black')
t.shape('turtle')
t.pensize(10)

# 배경음악 넣기(pygame)
# bg_sound = pygame.mixer.Sound("D:\My_file\Github_asdfrv20\Python_deep\python_intermediate\mission_answer\Star.mp3")
# bg_sound.play(-1)

t.onkeypress(up, "Up")
t.onkeypress(down, "Down")
t.onkeypress(left, "Left")
t.onkeypress(right, "Right")
t.onkeypress(clear_bg, "space")
t.onkeypress(close_window, "Escape")

t.listen()  # listen을 실행시켜 주어야 키 입력 모두가 실행되어 입력키에 반응함.

t.mainloop()


## turtle 키보드 이벤트 처리 Mission
'''
<turtle 키보드 연습문제에서 left, right, space, ESC 버튼을 눌렀을 때 기능을 추가해보자.>

'''


# [Tkinter]
## Tkinter 시작하기


## Tkinter 시작하기: Window 창 설정하기


## Tkinter 위젯: Label() - 1
## Hello World를 포함한 GUI창 띄우기


## Tkinter 위젯: Label() - 1 변형
## Hello World를 포함한 GUI창 띄우기 + (koverwatch,50)으로 font 바꿔보기


## Tkinter 위젯 배치 관리자 연습문제


## Tkinter 위젯: PhotoImage()
## 저장된 이미지를 GUI화면에 출력해보자.

