# 7주차(정규 수업) answer

# 수업할 내용: 리스트 제어하기5~7, 리스트 mission, 반복문(for, while), 함수

# [리스트 자료형] - 6주차 이어서...
youtuber = ['10월 악토', "로빈하르트", "우왁굳", "T1 Faker", "논리왕전기", "나무늘보"]
print(youtuber)

## 리스트 제어하기1: 데이터 추가
## 방법: 리스트이름.append('추가할문자열')
## 연습문제>> 문자열에 수진썜이 좋아하는 유튜버 "승우아빠"를 추가해보자.
youtuber.append("승우아빠")
print(youtuber)

## 리스트 제어하기2: 인덱싱
## 방법: 리스트이름[인덱스 번호], 여기서 인덱스 번호는 0부터 시작에 주의!
## python의 순서를 가진 것들은 기본 0부터 시작!!
## 연습문제>> 만들어진 유투버 리스트에서 내가 가장 좋아하는 유튜버만 출력해보자
print(youtuber[6])

## 리스트 제어하기3: 데이터 수정하기
## 방법: 리스트이름[인덱스 번호] = '새로넣을 문자열'
## 연습문제>> 내가 가장 좋아하는 유투버의 이름을 2번째로 좋아하는 유튜버의 이름으로 바꿔보자
youtuber[6] = '녹두로'
print(youtuber)

## 리스트 제어하기4: 데이터 삭제하기
## 방법: del 리스트이름[삭제할인덱스번호]
## 연습문제>> 아쉽지만(ㅎㅎ) 선생님이 추가한 유투버를 리스트에서 삭제해보자.
del youtuber[6]
print(youtuber)

## 리스트 제어하기5: 리스트 슬라이싱
## 방법: 리스트이름[처음:끝+1]
## 연습문제>> 처음~3번쨰, 2번째~끝, 3번째~4번째에 위치한 유투버들만, 그리고(':'를 활용하여) 리스트 전체을 출력해보자.
'''
print("-리스트 슬라이싱")
print(youtuber[:3])
print(youtuber[1:])
print(youtuber[2:3])
print(youtuber[:])
'''

## 리스트 제어하기6: 리스트 길이 구하기
## 방법: len(리스트이름)
## 연습문제>> 현재 리스트에 포함된 데이터의 개수를 구해보자
'''
print("-리스트 길이 구하기")
print(len(youtuber))
'''

## 리스트 제어하기7: 리스트 정렬하기
## 방법1: 리스트이름.sort()  <- 오름차순 정렬
## 방법2: 리스트이름.sort(reverse=True)  <- 내림차순 정렬
## 연습문제>> 유투버들을 오름차순과 내림차순으로 정렬한 결과를 각각 출력해보자
'''
print("-리스트 정렬하기")
youtuber.sort()
print(youtuber)
youtuber.sort(reverse=True)
print(youtuber)
'''

## 리스트 mission1
## :RGB 색상(red, green,blue)을 리스트에 저장하고
##  turtle 모듈을 활용하여 색상이 서로 다른 직선을 그려보자
##  (설정: 굵기(30), 선 길이(200))
'''
import turtle

color = ['red', 'green', 'blue']
win = turtle.Screen()
win.setup(600, 600)
t = turtle.Turtle('turtle')
t.pensize(30)

t.penup()
t.pencolor(color[0])
t.pendown()
t.fd(200)

t.penup()
t.setpos(0, 30)
t.pencolor(color[1])
t.pendown()
t.fd(200)

t.penup()
t.setpos(0, 60)
t.pencolor(color[2])
t.pendown()
t.fd(200)

win.mainloop()
'''

## 리스트 mission2
## 다음은 1번~5번 학생의 1분간 턱걸이 개수이다
'''
pull_up = [3, 16, 2, 5, 10, 7]
## 1번 문제: 7번째 학생의 턱걸이 개수가 9라고 할 때, 이를 리스트에 추가해보자
pull_up.append(9)
print(pull_up)
## 2번 문제: 2번 학생의 재측정 결과 20개의 턱걸이를 하였다. 리스트에 데이터를 수정해보자
pull_up[1] = 20
print(pull_up)
## 3번 문제: 3~7번까지의 학생의 턱걸이 갯수만을 뽑아 temp 변수에 저장하고 출력해보자
temp = pull_up[2:]
print(temp)
## 4번 문제: 학생들의 턱걸이 횟수 데이터를 오름차순으로 정렬
pull_up.sort()
print(pull_up)
'''

# [반복문]
## 반복문이란?: 반복적인 작업을 컴퓨터에 시키기 위한 명령.
## 종류: for문(횟수, 시퀀스 자료형), while문(조건)
## 시퀀스 자료형이란?: "순서"가 있는 자료형 (리스트, 문자열, range객체, 튜블, 딕셔너리)

## range() 함수 연습문제: range()를 활용하여
# 여러 활용 해보기 & list로 만들어 결과 확인하기
'''
print(range(10))
print(list(range(10)))
print(list(range(3,11)))
print(list(range(3,15,2)))
print(list(range(10, 1, -1)))
'''
## for 반복문
## : "횟수 or 시퀀스 자료"에 대한 반복문
## [문법] for 변수 in 시퀀스자료:
##           반복할 문장
## for문 연습문제1: range()를 활용한 "횟수" 반복. 원하는 문자열을 10번 반복해서 출력해보자.
'''
for i in range(10):
    print("퇴근하고 싶다!!!!!")
'''
## for문 연습문제2: list를 활용하여 for 반복문 실행시켜 보기
'''
youtubers = ['맛있는 녀석들', '장삐쭈', '와나나', '생활코딩', '옥냥이', '백종원']
for youtuber in youtubers:
    print(f"{youtuber} 채널 구독과 좋아요! 알람설정까지!")
'''
## for문 연습문제3: 문자열을 활용하여 for 반복문 실행시켜보기
'''
for char in "안녕하세요":
    print(char)
'''
## 이중 for문 연습문제: 이중 for문을 활용하여 높이5의 직각삼각형 만들기
'''
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print("")
'''
## while 반복문
## : "조건"에 대한 반복문
## [문법] while 조건:
##          반복할 문장
## while문 연습문제1: 기본적인 활용
'''
count = 0
while count<10:
    print("정신나갈꺼같아", end='')
    count += 1
'''
## while문 연습문제2: 무한루프와 break를 활용하여 게임 시작메뉴를 만들어보자
'''
while True:
    select = int(input("프로그램을 종료하려면 0을 입력하세요>>"))
    if select == 0:
        print("프로그램을 종료합니다.")
        break
'''
