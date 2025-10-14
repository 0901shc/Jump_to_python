# 프로그램을 만드는 방법
'''
1. 문제 정의: 해결하고자 하는 문제를 명확히 정의합니다.
2. 요구사항 분석: 문제를 해결하기 위한 요구사항을 분석합니다.
3. 설계: 프로그램의 구조와 동작 방식을 설계합니다.
4. 구현: 설계에 따라 코드를 작성합니다.
5. 테스트: 작성한 코드가 올바르게 동작하는지 테스트합니다.
6. 배포: 프로그램을 사용자에게 배포합니다.
7. 유지보수: 프로그램의 버그를 수정하고 기능을 개선합니다.
'''

#예: 계산기 프로그램 만들기

#1. 문제 정의: 두 수를 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하는 계산기 프로그램 만들기
#2. 요구사항 분석: 사용자가 입력한 두 수에 대해 사칙연산을 수행하고 결과를 출력해야 합니다.
#3. 설계: 클래스와 메서드를 사용하여 계산기 기능을 구현합니다.
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
#4. 구현: 위의 설계에 따라 코드를 작성합니다.
a = FourCal()
a.setdata(4, 2)
print(a.add())  #출력: 6
print(a.mul())  #출력: 8
print(a.sub())  #출력: 2
print(a.div())  #출력: 2.0
#5. 테스트: 작성한 코드가 올바르게 동작하는지 테스트합니다.
#위의 출력 결과를 통해 코드가 올바르게 동작함을 확인할 수 있습니다.
#6. 배포: 프로그램을 사용자에게 배포합니다.
#이 단계는 실제 배포 환경에 따라 다르므로 생략합니다.
#7. 유지보수: 프로그램의 버그를 수정하고 기능을 개선합니다.
#예: 나눗셈에서 0으로 나누는 경우를 처리하는 기능 추가
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
#위의 예제는 프로그램을 만드는 전반적인 과정을 보여줍니다.



# 예제 1 : 1부터 1000까지의 수 중에서 3 또는 5로 나누어 떨어지는 수의 합을 구하는 프로그램 만들기
# 문제정의 : 1000미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라
# 요구사항 분석 : 1부터 999까지의 수 중에서 3 또는 5로 나누어 떨어지는 수를 모두 더한다
# 설계 : for문과 if문을 사용하여 1부터 999까지의 수를 반복하면서 3 또는 5로 나누어 떨어지는 수를 찾고, 그 수를 누적하여 더한다
# 구현 : 아래 코드 참조

total = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
    
print(total)
# 테스트 : 위의 코드를 실행하여 결과가 올바른지 확인한다
# 배포 : 이 단계는 실제 배포 환경에 따라 다르므로 생략한다
# 유지보수 : 프로그램의 버그를 수정하고 기능을 개선한다
# 예를 들어, 3과 5 이외의 다른 수로 나누어 떨어지는 수의 합을 구하는 기능을 추가할 수 있다  



# 예제 2 : 책 페이지 수와 한 페이지에 들어가는 글자 수를 입력받아 총 몇 페이지가 필요한지 계산하는 프로그램 만들기
def get_total_page(m,n):
    if m%n == 0:
        return(m//n)
    else:
        return(m//n + 1)

print(get_total_page(5,10)) #1
print(get_total_page(15,10)) #2
print(get_total_page(25,10)) #3
print(get_total_page(30,10)) #3
