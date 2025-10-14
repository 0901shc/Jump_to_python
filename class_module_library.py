#클래스
#클래스는 객체 지향 프로그래밍의 기본 개념
#객체를 생성하기 위한 설계도 역할
#클래스 정의: class 클래스이름:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self): 
        print("Woof!")
#객체 생성: 변수 = 클래스이름()
my_dog = Dog("Buddy", 3)
#속성 접근: 객체.속성
print(my_dog.name)
print(my_dog.age)
#메서드 호출: 객체.메서드()
my_dog.bark()


#__init__ 메서드
#객체가 생성될 때 자동으로 호출되는 메서드 -> 이 점이 setdata 메서드와의 차이점
#객체의 초기화 작업을 수행
#예: def __init__(self, 매개변수):
#        실행할 코드
#self 매개변수는 객체 자신을 가리킴

#setdata 메서드
#객체의 속성 값을 설정하는 메서드
#예: def setdata(self, 매개변수):
#        실행할 코드
#        self.속성 = 매개변수
#self 매개변수는 객체 자신을 가리킴

#매서드 매개변수, 객체변수 -> first와 second로 사용되는 변수들을 말함

#계산기 클래스 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        return self.first / self.second


#상속
#기존 클래스의 기능을 확장하여 새로운 클래스를 만들 때 사용
#예: class 자식클래스(부모클래스):
#        실행할 코드
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second
#MoreFourCal 클래스는 FourCal 클래스를 상속받아 pow 메서드를 추가로 정의
a = MoreFourCal()
a.setdata(2, 3)
print(a.add())  #출력: 5
print(a.pow())  #출력: 8
#메서드 오버라이딩
#부모 클래스의 메서드를 자식 클래스에서 재정의하여 사용하는 것
#예: class 자식클래스(부모클래스):
#        def 메서드이름(self):
#            실행할 코드
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
b = SafeFourCal()
b.setdata(4, 0)
print(b.div())  #출력: 0
b.setdata(4, 2)
print(b.div())  #출력: 2.0

#클래스변수
#클래스 변수는 모든 객체가 공유하는 변수
#예: class 클래스이름:  클래스변수 = 값
class Family:
    lastname = "김"
print(Family.lastname)  #출력: 김
a = Family()
b = Family()
print(a.lastname)  #출력: 김
print(b.lastname)  #출력: 김
Family.lastname = "박"
print(a.lastname)  #출력: 박
print(b.lastname)  #출력: 박
#클래스 변수는 객체 변수와 다르게 모든 객체가 동일한 값을 가짐
#객체 변수는 객체마다 다른 값을 가질 수 있음

#모듈
#모듈은 관련된 함수, 클래스, 변수 등을 하나의 파일에 모아 놓은 것
#모듈을 사용하면 코드의 재사용성과 유지보수성을 높일 수 있음
#모듈 만들기: 파일이름.py
#모듈 사용하기: import 파일이름
import mymod.mod1 as mod1
result = mod1.add(3, 5)
print(result)
#출력: 8
from mymod.mod1 import sub
result = sub(10, 4)
print(result)
#출력: 6
from mymod.mod1 import *
result = mul(2, 3)
print(result)
#출력: 6


#다른 디렉터리에 있는 모듈을 불러오는 방법
#sys.path.append("경로")
import sys
sys.path.append("/Users/chosunghoon/Desktop/Github_Repository/Jump_to_python/Jump_to_python/mymod")
import mymod.mod1 as mod1
result = mod1.div(8, 2)
print(result)
#출력: 4.01


#패키지
#패키지는 모듈을 모아 놓은 디렉터리
#패키지를 사용하면 모듈을 체계적으로 관리할 수 있음
#패키지 만들기: 디렉터리이름/__init__.py
#패키지 사용하기: import 디렉터리이름.모듈이름

#예: import 패키지이름.모듈이름
import game.sound.echo
game.sound.echo.echo_test()

#예: from 패키지이름 import 모듈이름
from game.sound import echo
echo.echo_test()

#예: from 패키지이름.모듈이름 import 함수이름
from game.sound.echo import echo_test
echo_test()

#__init__.py
#패키지 디렉터리에 반드시 포함되어야 하는 파일
#패키지 초기화 작업을 수행
#비어 있어도 무방

#패키지 변수 및 함수 정의 : 패키지 수준에서 함수를 정의 할 수 있음, __init__.py 파일에 작성
#예: __init__.py 파일에 VERSION 변수와 print_version_info 함수 정의
import game
print(game.VERSION)
game.print_version_info()
#출력: 3.5
#      This is game package version 3.5

#패키지 내 모듈을 미리 import 하기
#패키지 사용 시 자주 사용하는 모듈을 미리 import 하여 편리하게 사용할 수 있음
#예: __init__.py 파일에 from . import 모듈이름 작성

import game
game.render_test()
#출력: render

from game.sound import *
echo.echo_test()
#출력: echo 

#상대경로 패키지
#패키지 내에서 상대경로를 사용하여 모듈을 import 할 수 있음


#내장함수
#파이썬에서 기본적으로 제공하는 함수
#예: abs(), all(), any(), bin(), bool(), chr(), dir(), divmod(), enumerate(), eval(), filter(), float(), format(), hex(), id(), input(), int(), isinstance(), len(), list(), map(), max(), min(), oct(), ord(), pow(), print(), range(), round(), sorted(), str(), sum(), tuple(), type(), zip() 등
print(abs(-5))  #출력: 5
print(all([1, 2, 3]))  #출력: True
print(any([0, 1, 2]))  #출력: True
#bin
print(chr(65))  #출력: A
print(dir([1, 2, 3]))  #출력: ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(divmod(7, 3))  #출력: (2, 1)
print(enumerate(['A', 'B', 'C']))  #출력: <enumerate object at 0x...>
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
#출력: 0 A
#      1 B
#      2 C
print(eval('3 + 5'))  #출력: 8
print(filter(lambda x: x > 2, [1, 2, 3, 4, 5]))  #출력: <filter object at 0x...>
print(hex(255))  #출력: 0xff
print(id([1, 2, 3]))  #출력: 140123456789056
#input() 함수는 사용자 입력을 받는 함수로, 실행 시 입력 대기 상태가 됨
#print(int('10'))  #출력: 10)
print(isinstance(3, int))  #출력: True
print(len('Hello'))  #출력: 5
print(list((1, 2, 3)))  #출력: [1, 2, 3]
print(map(lambda x: x * 2, [1, 2, 3]))  #출력: <map object at 0x...>
print(list(map(lambda x: x * 2, [1, 2, 3])))  #출력: [2, 4, 6]
print(max([1, 2, 3]))  #출력: 3
print(max("apple"))  #출력: p
print(min([1, 2, 3]))  #출력: 1
print(min("apple"))  #출력: a
print(oct(8))  #출력: 0o10
print(ord('A'))  #출력: 65
print(pow(2, 3))  #출력: 8
print(range(5))  #출력: range(0, 5)
for i in range(5):
    print(i, end=' ')
#출력: 0 1 2 3 4
print(range(1, 10, 2))  #출력: range(1, 10, 2)  
for i in range(1, 10, 2):
    print(i, end=' ')
#출력: 1 3 5 7 9
print(round(3.14159, 2))  #출력: 3.14
print(sorted([3, 1, 2]))  #출력: [1, 2, 3]
print(str(123))  #출력: '123'
print(sum([1, 2, 3]))  #출력: 6
print(tuple([1, 2, 3]))  #출력: (1, 2, 3)
print(type(3))  #출력: <class 'int'>
print(zip([1, 2, 3], ['A', 'B', 'C']))  #출력: <zip object at 0x...>
print(list(zip([1, 2, 3], ['A', 'B', 'C'])))  #출력: [(1, 'A'), (2, 'B'), (3, 'C')
#help() 함수는 파이썬 내장 함수, 모듈, 클래스, 메서드 등에 대한 도움말을 제공

