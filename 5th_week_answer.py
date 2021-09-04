# 5주차 mission 답안

## 비교연산: 2개 이상의 수를 비교하는 연산, 결과는 True or False
## mission>> <, > <=, >=, ==, != 연산을 하고 그 결과 예측(주석)하고 결과 확인하기
'''
print(5>8)      # False
print(3<8)      # True
print(10>=7)    # True
print(200>=751)  # False
print(5==11)    # False
print(5!=5)     # False
print("포항항항하항항" == "포항항항하항항")
print("illililillllllilil" != "illililillllllilil")
'''

## 논리연산: and, or, not 연산, 결과는 True or False
## mission>>and, or, not 연산을 활용하여 결과를 예측(주석)하고 결과 학인하기
'''
print(4 <6 and 10 >= 10)        # True and True -> True
print("로아 썸머 이벤트 조아요" != "로아 썸머 이벤트 조아요" or "시공의 폭풍은 정말 최고야!" == "시공의 폭풍은 정말 최고야!")   # False or True
print(not 5==5)     # not True -> False
'''

## 멤버십 연산: 포함관계를 나타내는 연산(in, not in), 결과는 True or False
## mission>> 멤버십 연산자를 활용하여 "abc" 문자열 안에 b와 d가 포함되어 있는지 확인하기
'''
print("a" in "abc")
print("d" in "abc")
print("L" not in "LOSTARK")
'''

# [입력과 자료형 변환]
## mission1>> input()함수 활용하여 변수 x,y에 숫자를 입력하고
## 이 숫자를 더하여 정수들의 합에 대한 결과를 출력해보자
'''
x = input("x를 입력하세요 >>")
y = input("y를 입력하세요 >>")
result = x+y
print(result)
'''

## mission2>> mission1에서 제대로 된 값이 나오도록 코드를 수정해보자.
'''
x = int(input("x를 입력하세요 >>"))
y = int(input("y를 입력하세요 >>"))
result = x+y
print(result)
'''

## mission3>> 출생년도를 입력하고 나이를 출력해보자.
'''
year = int(input('출생년도를 입력하세요 >> '))
age = 2021-year+1

print(f"당신의 나이는 {age}입니다.")
'''

# [조건문]
## 조건문이란?: 조건에 따라 명령이 달라지는 제어문,
## 제어문 및 함수의 주요 특징!: 제어문에 포함된 문장은 "띄어쓰기"로 구분한다.
## if문: 조건의 시작. if에 걸린 조건이 참일 경우, 포함된 문장들 실행
## else문: 조건이 거짓(False)인 경우, 포함된 문장을 실행
## elif문: if문의 조건이 거짓인 경우 중에서 elif문의 조건이 참일 때, 포함된 문장 실행
## mission1>> 구독자수를 입력받고 수익창출이 되는지 여부를 판단해보자
'''
subscriber = int(input("구독자 수를 입력하세요 >> "))
if subscriber>=1000:
    print("수익창출을 할 수 있는 계정입니다.")
else:
    print("수익창출을 할 수 없습니다.")
'''

## mission2>> 현재 가진 금액을 통해 최대로 먹을 수 있는 음식을 출력하는 프로그램
## 20000원 이상: 오늘 저녁은 치킨이닭!
## 10000원 이상: 이제는 고오급 음식인 떡볶이 ㅎㅎ
## 2000원 이상: 그래도 굶지는 않는 편의점 삼각김밥!
## 2000원 미만: 없다고 못먹는건 아니다. 친구에게 "한입만!"을 외쳐보자
'''
money = int(input("현재 가진 금액을 입력하세요 >> "))
if money >= 20000:
    print("오늘 저녁은 치킨이닭!!")
elif money >= 10000:
    print("이제는 고오급 음식인 떡볶이를 먹으러 가자!")
elif money >= 2000:
    print("그래도 굶지는 않는 편의점 삼각김밥!")
else:
    print('돈이 없다고 굶어야 하는 것은 아니다... 친구에게 "한입만!"을 외쳐보자')
'''

