#함수
#코드의 재사용성을 높이고, 가독성을 향상시키기 위해 사용
#함수 정의: def 함수이름(매개변수):
#    실행할 코드
#함수 호출: 함수이름(인수)

def add(a, b):
    return a + b

result = add(3, 5)
print(result)
#출력: 8

#기본 매개변수
def greet(name, message="안녕하세요"):
    print(name + ": " + message)

greet("Alice")
greet("Bob", "반갑습니다")
#출력: Alice: 안녕하세요
#      Bob: 반갑습니다

#가변 인자
def add_mul(choice, *args): 
    if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
        result = 0 
        for i in args: 
             result = result + i 
    elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
        result = 1 
        for i in args: 
           result = result * i 
    return result 

print(add_mul("add", 1, 2, 3, 4, 5))
#출력: 15
print(add_mul("mul", 1, 2, 3, 4, 5))
#출력: 120

#키워드 가변 매개변수
#매개변수 이름과 값의 쌍을 딕셔너리 형태으로 전달
#예: def 함수이름(**kwargs):
def creat_profile(name, age, **kwargs):
    print("name:", name)
    print("age:", age)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
creat_profile("Alice", 25, city="New York", job="Engineer")
#출력: name: Alice
#      age: 25
#      city: New York
#      job: Engineer    


#Return값
def add_and_mul(a, b):
    return a + b, a * b
result = add_and_mul(3, 5)
print(result)
#출력: (8, 15)
sum_result, mul_result = add_and_mul(3, 5)
print(sum_result)
print(mul_result)
#출력: 8
#      15
def add_and_mul(a,b): 
    return a+b 
    return a*b 
result = add_and_mul(3,5)
print(result)
#출력: 8
#첫 번째 return문에서 함수가 종료되어 두 번째 return문은 실행되지 않음



#람다 함수
#간단한 함수를 한 줄로 작성할 때 사용
add = lambda x, y: x + y
print(add(3, 5))
#출력: 8
#람다 함수는 이름이 없는 익명 함수로, 주로 일시적으로 사용되는 경우에 적합
#예: map(), filter(), sorted() 함수의 인수로 자주 사용됨
#예: map() 함수와 함께 사용
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
#출력: [1, 4, 9, 16, 25]
#예: filter() 함수와 함께 사용
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
#출력: [2, 4]
#예: sorted() 함수와 함께 사용
points = [(1, 2), (3, 1), (5, 4), (2, 3)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)
#출력: [(3, 1), (1, 2), (2, 3), (5, 4)]
#람다 함수는 단순한 연산에 적합하며, 복잡한 로직이 필요한 경우에는 일반 함수를 사용하는 것이 좋음
#람다 함수는 디버깅이 어려울 수 있으므로, 가독성을 위해 적절히 사용해야 함
#람다 함수는 여러 줄로 작성할 수 없으며, 단일 표현식만 포함할 수 있음

#함수의 독스트링
def add(a, b):
    """두 수의 합을 반환하는 함수"""
    return a + b    
print(add.__doc__)
#출력: 두 수의 합을 반환하는 함수
help(add)
#출력: Help on function add in module __main__:
#      add(a, b)
#          두 수의 합을 반환하는 함수
#독스트링은 함수의 목적, 매개변수, 반환값 등을 설명하는 데 사용
#독스트링은 함수 정의 바로 아래에 작성하며, 삼중 따옴표(""" """)로 감싸서 여러 줄로 작성 가능
#독스트링은 코드의 가독성을 높이고, 함수 사용법을 이해하는 데 도움을 줌
#독스트링은 함수의 __doc__ 속성으로 접근 가능하며, help() 함수를 통해 확인할 수 있음