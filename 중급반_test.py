# -*- coding: utf-8 -*-
# 중급반 test answer
# 최소 금요일 9시 전까지 선생님에게 전송할 것.

# 1번 문제
# 주제: 문자열 입출력 + 연산자

string = input("지금 하고 싶은 말을 입력해주세요>>")
n = int(input("몇 번?>>"))
print(string * n)

# 2번 문제
# 주제: 조건문

# 3번 문제
# 주제:리스트
'''
champion = ['티모', '아리', '리신', '람머스', '바드', '마스터 이']
print(champion)
print(type(champion))
'''
# 4번 문제
# 주제: for 반복문(2중 for문) - 어려움


# 5번 문제
# 주제: while 반복문


# 6번 문제
# 주제: 함수
'''
def product_3num(x, y, z):
    return x*y*z

x = int(input("첫번째 숫자를 입력하세요: "))
y = int(input("두번째 숫자를 입력하세요: "))
z = int(input("세번째 숫자를 입력하세요. "))
print(product_3num(x, y, z))
print(product_3num(2, 5, 7))
'''

# 7번 문제
# 주제: 클래스
'''
class Dog():
    def __init__(self, bark, attack,):
    def bark(self):
        print("멍멍")
    def attack(self):
        print("크르릉..컹컹!")
    def translate_bark(self):
        print("멍멍")
    def translate_attack(self):
        print("크르릉..컹컹")

class Dog:
    def __init__(self, bark, attack):
        self.bark = bark
        self. = health
        self.attack = attack
        self.speed = speed
        print(f"나는 아주아주 무서운 {self.name}다!!")
    def decrease_health(self, num):          # num만큼 체력을 감소시키는 메서드
        self.health -= num
    def get_health(self):                    # Monster의 체력을 반환해주는 메서드
        return self.health
    def info(self):                    # Monster의 현재 정보를 출력하는 메서드
        print(f'[{self.name} 스테이터스]')
        print(f'체력: {self.health}')
        print(f'공격력: {self.attack}')
        print(f'속도: {self.speed}')
   
'''
