#input함수
#사용자 입력을 받을 때 사용
#예: input("Enter something: ")
name = input("Enter your name: ")
print("Hello, " + name + "!")
#출력: Enter your name: Alice
#      Hello, Alice!
#input함수는 항상 문자열을 반환
#숫자 입력을 받을 때는 int()나 float()로 변환 필요
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")
#출력: Enter your age: 25
#      You are 25 years old.    


#출력함수
#화면에 출력할 때 사용
#예: print(출력할 내용)
print("Hello, World!")
#출력: Hello, World!
#여러 값을 출력할 때는 쉼표(,)로 구분
print("Name:", name, "Age:", age)
#출력: Name: Alice Age: 25
#문자열 포맷팅
#f-string (Python 3.6 이상)
print(f"Name: {name}, Age: {age}")
#출력: Name: Alice, Age: 25
#format() 메서드
print("Name: {}, Age: {}".format(name, age))
#출력: Name: Alice, Age: 25
#% 연산자
print("Name: %s, Age: %d" % (name, age))
#출력: Name: Alice, Age: 25         

#sep와 end 매개변수
print("Hello", "World", sep=", ", end="!\n")
#출력: Hello, World!
for i in range(3):
    print(i, end="!")
#출력: 0!1!2!
print("점프", "투", "파이썬", sep=" to ")
#출력: 점프 to 투 to 파이썬




#파일 입출력
#파일 열기: open("파일이름", "모드")
#모드: "r" (읽기), "w" (쓰기), "a" (추가), "b" (바이너리)
file = open("example.txt", "w")
file.write("Hello, File!\n")
file.write("This is a test file.\n")
file.close() 

#파일 읽기
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
#출력: Hello, File!
#      This is a test file.

#readline() 메서드: 한 줄씩 읽기
file = open("example.txt", "r")
line = file.readline()
print(line, end="")  # 줄바꿈 문자 제거 위해 end="" 사용
line = file.readline()
print(line, end="")
file.close()
#출력: Hello, File! 

#readlines() 메서드: 모든 줄을 리스트로 읽기
file = open("example.txt", "r")
lines = file.readlines()
for line in lines:
    print(line, end="")
file.close()
#출력: Hello, File!

#줄바꿈(\n) 문자 제거하기
#strip() 메서드 사용
file = open("example.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()
#출력: Hello, File! 

#read() 메서드 : 파일 내용 전체를 문자열로 반환
file = open("example.txt", "r")
content = file.read(5)  # 처음 5글자 읽기
print(content)
content = file.read(5)  # 다음 5글자 읽기
print(content)
file.close()
#출력: Hello

#with문을 사용한 파일 입출력 : 파일을 열고 닫는 것을 자동으로 처리
with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
#출력: Hello, File!
#      This is a test file.
#      Appending a new line.

#파일 삭제
import os
os.remove("example.txt")
#example.txt 파일이 삭제됨  
#파일 존재 여부 확인
if os.path.exists("example.txt"):
    print("File exists.")
else:   
    print("File does not exist.")
#출력: File does not exist. 
#파일이 존재하지 않음   

#파이썬에서는 함수 스코프와 블록 스코프가 다르게 동작한다.
#함수 내에서 정의된 변수는 함수 밖에서 접근할 수 없다.
def func():
    x = 10
    print(x)  # 함수 내에서는 접근 가능
func()
#출력: 10
#print(x)  # 함수 밖에서는 접근 불가, 오류 발생
#함수 내에서 함수 밖의 변수를 읽을 수는 있지만, 수정할 수는 없다.
if True:
    y = 20  # if 블록 내에서 정의된 변수
print(y)  # if 블록 밖에서도 접근 가능
#출력: 20
#파이썬은 블록 스코프를 따르지 않음

#파일 처리시 주의사항
#1. 파일을 열었으면 반드시 닫아야 함
#2. 파일이 존재하지 않을 때 읽기 모드로 열면 오류 발생
#3. 파일이 존재할 때 쓰기 모드로 열면 기존 내용이 삭제
#4. 파일 경로를 지정할 때 절대 경로와 상대 경로를 정확히 이해
#5. 파일 인코딩 문제에 주의 (특히 한글 처리 시)
#6. 예외 처리를 통해 파일 입출력 오류에 대비
#7. 대용량 파일 처리 시 메모리 사용에 주의
#8. 바이너리 파일과 텍스트 파일의 차이를 이해하고 적절한 모드로 열기
#9. with문을 사용하여 파일을 자동으로 닫기  
#10. 파일 권한 문제에 주의 (읽기/쓰기 권한 확인)
#11. 파일 이름에 특수 문자나 공백을 피하기
#12. 파일 경로 구분자에 주의 (운영체제별 차이)
#13. 파일 입출력 성능 최적화 고려 (버퍼링 등)
#14. 파일 백업 및 버전 관리 고려
#15. 파일 시스템의 제한 사항 이해 (파일 크기, 파일 수 등)
#16. 파일 입출력 시 데이터 무결성 확인 (예: 체크섬)
#17. 멀티스레딩 환경에서 파일 입출력 시 동기화 문제 주의
#18. 네트워크 파일 시스템(NFS) 사용 시 지연 시간 고려
#19. 로그 파일 작성 시 로테이션 및 관리 고려
#20. 파일 입출력 관련 라이브러리 및 도구 활용 (예: pandas, csv 등)

#한글 파일 쓰기
with open("korean.txt", "w", encoding="utf-8") as file:
    file.write("안녕하세요, 파일 입출력 테스트입니다.\n")
#한글 파일 읽기
with open("korean.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
#출력: 안녕하세요, 파일 입출력 테스트입니다.d

#korean.txt 파일이 삭제됨
os.remove("korean.txt")
#파일 입출력시 인코딩 문제 주의
#특히 한글 처리 시 인코딩을 명시적으로 지정하는 것이 좋음 (예: encoding="utf-8")

#인코딩과 UTF-8
#인코딩(Encoding)은 문자 데이터를 컴퓨터가 이해할 수 있는 이진 데이터로 변환하는 방법
#UTF-8은 유니코드 문자를 가변 길이의 바이트로 인코딩하는 방식
#UTF-8은 ASCII와 호환되며, 전 세계 대부분의 문자를 표현할 수 있음
#파이썬에서는 기본적으로 UTF-8 인코딩을 사용
#파일 입출력 시 인코딩을 명시적으로 지정하는 것이 좋음
#예: open("file.txt", "r", encoding="utf-8")
#인코딩 문제로 인해 한글이 깨지는 경우가 발생할 수 있음
#예: cp949, euc-kr 등 다른 인코딩 방식 사용 시
#인코딩 문제를 해결하려면 파일을 올바른 인코딩으로 열거나, 텍스트 에디터에서 인코딩을 변경


