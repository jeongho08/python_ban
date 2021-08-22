# -*- coding: utf-8 -*-
# 4주차 mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!

[3주차 복습]
1. Github에 commit, push 하기
2. 주석 처리 하는 방법 2가지
3. 문자열 입출력 print(), input()
'''
'''
name = input("이름을 입력하세요>>>")
print("%s님 안녕하세요" %name)
print(f"{name}님 안녕하세요")
'''

# [자료형]
## 숫자형 1) 정수형(integer, int)
## : 소수점이 없는 숫자의 형태
## mission>> 정수형인 숫자를 출력하고 type() 함수를 활용하여 자료형을 주석으로 적기
'''
print()
print(type(289732873781781938739873219078039487128792348793034978)) #int
'''
## 숫자형 2) 실수형(float)
## : 소수점이 있는 숫자의 형태
## mission>> 실수형인 숫자를 출력하고 type() 함수를 활용하여 자료형을 주석으로 적기
'''
print()
print(type(8497230782934.78092314)) #float
'''
## 문자열
## : 문자를 나열한 형태의 자료형
## mission1>> ""와 ''를 활용하여 내가 지금 하고 싶은 말을 문자열로 출력하기
'''
print()
print(type("오늘 저녁은 헤로인이었다"))    #str
'''
## mission2>> 문자열로 인용구호('') 출력하기


## mission3>> sep과 end를 활용하여 print() 용법 익히기
## sep: ,로 출력이 구분된 문자열 사이 출력 설정 // end: print문의 끝났을 때의 문자열 출력 설정
'''
print('안녕', '나는', '대마야', sep="@_@")
print('안녕하세요', end='안녕하지못한데요')
print('코카인')
'''
## - 불린형(참/거짓)
## : 참(True)/거짓(False) 형태의 자료형
## mission>> 불린형의 True와 False를 출력하고 type() 함수를 활용하여 자료형을 주석으로 적기
'''
print(True)
print(False)
print(type(True))
'''
# [변수]
## 변수란?: 데이터를 저장할 공간. 할당연산자(=)를 활용.
## 특징: "언제든지 데이터를 변경"할 수 있다.
## 문법: 변수이름 = 데이터
## mission>> 라인하르트(or 내 게임 주 캐릭터)의 이름, 공격력, 공격속도, 최대거리(reach)를 변수로 저장하고 출력해보자.
## 라인하르트 정보: https://namu.wiki/w/%EB%9D%BC%EC%9D%B8%ED%95%98%EB%A5%B4%ED%8A%B8(%EC%98%A4%EB%B2%84%EC%9B%8C%EC%B9%98)#s-4.2
'''
name = '미스포츈'
attack = 52
speed = 325
print(f'{name}')
print(f'공격력{attack}')
print(f'공격속도{325}')

'''

# [연산]
## 연산이란?: 수나 식을 일정한 '규칙'에 따라 계산하는 것
## 대입연산: 할당연산자(=)를 활용하여 데이터를 변수에 대입하는 연산자
'''
a = 3412
'''
## 숫자산술연산: + - * / 와 같은 수의 계산에 대한 연산자
## mission>> 7과 3에 대해서 + - * / // % **의 결과를 출력하기
'''
print(3+6)      #9
print(6-3)      #3
print(3-6)      #-3
print(3*6)      #18
print(3/6)      #0.5
print(6/3)      #2
print(6%3)      #0
print (6**3)    #216
'''
## 문자열연산: + *
## mission1>> 해시태그1,2,3를 변수로 받고 +연산을 사용하여 이를 한 문장으로 만들어 출력해보자
'''
tag1 = "#오늘부터1일"
tag2 ="#내꺼하자"
print(tag1+tag2)        #오늘부터1일#내꺼하자
string = '나락'
print(string*30)        #나락 30번 반복
'''

## mission2>> *연산을 활용하여 같은 문장이 반복되는 문자열을 출력해보자


## 복합할당연산자: 연산계의 줄임말
## mission>> 복함할당연산자를 활용하여 위에서 언급한 내 주 캐릭터의 스펙을 바꿔보자!
a = 4

a += 5
print(a)

a-= 5
print(a)

a *= 5
print(a)

a //= 5
print(a)

a%= 5
print(a)

a**=5
print(a)



## 비교연산: 2개 이상의 수를 비교하는 연산, 결과는 True or False
## mission>> <, > <=, >=, ==, != 연산을 하고 그 결과 예측(주석)하고 결과 확인하기


## 논리연산: and, or, not 연산, 결과는 True or False
## mission>>and, or, not 연산을 활용하여 결과를 예측(주석)하고 결과 학인하기


## 멤버십 연산: 포함관계를 나타내는 연산(in, not in), 결과는 True or False
## mission>> 멤버십 연산자를 활용하여 "abc" 문자열 안에 b와 d가 포함되어 있는지 확인하기



# [입력과 자료형 변환]
## mission1>> input()함수 활용하여 변수 x,y에 숫자를 입려하고 이 숫자를 더하여 결과를 출력해보자


## mission2>> mission1에서 오류가 않도록 코드를 수정해보자.


## mission3>> 자신이 생후 몇 개월인지 계산해보자!
## 입력: 출생년도(year) & 탄생월(month)


# [조건문]
## 조건문이란?: 조건에 따라 명령이 달라지는 제어문,
## 제어문 및 함수의 주요 특징!: 제어문에 포함된 문장은 "띄어쓰기"로 구분한다.
## if문: 조건의 시작. if에 걸린 조건이 참일 경우, 포함된 문장들 실행
## else문: 조건이 거짓(False)인 경우, 포함된 문장을 실행
## elif문: if문의 조건이 거짓인 경우 중에서 elif문의 조건이 참일 때, 포함된 문장 실행
## mission1>> 구독자수를 입력받고 수익창출이 되는지 여부를 판단해보자


## mission2>> 현재 가진 금액을 통해 최대로 먹을 수 있는 음식을 출력하는 프로그램
## 20000원 이상: 오늘 저녁은 치킨이닭!
## 10000원 이상: 이제는 3000원가지고는 택도 없는 떡볶이 ㅎㅎ
## 2000원 이상: 그래도 굶지는 않는 편의점 삼각김밥!
## 2000원 미만: 없다고 못먹는건 아니다. 친구에게 "한입만!"을 외쳐보자


## mission3>> Up-down 게임 만들기
## random 함수를 활용하여 1~100까지의 숫자를 생성하고 up-down 게임 만들어보기
## hit!: chapter2의 if 조건문 mission2 참고하기



# [리스트 자료형]
## 리스트를 사용하는 이유?: 여러개의 데이터를 한 번에 저장하기 위해서
## 문법: 리스트이름 = [데이터, 데이터, ... ,데이터]
## mission>> 내가 자주보는 유투버 이름 각자 1개씩 카톡방에 올리고 이 이름들을 list로 만들기


## 리스트 제어하기1: 데이터 추가
## 방법: 리스트이름.append('추가할문자열')
## mission>> 문자열에 수진썜이 좋아하는 유튜버 "승우아빠"를 추가해보자.


## 리스트 제어하기2: 인덱싱
## 방법: 리스트이름[인덱스 번호], 여기서 인덱스 번호는 0부터 시작에 주의!
## python의 순서를 가진 것들은 기본 0부터 시작!!
## mission>> 만들어진 유투버 리스트에서 내가 가장 좋아하는 유튜버만 출력해보자


## 리스트 제어하기3: 데이터 수정하기
## 방법: 리스트이름[인덱스 번호] = '새로넣을 문자열'
## mission>> 내가 가장 좋아하는 유투버의 이름을 2번째로 좋아하는 유튜버의 이름으로 바꿔보자


## 리스트 제어하기4: 데이터 삭제하기
## 방법: del 리스트이름[삭제할인덱스번호]
## mission>> 아쉽지만(ㅎㅎ) 선생님이 추가한 유투버를 리스트에서 삭제해보자.


## 리스트 제어하기5: 리스트 슬라이싱\
## 방법: 리스트이름[처음:끝+1]
## mision>> 처음~3번쨰, 2번째~끝, 3번째~4번째에 위치한 유투버들만을 출력해보자
## +mission>> :를 활용하여 리스트 전체를 출력해보자


## 리스트 제어하기6: 리스트 길이 구하기
## 방법: len(리스트이름)
## mission>> 현재 리스트에 포함된 데이터의 개수를 구해보자


## 리스트 제어하기7: 리스트 정렬하기
## 방법1: 리스트이름.sort()  <- 오름차순 정렬
## 방법2: 리스트이름.sort(reverse=True)  <- 내림차순 정렬
## mission>> 유투버들을 오름차순과 내림차순으로 정렬한 결과를 각각 출력해보자





