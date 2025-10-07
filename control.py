#파이썬 기초 문법 정리
#변수, 자료형, 연산자, 조건문, 반복문, 함수, 클래스 등
#기본적인 문법과 사용법을 익히는 것이 중요

#if문
#조건에 따라 다른 코드를 실행할 때 사용
#예: if, elif, else

#if문 예시
a = 10
if a > 5:
    print("a는 5보다 크다")
elif a == 5:
    print("a는 5와 같다")
else:
    print("a는 5보다 작다") 
#출력: a는 5보다 크다   
#조건문에서 비교 연산자 사용
#>, <, >=, <=, ==, !=
#논리 연산자 사용
#and, or, not

#조건부 표현식
#한 줄로 if문 작성 가능
#예: 변수 = 값1 if 조건 else 값2
b = 10
result = "b는 5보다 크다" if b > 5 else "b는 5보다 작거나 같다"
print(result)
#출력: b는 5보다 크다   
#조건부 표현식은 간단한 조건문에 적합, 복잡한 조건문에는 if문 사용 권장

#while문
#조건이 참인 동안 반복 실행
#예: while 조건:
count = 0
while count < 5:
    print("count:", count)
    count += 1
#출력: count: 0
#      count: 1
#      count: 2
#      count: 3
#      count: 4
#무한 루프 주의
#break문으로 루프 종료 가능
#continue문으로 다음 반복으로 건너뛰기 가능


prompt = """1. Add
2. Delete
3. List
4. Quit
Enter number:"""
number = 0
while number != 4:
    print(prompt)
    number = int(input())
    if number == 1:
        print("Add")
    elif number == 2:
        print("Delete")
    elif number == 3:
        print("List")
    elif number == 4:
        print("Quit")
    else:
        print("Wrong number. Enter again.")
#출력: 1. Add
#      2. Delete
#      3. List
#      4. Quit
#      Enter number:
#사용자가 4를 입력할 때까지 반복 실행   

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
#출력: 돈을 넣어 주세요: 
#      커피를 줍니다.
#      남은 커피의 양은 9개 입니다.
#      돈을 넣어 주세요: 
#      거스름돈 100를 주고 커피를 줍니다.       
#      남은 커피의 양은 8개 입니다.
#      돈을 넣어 주세요: 
#      돈을 다시 돌려주고 커피를 주지 않습니다.
#      남은 커피의 양은 8개 입니다.
#      돈을 넣어 주세요: 
#      커피가 다 떨어졌습니다. 판매를 중지 합니다.
#커피가 다 떨어지면 판매 중지

#while-else문
#while문이 정상적으로 종료되었을 때 else문 실행
#예: while 조건:
#        실행할 코드
#     else:
#        실행할 코드
n = 5
while n > 0:
    print(n)
    n -= 1
else:
    print("끝!")
#출력: 5
#      4
#      3
#      2
#      1
#      끝!
#while문이 break문으로 종료되면 else문 실행 안됨



#for문
#반복 가능한 객체(리스트, 튜플, 문자열 등)의 각 요소에 대해 반복 실행
#예: for 변수 in 반복 가능한 객체:
#        실행할 코드
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#출력: apple
#      banana
#      cherry

#for-else문
#for문이 정상적으로 종료되었을 때 else문 실행
#예: for 변수 in 반복 가능한 객체:
#        실행할 코드
#     else:
#        실행할 코드
for fruit in fruits:
    print(fruit)
else:
    print("끝!")
#출력: apple
#      banana
#      cherry
#      끝!  

#range() 함수 사용 가능
for i in range(len(fruits)):
    print(fruits[i])        
#출력: apple
#      banana
#      cherry   

#enumerate() 함수 사용 가능
for index, fruit in enumerate(fruits):
    print(index, fruit)
    print(enumerate(fruits))
#출력: 0 apple
#      1 banana
#      2 cherry
#      <enumerate object at 0x...>
#enumerate 객체는 반복 가능한 객체의 인덱스와 값을 튜플 형태로 반환
#딕셔너리 반복 가능
person = {"name": "Alice", "age": 25, "city": "New York"}
for key in person:
    print(key, person[key])
#출력: name Alice
#      age 25
#      city New York
#딕셔너리의 키와 값을 동시에 얻으려면 items() 메서드 사용
for key, value in person.items():
    print(key, value)
#출력: name Alice
#      age 25
#      city New York        


