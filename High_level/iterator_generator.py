# 반복 가능(iterable) 객체 : for문과 같은 반복 구문에 적용할 수 있는 리스트와 같은 객체
# 이터레이터(iterator) : 데이터를 하나씩 순서대로 꺼내올 수 있는 객체 

a = [1, 2, 3]
ia = iter(a)
for i in ia:
    print(i)    

for i in ia:
    print(i)    

# for문이나 next함수로 그 값을 한 번 읽으면 그 값을 다시는 읽을 수 없다는 특징이 있다.

# 이터레이터 만들기
# __init__메서드 : 이터레이터를 초기화한다
# __iter__메서드 : 이터레이터 객체 자신을 반환한다
# __next__메서드 : 다음 값을 반환하고, 더 이상 값이 없으면 StopIteration 예외를 발생시킨다


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    i = MyIterator([1,2,3])
    for item in i:
        print(item)



class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data) -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result

if __name__ == "__main__":
    i = ReverseIterator([1,2,3])
    for item in i:
        print(item)



# 제너레이터 : 간단하게 이터레이터를 만드는 특별한 함수
# 제너레이터를 사용하면 함수 하나만으로 간단하게 이터레이터를 만들 수 있다
# 제너레이터의 핵심 특징
# 1. 일반 함수와 비슷하지만 return 대신 yield 키워드를 사용한다.
# 2. yield를 만나면 값을 반환하고 함수 실행을 일시정지한다.
# 3. 다시 호출하면 일시정지했던 지점부터 계속 실행한다.
# 4. 마치 음악 플레이어의 재생/일시정지 기능처럼 동작한다.


def mygen():
    yield 'a'
    yield 'b'
    yield 'c'

g = mygen()
print(type(g))

print(next(g))
print(next(g))


# 제너레이터 표현식 

def mygen():
    for i in range(1, 1000):
        result = i*i
        yield result

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))

G = (i * i for i in range(1, 1000))
print(next(G))
print(next(G))

# 제너레이터와 이터레이터
'''
지금까지 살펴본 제너레이터는 이터레이터와 서로 상당히 비슷하다는 것을 알 수 있다. 
클래스를 이용해 이터레이터를 작성하면 좀 더 복잡한 행동을 구현할 수 있다. 
이와 달리 제너레이터를 이용하면 간단하게 이터레이터를 만들 수 있다. 
따라서 이터레이터의 성격에 따라 클래스로 만들 것인지, 제너레이터로 만들 것인지를 선택해야 한다.
'''


# 제너레이터 활용하기
import time

def longtime_job():
    print("job start")
    time.sleep(1)  # 1초 지연 - 실제로는 데이터베이스 조회, 파일 처리 등을 시뮬레이션
    return "done"

# 리스트 컴프리헨션: 5번의 작업을 모두 실행해서 리스트로 만든다
list_job = [longtime_job() for i in range(5)]
print(list_job[0])  # 첫 번째 결과만 필요한 상황


import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

# 제너레이터 표현식: 함수를 미리 실행하지 않고 필요할 때만 실행
list_job = (longtime_job() for i in range(5))
print(next(list_job))  # 첫 번째 값만 요청

'''
핵심 차이점:

[ ] (리스트 컴프리헨션) → ( ) (제너레이터 표현식)으로 변경
list_job[0] → next(list_job)으로 값을 가져오는 방식 변경
'''

'''
제너레이터에서는 필요한 첫 번째 함수만 실행했기 때문에 시간이 단축되었음,
이와 함께 메모리 사용량도 크게 절약되는데, 
리스트는 모든 결과를 메모리에 저장하지만 제너레이터는 필요할 때만 값을 생성하기 때문이다.
이런 방식을 '느긋한 계산법(lazy evaluation)'이라고 한다.
'''

'''
제너레이터는 다음과 같은 상황에서 매우 유용하다:

대용량 데이터 처리 시 메모리 절약
시간이 오래 걸리는 작업을 필요할 때만 실행
무한한 데이터 스트림 처리
'''

