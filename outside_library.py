#외부 라이브러리
 

#pip
#파이썬 패키지 관리자
#https://pypi.org/
#패키지 설치, 업그레이드, 삭제, 목록 확인, 정보 확인 등의 기능 제공
#pip는 파이썬 설치 시 기본적으로 함께 설치됨
#pip의 가장 큰 장점은 의존성 있는 패키지들도 함께 설치해준다는 것
#pip 사용법 
#pip install 패키지이름 #패키지 설치
#pip uninstall 패키지이름 #패키지 삭제
#pip list #설치된 패키지 목록 확인
#pip show 패키지이름 #패키지 정보 확인
#pip install --upgrade 패키지이름 #패키지 업그레이드


#Faker
#Faker는 가짜 데이터를 생성해주는 파이썬 라이브러리
#가짜 이름, 주소, 전화번호, 이메일, 회사명, 날짜 등 다양한 유형의 데이터를 생성할 수 있음
#Faker 설치: pip install Faker
#Faker 사용법
from faker import Faker
fake = Faker('ko_KR')  #한국어 데이터 생성
print(fake.name())  #가짜 이름 생성
print(fake.address())  #가짜 주소 생성
print(fake.phone_number())  #가짜 전화번호 생성
print(fake.email())  #가짜 이메일 생성
print(fake.company())  #가짜 회사명 생성
print(fake.date_of_birth())  #가짜 생년월일 생성
print(fake.text())  #가짜 텍스트 생성
#Faker는 테스트 데이터 생성, 데이터베이스 초기화, 웹 스크래핑 등 다양한 용도로 활용될 수 있음
#Faker는 파이썬 표준 라이브러리가 아니므로 별도의 설치가 필요함
#Faker는 다양한 언어와 국가의 데이터를 지원함
#Faker는 커스터마이징이 가능하여 사용자가 원하는 유형의 데이터를 생성할 수 있음
#Faker는 오픈 소스 라이브러리로, GitHub에서 소스 코드를 확인하고 기여할 수 있음


#sympy
#sympy는 파이썬에서 수학 기호 연산을 수행할 수 있는 라이브러리
#대수학, 미적분학, 방정식 풀이, 행렬 연산 등 다양한 수학적 기능을 제공
#sympy 설치: pip install sympy
#sympy 사용법
from sympy import symbols, expand, factor, solve, Matrix
x, y = symbols('x y')  #변수 정의
expr = x**2 + 2*x*y + y**2
print(expand(expr))  #식 전개
print(factor(expr))  #식 인수분해
eq = x**2 + 2*x + 1
print(solve(eq, x))  #방정식 풀이
matrix = Matrix([[1, 2], [3, 4]])
print(matrix.inv())  #행렬의 역행렬
#sympy는 수학적 문제 해결, 과학적 계산, 공학적 분석 등 다양한 분야에서 활용될 수 있음
#sympy는 파이썬 표준 라이브러리가 아니므로 별도의 설치가 필요함
#sympy는 오픈 소스 라이브러리로, GitHub에서 소스 코드를 확인하고 기여할 수 있음
#sympy는 심볼릭 연산을 지원하여 수학적 표현식을 그대로 다룰 수 있음
#sympy는 LaTeX 형식으로 수학적 표현식을 출력할 수 있음  
#sympy는 수학적 표현식을 시각화하기 위한 다양한 플로팅 기능을 제공함
