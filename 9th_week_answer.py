# 9주차 정규수업(10:00~12:00) answer
'''
[9주차 주제]
1. 튜플
2. 딕셔너리
3. class - 1
'''

# [튜플과 딕셔너리]
## [튜플]
## : 간단하게 말해 "수정, 추가, 삭제가 불가능한 리스트" 라고 간주할 수 있다.
## 연습문제1: 튜플 만들기
## 2가지 방법으로 튜플을 선언해보고, 두 변수의 값고 자료형을 출력해보자.
'''
numbers1 = (4, 5, 6, 7)
numbers2 = 1, 2, 3, 4
print(numbers1, type(numbers1))
print(numbers2, type(numbers2))
'''
## 연습문제2: 원소가 하나인 튜플 만들기
## 선언시 ,(쉽표)를 넣지 않은 경우와 쉼표를 넣어 변수를 만들고, 변수들의 값과 자료형을 비교해보자.
'''
num1 = (77)
num2 = (77,)
num3 = 77
num4 = 77,
print("num1: ", num1, type(num1))
print("num2: ", num2, type(num2))
print("num3: ", num3, type(num3))
print("num4: ", num4, type(num4))
'''
## 연습문제3: 튜플 ↔ 리스트로 변환
## : tuple을 만들고 이를 list로 변환 후 값과 자료형을 출력한 후, 이를 다시 튜플로 바꾸어 같은 과정을 반복해보자.
'''
numbers = (100, 110, 10)
numbers = list(numbers)
print(numbers, type(numbers))
numbers = tuple(numbers)
print(numbers, type(numbers))
'''
## 연습문제4: 패킹과 언패킹 그리고 a, b 값 바꾸기
## 4-1) 패킹과 언패킹을 하여 자료형을 출력해보자.
## 4-2) 패킹 언패킹 개념을 활용하여 a, b의 값 바꾸어보자
'''
a = 7
b = 8
numbers = a, b
print("numbers:", numbers, type(numbers))
c, d = numbers
print("c: ", c, type(c))
print("d: ", d, type(d), end='\n\n')

print("a: ", a)
print("b: ", b)
a, b = b, a         
print("a: ", a)
print("b: ", b)
'''

## 연습문제5: 튜플과 관련된 함수
'''
numbers = 100, 546, 896, 10, 777
print(max(numbers))         # max(): 튜플에서 최댓값을 반환하는 함수
print(min(numbers))         # min(): 튜플에서 최솟값을 반환하는 함수
print(sum(numbers))         # sum(): 튜플에 포함된 원소들의 함을 반환하는 함수
print(numbers.count(777))   # .count(): 입력한 숫자가 튜플에 몇 개 있는지 세어주는 함수(메서드)
print(numbers.index(246))   # .index(): 입력한 숫자의 인덱스를 반환해주는 함수(메서드)
'''

## [딕셔너리]
## : 키(key)와 데이터(value)를 가지고 있는 "사전과 같은 자료형"
## key값을 통해 value값을 불러올 수 있다.

## 연습문제1: 딕셔너리 만들기
## : 자신이 좋아하는 youtuber 3~5명의 채널이름(key)과 구독자 수(value)로 dictionary 자료형을 만들어보자
'''
youtuber = {
    "승우아빠" : 1460000,
    "백종원의 요리비책" : 5110000,
    "잇섭" : 1830000,
    "옥냥이" : 460000,
    "오킹TV" : 1110000
}
'''
## 연습문제2: 딕셔너리 제어1-값에 접근하기
## : 자신이 가장 좋아하는 youtuber의 구독자 수를 출력해보자
'''
print(youtuber["승우아빠"])
'''
## 연습문제3: 딕셔너리 제어2-값 할당(or 수정)하기
## : 자신이 가장 좋아하는 유투버의 구독자 수에 1000이 더 큰 숫자를 넣고 이를 출력해보자
'''
youtuber["승우아빠"] = 1461000
print(youtuber["승우아빠"])
'''
## 연습문제3: 딕셔너리 제어3-삭제하기
## : 자신이 두번째로 좋아하는 youtuber를 딕셔너리에서 삭제해보자
'''
del youtuber["백종원의 요리비책"]
print(youtuber)
'''
## 연습문제4: 딕셔너리 관련 함수
## .items(), .keys(), .values()의 결과와 데이터 타입을 출력해보자
'''
print(youtuber.items())
print(youtuber.keys())
print(youtuber.values())
'''


# [클래스(class)]
## 클래스와 객체
## 클래스: 객체를 만들기 위한 "설계도"
## 객체: 설계도로부터 만들어낸 "제품"

## 클래스를 사용하는 이유
## LOL 인벤 챔피언들 정보: https://lol.inven.co.kr/dataninfo/champion/compare.php
## LOL 혹은 자신이 좋아하는 게임의 캐릭터 3가지를 선택하여 해당 캐릭터의 정보(채력, 공격력, 이동속도)를 입력하고,
## "게임 시작 인사, 캐릭터 능력을 각각 출력(함수)"등을 수행하는 프로그램을 만들어 보자

## case1: class를 활용하지 않은 경우
'''
character1_name = "레넥톤"
character1_health = 575
character1_attack = 69
character1_speed = 345

print(f"{character1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

character2_name = "리신"
character2_health = 575
character2_attack = 70
character2_speed = 345

print(f"{character2_name}님 소환사의 협곡에 오신 것을 환영합니다.")

## 여기에서 캐릭터를 하나 더 추가해보자.
character3_name = "오른"
character3_health = 590
character3_attack = 69
character3_speed = 335

print(f"{character3_name}님 소환사의 협곡에 오신 것을 환영합니다.")

## 캐릭터의 이름과 기본 공격력(attack)을 출력하는 함수를 정의하여 세 캐릭터의 공격력을 출력해보자
def basic_info(name, attack, health, speed):
    print(f"[{name}]")
    print(f"기본공격력: {attack}")
    print(f"기본체력: {health}")
    print(f"기본속도: {speed}")

basic_info(character1_name, character1_attack, character1_health, character1_speed)
basic_info(character2_name, character2_attack, character2_health, character2_speed)
basic_info(character3_name, character3_attack, character3_health, character3_speed)

print("=========클래스를 사용한 경우==========")
'''


## case2: 클래스를 사용한 경우
'''
class Character:
    def __init__(self, name, attack, health, speed):
        self.name = name
        self.attack = attack
        self.health = health
        self.speed = speed
        print(f"{self.name}님 소환사의 협곡에 오신 것을 환영합니다.")
    def basic_info(self):
        print(f'[{self.name}]')
        print(f'기본공격력: {self.attack}')
        print(f'기본체력: {self.health}')
        print(f'기본속도: {self.speed}')
        
renekton = Character("레넥톤", 69, 575, 345)
leesin = Character("리신", 70, 575, 345)
ornn = Character("오른", 69, 590, 335)        ## 역시 하나의 챔피언 추가

# 챔피언 정보 출력하기
renekton.basic_info()
leesin.basic_info()
ornn.basic_info()
'''

# [이번주 추가 문제: 덩치]
## url: https://www.acmicpc.net/problem/7568
# - 백준 7568번 덩치 문제
'''
import sys

# import time

# 입력 가져오기 
N = int(input(""))
people = []
for i in range(N):
    height, weight = (sys.stdin.readline().split())
    height = int(height)
    weight = int(weight)
    temp = [height, weight, 1]
    people.append(temp)

# 순위 판단
# start = time.time()
for i in range(len(people)):
    for j in range(len(people)):
        if i == j:
            continue
        else:
            if (people[i][0] < people[j][0]) and (people[i][1] < people[j][1]):
                people[i][2] += 1

# 등수 출력
for i in range(len(people)):
    print(f"{people[i][2]}", end=" ")
'''