# 8주차 정규수업(10:00~12:00) answer

# 저번 시간에 못 다한 반복문 마지막 Mission
## 반복문 mission4: turtle을 활용하여 무지개 그리기 (이후 함수에도 연개할 예정이므로 반드시 수행)
### for 반복문 Mission2: turtle 모듈을 활용하여 무지개 만들기
'''
import turtle

# 변수 및 객체 선언
win = turtle.Screen()
t = turtle.Turtle('turtle')
t.shapesize(10)
rainbow_size = 500         # 무지개 크기(너비)
pen_size = 30              # 펜 굵기
rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']      # 활용할 색상 지정
t.speed(10)                # 거북이 속도 설정 (1~10 숫자가 클수록 빠름, but 0은 가장 빠른 속도)

# 펜 초기 설정
t.pensize(pen_size)

# for 반복문 실행(무지개 그리기)
for i in range(7):
    t.setheading(90)
    t.penup()
    t.setpos(rainbow_size/2 - i*pen_size, 0)
    t.pencolor(rainbow_color[i])
    t.pendown()
    t.circle(rainbow_size/2 - i*pen_size, 180)
turtle.mainloop()
'''

# [함수]
##: 여러개의 명령어들을 묶어서 한꺼번에 처리할 수 있도록 만든 하나의 명령어 묶음에 이름을 붙인 것.
## 문법: def 함수이름(매개변수1, 매개변수2, ...):
##         명령어 블럭
##         return 반환값

## docstring: 함수에 대한 설명을 나타내는 문장

## 연습문제1: 입력X, 출력X인 함수
## >> 함수를 호출하면 별모양을 그리는 DrawStar_100()
'''
import turtle
def DrawStar_100():
    """
    한 변의 길이가 100인 별을 그리는 함수
    """
    t = turtle.Turtle("turtle")
    for i in range(5):
        t.forward(100)
        t.right(144)
        t.forward(100)
        t.left(72)

win = turtle.Screen()
DrawStar_100()
win.mainloop()
'''
## 연습문제2: 입력O, 출력X인 함수
## >> 한 변의 길이를 입력하면, 그 한변의 길이를 가지는 별을 그리는 DrawStar()
'''
import turtle
def DrawStar(length):
    """한 변의 길이가 length인 별을 그리는 함수"""
    t = turtle.Turtle("turtle")
    for i in range(5):
        t.forward(length)
        t.right(144)
        t.forward(length)
        t.left(72)

win = turtle.Screen()
DrawStar(200)
win.mainloop()
'''
## 연습문제3: 입력X, 출력O인 함수
## >> 1~100까지 랜덤한 정수 1개를 반환하는 getRandomNum()
'''
import random
def getRandomNum():
    """1~100사이의 랜덤한 수를 반환하는 함수"""
    return random.randint(1,100)

num = getRandomNum()
print(num)
'''
## 연습문제4: 입력O, 출력O인 함수
## >> a,b를 입력하면 두 수의 합을 반환하는 add()
'''
def add(a,b):
    """입력된 a와 b를 더한 결과를 반환하는 함수"""
    return a+b

X = add(100, 55)
print(X)
'''

## 함수 Mission: 앞서 반복문 Mission4에서 그린 무지개를 "함수"로 만들어보자
## 조건은 ppt 16p참고
'''
# draw_rainbow() 함수 정의하기
def draw_rainbow(t, rainbow_size, pen_size, x, y):
    """
    입력한 t가 rainbow_size크기의 지름과 pen_size 두께의 색상띠를 가지는 무지개를 (x,y)에 그리는 함수
    :param t: 그림을 그릴 turtle 객체
    :param rainbow_size: 무지개의 지름
    :param pen_size: 무지개를 그릴 펜의 두께
    :param x: 무지개가 그려질 x좌표
    :param y: 무지개가 그려질 y좌표
    :return:
    """
    # 설정
    rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
    t.pensize(pen_size)

    # 그리기
    for i in range(7):
        t.setheading(90)
        t.penup()
        t.setpos(x+(rainbow_size / 2 - i * pen_size), y)
        t.pencolor(rainbow_color[i])
        t.pendown()
        t.circle((rainbow_size / 2 - i * pen_size), 180)

import turtle

win = turtle.Screen()
win.screensize(1000,1000)
t = turtle.Turtle('turtle')
t.speed(0)

draw_rainbow(t, 500, 30, 200, 200)
draw_rainbow(t, 500, 30, -100, -150)
draw_rainbow(t, 100, 8, 100, 100)
draw_rainbow(t, 200, 10, -20, -300)
draw_rainbow(t, 180, 15, 200, -40)
draw_rainbow(t, 100, 5, -50, 70)
draw_rainbow(t, 80, 3, -200, -100)
draw_rainbow(t, 50, 3, -100, -100)
draw_rainbow(t, 50, 3, 70, -30)

turtle.mainloop()
'''



# [오늘의 추가문제!(8주차): 분해합]
## url: https://www.acmicpc.net/problem/2231
'''
import copy

N = int(input())

# N의 가장 작은 생성자를 구하는 알고리즘 
result = N
temp = 0
for number in range(N):
    dummy = copy.copy(number)
    split_numbers = []
    while dummy >= 10:
        split_numbers.append(dummy%10)
        dummy = dummy//10
    split_numbers.append(dummy)
    
    # 생성자 후보의 분해합 구한 후, 최솟값일 때 대입
    temp = number+sum(split_numbers)
    if N == temp and number<result:
         result = number
if result == N:
    result = 0

print(result)
'''