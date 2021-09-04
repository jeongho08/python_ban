# 6주차 answer

# 5주차 잘못 업로드 되었던 주제: 논리연산자/ 멤버십 연산자
## 논리연산: and, or, not 연산, 결과는 True or False
## 논리연산 연습문제>>and, or, not 연산을 활용하여 결과를 예측(주석)하고 결과 학인하기
'''
print(4 <6 and 10 >= 10)        # True and True -> True
print("로아 썸머 이벤트 조아요" != "로아 썸머 이벤트 조아요" or "시공의 폭풍은 정말 최고야!" == "시공의 폭풍은 정말 최고야!")   # False or True
print(not 5==5)                 # not True -> False
'''

## 멤버십 연산: 포함관계를 나타내는 연산(in, not in), 결과는 True or False
## 멤버십연산 연습문제>> 멤버십 연산자를 활용하여 "abc" 문자열 안에 b와 d가 포함되어 있는지 확인하기
'''
print("a" in "apple")             # True
print("d" in "banana")             # False
print("L" not in "LOSTARK")     # False
'''

# if 조건문 Mission(5주차 이어서)
## mission3>> 국어, 영어, 수학 점수를 입력받고 합계와 평균를 출력한 뒤.
## - 평균이 60점이 넘을 경우: "보충 대상자가 아닙니다. 즐거운 방학보내세요"
## - 퍙균이 60점이 넘지 않을 경우: "보충 대상자입니다. 당신의 방학은 이제 제껍니다 ㅎㅎ"
## 를 출력하는 프로그램을 만들어 보자
'''
kor = int(input("국어>>> "))
math = int(input("수학>>> "))
eng = int(input("영어>>> "))

sum = kor + math + eng
avg = sum/3
print("합계: %4d, 평균: %4.2f" %(sum, avg))

if avg>=60:
    print("보충 대상자가 아닙니다. 즐거운 방학보내세요 :D")
else:
    print("보충 대상자입니다. 당신의 방학은 이제 제껍니다 ㅎㅎ")
'''

## mission4>> Up-down 게임 만들기
## random 함수를 활용하여 1~100까지의 숫자를 생성하고 up-down 게임 만들어보기
'''
import random

print("[Up-Down Game]")
random_num = random.randint(1, 100)
while True:
    your_num = int(input("숫자를 입력하세요>> "))
    if random_num == your_num:
        print("정답입니다~~!")
        break
    elif random_num < your_num:
        print("Down")
    else:
        print("Up")
'''

# [리스트 자료형]
## 리스트를 사용하는 이유?: 여러개의 데이터를 한 번에 저장하기 위해서
## 문법: 리스트이름 = [데이터, 데이터, ... ,데이터]
## 연습문제>> 내가 자주보는 유투버 이름 각자 1개씩 카톡방(혹은 채팅방)에 올리고
## 이 이름들을 list로 만들기
'''
youtuber = ['맛있는 녀석들', '장삐쭈', '와나나', '생활코딩', '옥냥이', '백종원']
print(youtuber)
print(type(youtuber))
'''

## 리스트 제어하기1: 데이터 추가
## 방법: 리스트이름.append('추가할문자열')
## 연습문제>> 문자열에 수진썜이 좋아하는 유튜버 "승우아빠"를 추가해보자.
'''
print("-데이터 추가하기")
youtuber.append('승우아빠')
print(youtuber)
'''

## 리스트 제어하기2: 인덱싱
## 방법: 리스트이름[인덱스 번호], 여기서 인덱스 번호는 0부터 시작에 주의!
## python의 순서를 가진 것들은 기본 0부터 시작!!
## 연습문제>> 만들어진 유투버 리스트에서 내가 가장 좋아하는 유튜버만 출력해보자
'''
print("-리스트 인덱싱")
print(youtuber[6])
'''

## 리스트 제어하기3: 데이터 수정하기
## 방법: 리스트이름[인덱스 번호] = '새로넣을 문자열'
## 연습문제>> 내가 가장 좋아하는 유투버의 이름을 2번째로 좋아하는 유튜버의 이름으로 바꿔보자
'''
print("-데이터 수정")
youtuber[6] = '녹두로'
print(youtuber)
'''

## 리스트 제어하기4: 데이터 삭제하기
## 방법: del 리스트이름[삭제할인덱스번호]
## 연습문제>> 아쉽지만(ㅎㅎ) 선생님이 추가한 유투버를 리스트에서 삭제해보자.
'''
print("-데이터 삭제")
del youtuber[6]
print(youtuber)
'''




