# -*- coding: utf-8 -*-
# 7주차 보강2
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[7주차 정규수업 복습]
1. 리스트 제어하기(~7.리스트 정렬하기)
2. 리스트 mission1: turtle 모듈을 활용하여 RGB 구하기
3. 반복문의 개념과 연습문제
'''

# <! 저번시간에 빠트린 문제1>
## 리스트 mission2
## 다음은 1번~5번 학생의 1분간 턱걸이 개수이다
pull_up = [3, 16, 2, 5, 10, 7]
## 1번 문제: 7번째 학생의 턱걸이 개수가 9라고 할 때, 이를 리스트에 추가해보자
pull_up.append(9)
print(pull_up)
## 2번 문제: 2번 학생의 재측정 결과 20개의 턱걸이를 하였다. 리스트에 데이터를 수정해보자
pull_up[1]=20
print(pull_up)
## 3번 문제: 3~7번까지의 학생의 턱걸이 갯수만을 뽑아 temp 변수에 저장하고 출력해보자
temp = pull_up[2:]
print(temp)
## 4번 문제: 학생들의 턱걸이 횟수 데이터를 오름차순으로 정렬

pull_up.sort(reverse=False)
print(pull_up)
# <반복문 이어서...>
## while문 + continue 연습문제
## : continue 문을 활용하여 1~10까지 숫자 중 홀수만 출력하는 프로그램 작성
num = 0
while num <= 10 :
    num += 1        # num =
    if num % 2 == 0:
        continue
    print(num)
    num += 1  # num = num + 1


## 반복문 mission1-1: 원하는 단의 구구단만 출력하기
## for 반복문을 활용하여 출력을 원하는 구구단의 단 수를 입력받고, 1~9까지 곱한 구구단 출력하기
num = int(input("숫자를 입력하세요"))
for i in range(1, 10):
    print("%d * %d = %d" %(num, i, num*i))

## 반복문 mission1-2: 2~9단 모두 출력하기
## for 반복문을 활용하여, 2단~9단까지 모두 출력하기

for i in range(2, 10):
    print("[%d단]" %i)
    for j in range(1, 10):
        print("%d * %d = %d" % (i, j, i*j))
    print("------------------")

## 반복문 mission2-1: while문을 활용하여 반복문 mission1-1과 같은 결과를 출력해보자

i = 1
while i < 10:
    print("%d * %d = %d" %(num, i, num*i))
    i += 1



## 반복문 mission2-2: while문을 활용하여 반복문 mission1-2와 같은 결과를 출력해보자.
i = 2
while i < 10:
    print("")

## 반복문 mission3: 영단어 타자연습 프로그램
# -영타연습 Program-
# 1. 연습할 영단어가 담긴 리스트를 만든다.
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다
# 3. 프로그램 사용자는 단어를 그대로 입력한다.
# 4. 입력이 끝나면 전체 문제, 맞은 문제, 틀린 문제의 수가 출력된다.


## 반복문 mission4: turtle을 활용하여 무지개 그리기 (이후 함수에도 연개할 예정이므로 반드시 수행)
### for 반복문 Mission2: turtle 모듈을 활용하여 무지개 만들기
