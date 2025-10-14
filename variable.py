#숫자형
#정수형, 실수형, 8진수, 16진수
a = 123 #integer
b = -123
c = 3.14 #float
d = -3.14
e = 0.5e10 #0.5 * 10^10
f = 0.5e-10 #0.5 * 10^-10
g = 0o177 #8진수
h = 0x8ff #16진수
i = 0xABC #16진수
print(a,b,c,d,e,f,g,h,i)

#사칙연산
a = 3
b = 4
print(a+b) #7
print(a-b) #-1
print(a*b) #12
print(a/b) #0.75
print(a//b) #0 몫
print(a%b) #3 나머지
print(a**b) #81 3^4 = 3*3*3*3 = 81

#문자열
#작은따옴표, 큰따옴표, 삼중따옴표
a = 'Hello'
b = "Hello"
c = '''Hello'''
d = """Hello"""
print(a,b,c,d)  
#문자열에 큰따옴표 포함
e = 'He said, "Hello"'
f = "He said, \"Hello\""
g = '''He said, "Hello"'''
h = """He said, "Hello" """
print(e,f,g,h)

#이스케이프 문자
print('I\'m a student') #I'm a student
print("He said, \"Hello\"") #He said, "Hello"
print('''This is a long string that spans multiple lines.
It can contain "quotes" and 'apostrophes' without any issues.''')


print("Line1\nLine2\nLine3") #\n 줄바꿈
print("Column1\tColumn2\tColumn3") #\t 탭
print("This is a backslash: \\") #\\ 백슬래시
print("This is a single quote: \'") #\' 작은따옴표
print("This is a double quote: \"") #\" 큰따옴표
print("This is a carriage return:\rStart") #\r 캐리지 리턴
print("This is a backspace: ABC\bD") #\b 백스페이스
print("This is a form feed:\fNext") #\f 폼 피드
print("This is a vertical tab:\vNext") #\v 수직 탭
print("This is a unicode character: \u03A9") #\u 유니코드 문자
print("This is a raw string: r\"Hello\nWorld\"") #r raw 문자열
print(r"This is a raw string: Hello\nWorld") #r raw 문자열
#raw 문자열은 이스케이프 문자를 무시하고 그대로 출력
print("This is a byte string: b'Hello'") #b 바이트 문자열
print(b"This is a byte string: b'Hello'") #b 바이트 문자열  
#바이트 문자열은 바이트 단위로 데이터를 처리할 때 사용
print("This is a formatted string: f'{a} World'") #f 포맷 문자열
a = "Hello"
print(f"This is a formatted string: {a} World") #f 포맷 문자열
#포맷 문자열은 변수나 표현식을 문자열 안에 삽입할 때 사용


#문자열 연산
a = "Hello" 
b = "World" 
print(a + " " + b) #Hello World
print(a * 3) #HelloHelloHello
print(a[1]) #e 인덱스 1
print(a[1:4]) #ell 인덱스 1~3
print(len(a)) #5 길이
print(a.lower()) #hello 소문자
print(a.upper()) #HELLO 대문자
print(a.startswith("H")) #True 시작문자 확인
print(a.endswith("o")) #True 끝문자 확인
print(a.split("e")) #['H', 'llo'] e 기준으로 분리
print(a.replace("l", "p")) #Heppo l을 p로 변경
print(a.strip()) #Hello 양쪽 공백 제거
print(a.find("e")) #1 e의 인덱스 반환
print(a.index("e")) #1 e의 인덱스 반환
print(a.count("l")) #2 l의 개수 반환
print(a.isalpha()) #True 알파벳인지 확인
print(a.isdigit()) #False 숫자인지 확인
print("I am {} years old".format(20)) #I am 20 years old
print("I am {age} years old".format(age=20)) #I am 20 years old
age = 20
print(f"I am {age} years old") #I am 20 years old           
print("I am %d years old" % age) #I am 20 years old
print("I eat %s apples." % "five") #I eat five apples.
print("PI is %.2f" % 3.14159) #PI is 3.14
print("Hex: %x" % 255) #Hex: ff
print("Oct: %o" % 255) #Oct: 377

#문자열 슬라이싱
a = "Hello, World!"
print(a[0]) #H 인덱스 0
print(a[7]) #W 인덱스 7
print(a[-1]) #! 인덱스 -1
print(a[-7]) #W 인덱스 -7
print(a[0:5]) #Hello 인덱스 0~4
print(a[7:12]) #World 인덱스 7~11
print(a[:5]) #Hello 인덱스 0~4
print(a[7:]) #World! 인덱스 7~끝
print(a[:]) #Hello, World! 인덱스 처음~끝
print(a[::2]) #Hlo ol! 인덱스 0~끝 2칸씩
print(a[1::2]) #el,Wrd 인덱스 1~끝 2칸씩
print(a[::-1]) #!dlroW ,olleH 인덱스 끝~처음 역순
print(a[-1:-6:-1]) #!dlroW 인덱스 -1~-6 역순                    
print(a[-6:-1]) #World 인덱스 -6~-2
print(a[3:8]) #lo, W 인덱스 3~7
print(a[3:-3]) #lo, Wo 인덱스 3~-4

str("Hello") #문자열로 변환
int("123") #정수로 변환
float("3.14") #실수로 변환
list("Hello") #문자열을 리스트로 변환 ['H', 'e', 'l', 'l', 'o']
tuple("Hello") #문자열을 튜플로 변환 ('H', 'e', 'l', 'l', 'o')
set("Hello") #문자열을 집합으로 변환 {'H', 'e', 'l', 'o'}
#집합은 중복된 값이 없고 순서가 없음
dict([('a', 1), ('b', 2)]) #리스트를 딕셔너리로 변환 {'a': 1, 'b': 2}               
#딕셔너리는 키와 값의 쌍으로 이루어진 자료형   
#딕셔너리는 문자열을 직접 변환할 수 없음
#딕셔너리는 리스트나 튜플을 이용해 변환해야 함
#예: dict([('key1', 'value1'), ('key2', 'value2')])
bool(1) #True 불리언으로 변환
bool(0) #False 불리언으로 변환
bool("Hello") #True 불리언으로 변환
bool("") #False 불리언으로 변환
#빈 문자열은 False, 나머지는 True
#파이썬 기초 문법 정리
#변수, 자료형, 연산자, 조건문, 반복문, 함수, 클래스 등
#기본적인 문법과 사용법을 익히는 것이 중요
#파이썬 공식 문서와 다양한 온라인 자료를 참고하여 학습 가능
#꾸준한 연습과 프로젝트를 통해 실력을 향상시킬 수 있음

del a #변수 삭제
#print(a) #Error a가 삭제되어 참조 불가
#변수 a가 삭제되어 참조할 수 없음
a = 10 #변수 재선언
print(a) #10    

'''
remove() #리스트에서 특정 값 제거
pop() #리스트에서 특정 인덱스의 값 제거 및 반환
clear() #리스트의 모든 값 제거
append() #리스트에 값 추가
insert() #리스트의 특정 인덱스에 값 추가
extend() #리스트에 다른 리스트의 값 추가
sort() #리스트의 값을 오름차순 정렬
reverse() #리스트의 값을 역순으로 정렬
count() #리스트에서 특정 값의 개수 반환
index() #리스트에서 특정 값의 인덱스 반환
extend() #리스트에 다른 리스트의 값을 추가
'''

#튜플
#리스트와 거의 동일한 메서드를 가짐
#단, 값 추가, 삭제, 변경 불가
#튜플은 불변(immutable) 자료형
#튜플은 소괄호()로 생성
#튜플은 리스트보다 메모리 사용량이 적고 속도가 빠름
#튜플은 해시 가능(hashable) 자료형
#튜플은 딕셔너리의 키로 사용 가능
#튜플은 함수의 반환값으로 자주 사용
#튜플은 언패킹(unpacking) 기능을 지원
#튜플은 여러 개의 값을 하나로 묶을 때 유용
#튜플은 리스트보다 안전한 자료형

#튜플기능
a = (1, 2, 3)
print(a[0]) #1 인덱스 0
print(a[1:3]) #(2, 3) 인덱스 1~2
print(len(a)) #3 길이
print(a + (4, 5)) #(1, 2, 3, 4, 5) 튜플 합치기
print(a * 2) #(1, 2, 3, 1, 2, 3) 튜플 반복
print(a.index(2)) #1 값 2의 인덱스 반환
print(a.count(2)) #1 값 2의 개수 반환

#딕셔너리 
#키와 값의 쌍으로 이루어진 자료형 
#중괄호{}로 생성 
#키는 중복될 수 없고, 값은 중복될 수 있음
#키는 문자열, 숫자, 튜플 등 해시 가능한 자료형만 가능
#값은 모든 자료형 가능

#딕셔너리 기능
a = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(a['name']) #Alice 키로 값 접근
print(a.get('age')) #25 키로 값 접근
print(a.keys()) #dict_keys(['name', 'age', 'city']) 키 목록 반환
print(a.values()) #dict_values(['Alice', 25, 'New York']) 값 목록
print(a.items()) #dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')]) 키-값 쌍 목록 반환
a['age'] = 26 #키로 값 변경
a['country'] = 'USA' #새로운 키-값 추가
print(a) #{'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}
del a['city'] #키-값 삭제
print(a) #{'name': 'Alice', 'age': 26, 'country': 'USA'}
print(len(a)) #3 길이
a.clear() #모든 키-값 삭제
print(a) #{} 빈 딕셔너리    
a = {'name': 'Alice', 'age': 25}
b = {'city': 'New York', 'country': 'USA'}
a.update(b) #딕셔너리 병합
print(a) #{'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}
print('name' in a) #True 키 존재 여부 확인
print('gender' in a) #False 키 존재 여부 확인
for key in a: #딕셔너리 순회
    print(key, a[key])
#name Alice
#age 25
#city New York
#country USA      
for key, value in a.items(): #키-값 쌍 순회
    print(key, value)
#name Alice
#age 25
#city New York
#country USA
a.get('name')
a.get('age')
a.get('city')
a.get('country')
a.get('gender') #None 존재하지 않는 키 접근시 None 반환 


#집합
#중복된 값이 없고 순서가 없음
#중괄호{} 또는 set() 함수로 생성
#집합은 수학의 집합 개념과 유사
#집합은 교집합, 합집합, 차집합 등의 연산 지원
#집합은 중복된 값을 자동으로 제거
#집합은 리스트나 튜플보다 메모리 사용량이 적고 속도가 빠름
#집합은 집합 연산에 유용
#집합은 해시 가능(hashable) 자료형만 원소로 가질 수 있음
#집합은 딕셔너리의 키로 사용 가능
#집합은 순서가 없기 때문에 인덱스로 접근할 수 없음
#집합은 변경 가능한(mutable) 자료형
#집합은 add(), remove(), discard(), pop(), clear() 등의 메서드 제공
#집합은 frozenset() 함수를 이용해 변경 불가능한(immutable) 집합 생성 가능
#frozenset은 집합과 동일한 기능을 제공하지만, 원소를 추가하거나 제거할 수 없음
#frozenset은 해시 가능(hashable) 자료형이므로, 딕셔너리의 키로 사용 가능
#frozenset은 집합 연산에 유용
#frozenset은 set보다 메모리 사용량이 적고 속도가 빠름
#frozenset은 집합과 달리 변경할 수 없기 때문에 안전한 자료형
#frozenset은 집합과 동일한 메서드를 제공하지만, 원소를 추가하거나 제거하는 메서드는 없음

#집합 기능
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b) #{1, 2, 3, 4, 5} 합집합
print(a & b) #{3} 교집합
print(a - b) #{1, 2} 차집합
print(a ^ b) #{1, 2, 4, 5} 대칭차집합
a.add(4) #값 추가
print(a) #{1, 2, 3, 4}
a.remove(2) #값 제거
print(a) #{1, 3, 4}
a.discard(5) #값 제거(존재하지 않아도 에러 없음)
print(a) #{1, 3, 4}
a.pop() #임의의 값 제거 및 반환
print(a) #{3, 4} (1이 제거됨)
print(len(a)) #2 길이
a.clear() #모든 값 제거
print(a) #set() 빈 집합
a.update(b) #집합 병합
print(a) #{3, 4, 5}
a = {1, 2, 3}
b = {3, 4, 5}
print(a.issubset(b)) #False a가 b의 부분집합인지 확인
print(a.issuperset(b)) #False a가 b의 상위집합인지 확인
print(a.isdisjoint(b)) #False a와 b가 공통 원소가 없는지 확인
print(frozenset(a)) #frozenset({1, 2, 3}) 변경 불가능한 집합 생성
print(frozenset(b)) #frozenset({3, 4, 5}) 변경 불가능한 집합 생성  

#불리언
#참(True) 또는 거짓(False)을 나타내는 자료형
#불리언은 조건문과 반복문에서 주로 사용
#불리언은 비교 연산자와 논리 연산자의 결과로 생성
#불리언은 bool() 함수를 이용해 다른 자료형을 불리언으로 변환 가능
#불리언은 1(True)과 0(False)으로도 표현 가능
#불리언은 파이썬에서 중요한 자료형 중 하나
#불리언은 조건문과 반복문에서 주로 사용
#불리언은 비교 연산자와 논리 연산자의 결과로 생성
#불리언은 bool() 함수를 이용해 다른 자료형을 불리언으로 변환 가능
#불리언은 1(True)과 0(False)으로도 표현 가능

#불리언 기능
a = True
b = False
print(a and b) #False 논리곱
print(a or b) #True 논리합
print(not a) #False 부정
print(not b) #True 부정
print(a == b) #False 같음
print(a != b) #True 다름
print(a > b) #True a가 b보다 큼
print(a < b) #False a가 b보다 작음
print(a >= b) #True a가 b보다 크거나 같음
print(a <= b) #False a가 b보다 작거나 같음
print(bool(1)) #True 1은 True로 변환
print(bool(0)) #False 0은 False로 변환
print(bool("Hello")) #True 빈 문자열이 아니면 True
print(bool("")) #False 빈 문자열은 False
print(bool([])) #False 빈 리스트는 False
print(bool([1, 2, 3])) #True 빈 리스트가 아니면 True
print(bool(())) #False 빈 튜플은 False
print(bool((1, 2, 3))) #True 빈 튜플이 아니면 True
print(bool({})) #False 빈 딕셔너리는 False
print(bool({'a': 1})) #True 빈 딕셔너리가 아니면 True
print(bool(set())) #False 빈 집합은 False
print(bool({1, 2, 3})) #True 빈 집합이 아니면 True
print(int(True)) #1 True는 1로 변환
print(int(False)) #0 False는 0으로 변환
print(float(True)) #1.0 True는 1.0으로 변환


#변수명
#변수명은 문자, 숫자, 밑줄(_)로 구성
#변수명은 숫자로 시작할 수 없음
#변수명은 대소문자를 구분
#변수명은 파이썬의 예약어를 사용할 수 없음
#예약어: if, else, elif, for, while, def, return, class, import, from, as, with, try, except, finally, raise, in, is, and, or, not, lambda, pass, break, continue, global, nonlocal, assert, yield, del
#변수명은 의미 있는 이름으로 작성하는 것이 좋음
#예: age, name, total_price, is_valid 등
#변수명은 밑줄(_)로 단어를 구분하는 스네이크_케이스(snake_case) 방식 권장
#예: total_price, is_valid 등
#변수명은 너무 길거나 짧지 않게 작성하는 것이 좋음
#예: a, b, c 등 너무 짧은 변수명은 피하는 것이 좋음
#변수명은 숫자나 특수문자를 포함하지 않는 것이 좋음
#예: price1, total$ 등 특수문자가 포함된 변수명은 피하는 것이 좋음
#변수명은 변수의 용도나 의미를 잘 나타내는 것이 좋음
#예: count, index, result 등 변수의 역할을 잘 나타내는 이름이 좋음
#변수명은 일관성 있게 작성하는 것이 좋음
#예: total_price, totalPrice 등 같은 의미의 변수명은 일관성 있게 작성하는 것이 좋음
#변수명은 가독성을 높이기 위해 적절한 길이로 작성하는 것이 좋음
#예: total_price, is_valid 등 너무 길거나 짧지 않게 작성하는 것이 좋음


#변수를 만드는 여러 가지 방법
a, b =('python', 'life') #튜플 언패킹
print(a) #python
print(b) #life
(a, b) = 'python', 'life' #튜플 언패킹
print(a) #python
print(b) #life
[a, b] = ['python', 'life'] #리스트 언패킹
print(a) #python
print(b) #life
a = b = 'python' #여러 변수에 같은 값 대입
print(a) #python
print(b) #python
a = 3 #정수형 변수
b = 3.9 #실수형 변수
c = "Hello" #문자열 변수
d = [1, 2, 3] #리스트 변수
e = (1, 2, 3) #튜플 변수
f = {'name': 'Alice', 'age': 25} #딕셔너리 변수
g = {1, 2, 3} #집합 변수
h = True #불리언 변수
print(a, b, c, d, e, f, g, h) #3 3.9 Hello [1, 2, 3] (1, 2, 3) {'name': 'Alice', 'age': 25} {1, 2, 3} True

