# 7주차 1차 (토요일 12:00~2:00) 보강수업 answer

# Problem1: turtle과 반복문을 활용하여 별모양 그리기
# 이제는 for문으로 그릴 수 있다!
## [Hint에 없는 필요 명령어]
## t.forward(): ()안의 거리만큼 전진
## t.right(): ()안의 각도만큼 현재 각도에서 오른쪽으로 회전
## t.left(): ()안의 각도만큼 현재 각도에서 왼쪽으로 회전
'''
import turtle

win = turtle.Screen()
win.setup(500, 500)
t = turtle.Turtle('turtle')

for i in range(5):
    t.forward(100)
    t.right(144)
    t.forward(100)
    t.left(72)

turtle.mainloop()
'''

# Problem2: factorial 계산하기
# ※ factorial이란?: 1에서 시작하여 "어떤 범위에 있는 모든 정수를 곱하는 것"
'''
num = int(input("숫자를 입력하세요>> "))

print("결과: 1", end='')
facto = 1
for i in range(2, num+1):
    facto = i * facto
    print(f"*{i}", end='')
print(f'={facto}')
'''

# Problem3: 유클리드 알고리즘으로 최대공약수 구하기(GCD: Greatest Common Divisor)
## [유클리드의 GCD 알고리즘] - while문 사용하기
## 1. 두 수 가운데 큰 수를 x, 작은 수를 y라고 한다.
## 2. y가 0이면 최대 공약수는 x와 같고 알고리즘을 종료한다.
## 3. r <- x % y
## 4. x <- y
## 5. y <- r
'''
x = int(input("첫번째 정수를 입력하세요: "))
y = int(input("두번째 정수를 입력하세요: "))

if x < y:
    x, y = y, x

while (y != 0):
    r = x % y
    x, y = y, r
print(f"최소 공약수는 {x}입니다")
'''

# Problem4: 아스키코드를 활용한 슬롯머신 문제
# ASCII 코드의 33~39번(총 7개)의 특수문자를 활용하여 슬롯머신 만들기
# >> 시간상 다음 시간에 계속

# Problem5: 달팽이 문제(for문으로 풀면 안풀리는 문제)
# for문과 알고리즘으로 풀이하는 방법 모두해볼 것
# 코딩테스트 사이트 같이 알려주기 & Hint 많이 줄 것!!
# 사이트에 직접 해볼 수 있도록 하기

# 사이트: https://www.acmicpc.net/problem/2869
# 시간측정: import time // start = time.time() // print("time: ", time.time()-start)
# 조건1: 입력1>> 2 1 5 [결과: 4] // 입력2>> 5 1 6 [결과: 2] // 입력3>> 2 1 10000000 [결과: 9999901]
# 조건2: 위 조건1의 모든 입력에 대한 수행시간이 1초 이내에 완료
# Hint1: .split(' ')
# Hint2: import math // .ceil() 사용하기

## 1. for문으로 작성한 경우
'''
import time

temp = input('')

start = time.time()
temp = temp.split(' ')

for i in range(3):
    temp[i] = int(temp[i])
A = temp[0]
B = temp[1]
V = temp[2]

count = 1
while V >= 0:
    V = V - A
    if V <= 0:
        break
    V = V + B
    count += 1
print(count)
print('time: ', time.time()-start)
'''

## 2. 공식을 세워 연산한 경우
'''
import math
import time

temp = input('')

start = time.time()
temp = temp.split(' ')

for i in range(3):
    temp[i] = int(temp[i])
A = temp[0]
B = temp[1]
V = temp[2]

result1 = 2 + math.floor((V-A)/(A-B))
result2 = 1 + math.ceil((V-A)/(A-B))
result = 1 + (V-A)/(A-B)

print(result1)
print(result2)
print(result)
print("time: ", time.time()-start)
'''

## 3. 홈페이지에서 채점을 받고 싶다면?
## import sys // A, B, V = map(int, sys.stdin.readline().split())
'''
import math
import sys
import time

A, B, V = map(int, sys.stdin.readline().split())

result = 1 + math.ceil((V-A)/(A-B))

print(result)
print("time: ",  time.time()-start)
'''

