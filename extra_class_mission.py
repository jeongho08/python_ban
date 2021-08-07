# 기말고사 보강수업 3차
# 보강수업 주제: Today is "CASINO DAY!!!"
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!
'''

# Problem1: 아스키코드를 활용한 슬롯머신 문제
# ASCII 코드의 33~39번(총 7개)의 특수문자를 활용하여 슬롯머신 만들기
# 자세한 내용은 ppt 내용 참고


# Problem2: 동물레이싱
## case1: 우리가 배운 내용만을 사용한 코딩
'''
import turtle
import random

# 화면창 설정
win = turtle.Screen()
win.title('여기는 동물레이싱 경기장')
win.bgpic('별무리경기장.gif')

width = 1200
height = 800
offset = 50
win.setup(width, height)

# Turtle 객체의 이미지 추가
win.addshape('거북이.gif')
win.addshape('강아지.gif')
win.addshape('고양이.gif')

# 선수등록
Turtle = turtle.Turtle('거북이.gif')
puppy = turtle.Turtle('강아지.gif')
cat = turtle.Turtle('고양이.gif')

# 선수 출발선 이동
Turtle.penup()
Turtle.goto(-width/2+offset, -8/32*height)
puppy.penup()
puppy.goto(-width/2+offset, -10/32*height)
cat.penup()
cat.goto(-width/2+offset, -12/32*height)

# 달리기 시작!: 이 부분을 작성해 보자
# Hint1 - Turtle, puppy, cat은 결승선에 도착하기까지 달리도록 한다.
#         (결승선 x좌표:width/2-2*offset)
# Hint2 - x의 현재 좌표를 확인하는 방법: 변수(객체).xcor()
# Hint3 - 거북이는 랜덤하게 5~7의 거리를, 강아지는 3~9의 거리를, 고양이는 1~11의 거리를 이동한다.
#         (.forward()와 random.randint()를 활용하도록 하자)
# <code를 작성할 부분>

win.mainloop()
'''


## case2: (위의 문제점을 해결해 보도록 하자) thread를 사용한 경우
'''
def turtleRun():
    while(Turtle.xcor() < width/2 - 2*offset):
        Turtle.forward(random.randint(5, 7))

def puppyRun():
    while (puppy.xcor() < width / 2 - 2 * offset):
        puppy.forward(random.randint(3, 9))

def catRun():
    while (cat.xcor() < width / 2 - 2 * offset):
        cat.forward(random.randint(1, 12))

import random
import turtle
import threading

# 화면창 설정
win = turtle.Screen()
win.title('여기는 동물레이싱 경기장')
win.bgpic('별무리경기장.gif')

width = 1200
height = 800
offset = 50
win.setup(width, height)

# Turtle 객체의 이미지 추가
win.addshape('거북이.gif')
win.addshape('강아지.gif')
win.addshape('고양이.gif')

# 선수등록
Turtle = turtle.Turtle('거북이.gif')
puppy = turtle.Turtle('강아지.gif')
cat = turtle.Turtle('고양이.gif')

# 선수 출발선 이동
Turtle.penup()
Turtle.goto(-width/2+offset, -8/32*height)
puppy.penup()
puppy.goto(-width/2+offset, -10/32*height)
cat.penup()
cat.goto(-width/2+offset, -12/32*height)

# 경기 시작!
# 1. thread 생성
# <code를 작성할 부분1>

# 2. 출발!!
# <code를 작성할 부분2>

win.mainloop()
'''

# Problem3: 이상한 블랙잭 문제
# url: https://www.acmicpc.net/problem/2798
'''
import sys
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split(' ')))

# 이 부분을 작성하는 것이 mission
# [조건1]: 3중 for문을 활용할 것.
# [조건2]: 리스트 슬라이싱 or range함수를 활용하면 좋음.
# >> 코딩 결과는 위 사이트로 이동하여 직접 넣어보도록 하자 
# <code를 작성할 부분>


print(sum_number)
'''

# Problem4: 미로탈출 게임
'''
def drawRectangle(width,height,color): # 주어진 너비,높이,색상의 네모그리기
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.end_fill()

def drawButton(x,y,msg): # Button 시작점 x좌표, y좌표, 메시지
    t.penup()
    t.goto(x,y)     # 버튼 시작점 위치로 이동
    t.setheading(0) # 버튼 시작점 방향 초기화
    drawRectangle(button_width, button_height, button_color)
    t.goto(x+button_width/2,y-button_height)    # 네모 아래 중앙으로 이동
    t.pencolor('white')
    t.write(msg, align='center', font=('돋움체', 30)) # 텍스트 입력

def init():
    win.bgpic('') # 화면 지우기
    t.clear()     # 선 지우기
    drawButton(start_x,start_y,'START') # 시작 버튼 만들기
    drawButton(next_x,next_y,'NEXT')    # 다음 버튼 만들기
    drawButton(quit_x,quit_y,'QUIT')    # 종료 버튼 만들기

def checkButton(x,y):
    global stage                    # stage 전역변수 사용
    if (x>=start_x and
        x<=start_x+button_width and
        y<=start_y and
        y>=start_y-button_height):  # 시작 버튼 눌렀을 때
        stage = 1
        init()
        win.bgpic('mazeStage1.png')
    elif (x>=next_x and
          x<=next_x+button_width and
          y<=next_y and
          y>=next_y-button_height):  # 다음 버튼 눌렀을 때
        stage = stage + 1
        init()
        if stage == 2:
            win.bgpic('mazeStage2.png')
        else:
            win.bgpic('mazeStage3.png')
    elif (x>=quit_x and
          x<=quit_x+button_width and
          y<=quit_y and
          y>=quit_y-button_height):  # 종료 버튼 눌렀을 때
        win.bye()                    # 윈도우 닫기
    else:
        t.goto(x,y)
        t.pendown()
        t.pencolor('black')

stage = 0   # 미로 게임 스테이지 번호
window_width = 1200     # 전체 윈도우 너비
window_height = 800     # 전체 윈도우 높이
button_width = 150      # 버튼 너비
button_height = 50      # 버튼 높이
button_color = 'sky blue'   # 버튼 색상
start_x = 400   # 시작 버튼 시작점 x좌표
start_y = 200   # 시작 버튼 시작점 y좌표
next_x = 400    # 다음 버튼 시작점 x좌표
next_y = 100    # 다음 버튼 시작점 y좌표
quit_x = 400    # 종료 버튼 시작점 x좌표
quit_y = 0      # 종료 버튼 시작점 y좌표

import turtle
win = turtle.Screen()
win.setup(window_width, window_height)
t = turtle.Turtle()
t.speed(500)

init()  # 화면 및 선 지우고, 버튼 만들기

win.onclick(checkButton)    # 마우스 버튼 이벤트 발생 시 checkButton함수 실행
t.ondrag(t.goto)    # 마우스 드래그 시 거북이 객체 이동(선 긋기)

win.mainloop()
'''

# Problem5: 두더지 잡기 GAME
'''
def show(x,y):      # show함수: 랜덤 위치로 거북이를 이동시키는 함수
    global count
    count = count + 1
    t.hideturtle()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x,y)
    t.showturtle()

import random
import turtle
win = turtle.Screen()
win.setup(700, 700)
t = turtle.Turtle('turtle')
t.penup()
t.onclick(show)     # 이벤트 함수 onclick: 객체를 클릭했을 때, 지정한 event 함수 실행

def checkMinute():
    global time
    time += 1
    timer.clear()

    # 현재 타이머 시간 표시
    timer.write('경과시간: ' + str(time) + '초' + ', 잡은 개수:' + str(count))

    # 1초 후, countMiunute함수 호출하는 쓰레드 생성
    thread = threading.Timer(1, checkMinute())
    if time < 60:  # 1분이 지나면 타이머 및 카운팅 중지
        thread.start()

timer = turtle.Turtle()
timer.penup()
timer.goto(100, 200)
import threading
time = 0
count = 0

# 1분 시간 체크 쓰레드 생성
thread = threading.Thread(target=checkMinute())
thread.start()

win.mainloop()
'''