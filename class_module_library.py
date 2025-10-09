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
import mymod.mod1 as m


#다른 디렉터리에 있는 모듈을 불러오는 방법
#sys.path.append("경로")
import sys
sys.path.append("/Users/chosunghoon/Desktop/Github_Repository/Jump_to_python/Jump_to_python/mymod")
import mymod.mod1 as mod1
result = mod1.div(8, 2)
print(result)
#출력: 4.01
