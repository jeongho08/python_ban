# 10주차 정규수업(10:00~12:00) answer
'''
[10주차 주제]
1. class 선언 및 호출
2. 상속
3. 메서드 오버라이딩
4. 클래스 변수
'''

# [class]
## <class 생성 및 호출>
## <class 생성 문법>
## class 클래스 이름:
##     def 메서드 이름1(self, 입력변수1, 입력변수2, ...):
##         실행명령
##     def 메서드 이름2(self, 입력변수1, 입력변수2. ...):
##         실행명령

## <class 호출 문법>
## 클래스 선언하기: 인스턴스 = 클래스이름()
## 매서드 호출하기: 인스턴스.메서드()

## 연습문제2: 모든 자료형은 class이다.
## 정수형, 실수형, 문자열, 불린형 등의 다양한 자료형을 가진 변수를 선언 후
## type() 명령을 통해 자료형을 출력하여 보자(class 확인 할 것)
## + 추가적으로 .__dir__() 역시 출력해보자

a = 12
b = 0.125
c = '안녕하세요'
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(a.__dir__())
print(b.__dir__())
print(c.__dir__())
print(d.__dir__())


## class Mission1
## : Mission에 언급된 내용대로 Cat class를 만들어 보자
'''
class Cat():
    def cry(self):
        print("야옹!")
    def tail_wag(self):
        print("야옹! 야옹!!")
    def translate_cry(self):
        print("하찮은 닝겐! 나에게 밥을 대령해라!")
    def translate_tw(self):
        print("심심하다! 특별히 나와 놀게 해주겠다 닝겐!")

# 객체 생성 후 매서드 호출하기
siamese = Cat()

siamese.cry()
siamese.tail_wag()
siamese.translate_cry()
siamese.translate_tw()
'''

## <생성자>
## : 객체가 생성될 때 자동으로 호출되는 메서드.
## [문법] class 클래스이름:
##           def __init__(self, 입력변수들):
##               초기화 실행 문장

## 생성자 연습문제
## : Monster 클래스를 만들고 step에 따라 생성자와 메서드가 추가된 Monster 클래스를 만들어보자.
## step1) 가장 기본적인 Monster 클래스를 만들어 보자
##        : say 메서드만을 가지는 Monster 클래스
'''
class Monster:
    def say(self):
        print("나는 아주아주 무서운 몬스터다!!")

goblin = Monster()
goblin.say() 
'''
## step2) Monster 클래스에 속성(name, health, attack, speed)을 추가하여 초기화해보자.
##        또한, 인스턴스 생성 시에 say의 내용이 출력되도록 만들어보자.
'''
class Monster:
    def __init__(self, name, health, attack, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
        print(f"나는 아주아주 무서운 {self.name}다!!")

goblin = Monster('고블린', 200, 10, 5)
'''
## step3) Monster 클래스에 메서드(decrease_health, get_health, info)를 추가한 후,
##        각 메서드들을 호출해보자.
'''
class Monster:
    def __init__(self, name, health, attack, speed):
        self.name = name
        self.health = health
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

# 고블린 인스턴스 생성
goblin = Monster('고블린', 200, 20, 5)
goblin.decrease_health(50)
print(goblin.get_health())
goblin.info()

# 늑대 인스턴스 생성
wolf = Monster('늑대', 500, 80 ,15)
wolf.decrease_health(100)
print(wolf.get_health())
wolf.info()
'''

## <상속>
## : 부모 클래스의 속성과 메서드를 자식클래스가 물려받을 수 있도록 만든 기능
## 상속을 사용하는 이유: 클래스들에 중복된 코드를 제거하고 유지보수를 하기 위해 사용하기 위해서 사용.

## 메서드 오버라이딩(덮어쓰기)
## : 부모 클래스에 있는 메서드를 자식클래스에서 동일한 이름으로 다시 만드는 것

## 상속 연습문제
## :Monster 클래스를 만들고, 상속을 활용하여 Wolf, Shark, Dragon 클래스를 만들어,각각의 객체를 생성해보자.

## step1) 부모 클래스: Monster 클래스 정의하기
## - 속성: name, health, attack
## - 메서드: move("self.name 지상에서 이동하기"를 출력하는 메서드, 이후 해당 몬스터의 이동방법이 출력되도록 할 것임.)
'''
class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")
'''
## step2) 자식 클래스: Wolf, Shark, Dragon
## - Monster 클래스를 상속 받을 것.
## - 몬스터의 속성에 맞게 move를 메서드 오버라이딩할 것.
'''
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):     # 메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    def move(self):
        print(f"[{self.name}] 날기")

wolf = Wolf("울프", 1500, 200)
wolf.move()

shark = Shark("샤크", 3000, 400)
shark.move()

dragon = Dragon("드래곤", 8000, 800)
dragon.move()
'''

# [이번주 추가 문제: 한수]
## url: https://www.acmicpc.net/problem/1065
'''
import sys
import copy

def checkHanNumber(number):
    # number를 각 자리 정수로 나누기
    dummy = copy.copy(number)
    num_list=[]
    while dummy>=10:
        num_list.append(dummy%10)
        dummy //= 10
    num_list.append(dummy)
    # print(num_list)

    # 한수 검사
    ## 한 자리 수 일 때, 항이 1개 뿐이므로 등차수열이라고 할 수 있음.
    if len(num_list) == 1:
        return True
    ## 두 자리 수 일 때, 항이 2개 이므로 두 항의 차이를 가지는 등차수열이라고 할 수 있음.
    elif len(num_list) == 2:
        return True
    ## 세자리 이상 일 때, 각 항의 차이 "d"를 list로 저장하여. d.count(d[0])==len(d)인지 검사 
    else:
        d = []
        for i in range(len(num_list)-1):
           d.append(num_list[i+1]-num_list[i])
        if d.count(d[0]) == len(d):
            return True

N = int(sys.stdin.readline())

count = 0
for number in range(1, N+1):
    check_result = checkHanNumber(number)
    if check_result == True:
        count += 1
print(count)
'''

