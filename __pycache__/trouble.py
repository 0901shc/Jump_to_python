#예외 처리

#오류는 언제 발생하는가?
#1. 문법적으로 잘못된 경우(SyntaxError)
#2. 코드 실행 중에 발생하는 경우(Exception)
#   - 예: ZeroDivisionError, IndexError, KeyError, TypeError, ValueError 등
#3. 시스템 관련 오류(SystemError, MemoryError 등)
#4. 사용자가 임의로 발생시키는 경우(Raise)          


#예외 처리 방법
#1. try-except 구문
#2. try-except-finally 구문
#3. try-except-else 구문
#4. 예외 발생시키기(raise)
#5. 사용자 정의 예외 만들기 (class MyError(Exception): ...) 
#6. with 구문과 예외 처리
#7. assert 구문과 예외 처리
#8. 예외 계층 구조 이해하기
#9. 여러 예외 처리하기
#10. 예외 무시하기
#11. 예외의 원인 알기 (import traceback)
#12. 예외와 로그 (import logging)
#13. 예외 전파 (함수에서 발생한 예외를 호출한 쪽으로 전달)
#14. 예외 처리 시 주의할 점 (except 구문에서 모든 예외를 잡지 않기)
#15. 예외 처리 시 성능 고려하기 (try 구문 안에 많은 코드를 넣지 않기)
#16. 예외 처리 시 가독성 고려하기 (try 구문을 너무 많이 중첩하지 않기)
#17. 예외 처리 시 디버깅 고려하기 (예외 발생 시 디버깅 정보를 출력하기)
#18. 예외 처리 시 테스트 고려하기 (예외 상황에 대한 테스트 코드 작성하기)
#19. 예외 처리 시 문서화 고려하기 (함수나 클래스의 예외 상황 문서화하기)
#20. 예외 처리 시 팀원과의 협업 고려하기 (예외 처리 방식에 대한 팀 내 합의)
#21. 예외 처리 시 최신 파이썬 버전 고려하기 (최신 버전의 예외 처리 기능 활용하기)
#22. 예외 처리 시 외부 라이브러리 고려하기 (외부 라이브러리의 예외 처리 방식 이해하기)
#23. 예외 처리 시 보안 고려하기 (예외 메시지에 민감한 정보 포함하지 않기)
#24. 예외 처리 시 사용자 경험 고려하기 (사용자에게 친절한 예외 메시지 제공하기)
#25. 예외 처리 시 로그 파일 관리 고려하기 (로그 파일 크기 관리하기)
#26. 예외 처리 시 성능 모니터링 고려하기 (예외 발생 빈도 모니터링하기)
#27. 예외 처리 시 코드 리뷰 고려하기 (예외 처리 코드에 대한 코드 리뷰 진행하기)
#28. 예외 처리 시 린트 도구 활용하기 (예외 처리 관련 린트 규칙
#29. 예외 처리 시 자동화 도구 활용하기 (예외 처리 관련 자동화 도구 활용하기)
#30. 예외 처리 시 커뮤니티 자료 활용하기 (예외 처리 관련 커뮤니티 자료 참고하기)
#31. 예외 처리 시 최신 트렌드 고려하기 (예외 처리 관련 최신 트렌드 파악하기)
#32. 예외 처리 시 지속적인 학습 고려하기 (예외 처리 관련 지속적인 학습하기)
#33. 예외 처리 시 코드 품질 고려하기 (예외 처리 코드의 품질 유지하기)
#34. 예외 처리 시 유지보수 고려하기 (예외 처리 코드의 유지보수성 높이기)

#예외 처리 예제
#1. try-except 구문
#try:
#    실행할 코드
#except [발생오류[as 오류변수]]:
#    예외 발생 시 실행할 코드
# []는 생략 가능, 여러 개의 오류를 한꺼번에 처리할 수도 있음
#예: ZeroDivisionError, IndexError, KeyError, TypeError, ValueError 등
#예외가 발생하지 않으면 try 블록의 모든 코드가 실행된 후 except 블록은 건너뜀
#예외가 발생하지 않으면 except 블록은 실행되지 않음
#예외가 발생하면 except 블록이 실행되고 프로그램이 종료되지 않음
try:
    4 / 0
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    print(e)
#출력: 0으로 나눌 수 없습니다.
#      division by zero     




#1-1 try-except만 사용
try:
    4 / 0
except:
    print("에러가 발생했습니다.")
#출력: 에러가 발생했습니다.
#1-2 발생 오류만 포함한 except 사용
try:
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
#출력: 0으로 나눌 수 없습니다.
#1-3 발생 오류와 오류 변수까지 포함한 except 사용
try:
    4 / 0
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    print(e)
#출력: 0으로 나눌 수 없습니다.
#      division by zero
#1-4 여러 개의 오류를 한꺼번에 처리
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print("0으로 나눌 수 없거나 잘못된 인덱스입니다.")
    print(e)
#출력: 0으로 나눌 수 없거나 잘못된 인덱스입니다.
#      list index out of range
#1-5 모든 오류를 한꺼번에 처리
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except Exception as e:
    print("알 수 없는 에러가 발생했습니다.")
    print(e)
#출력: 알 수 없는 에러가 발생했습니다.
#      list index out of range  




#2. try-finally 구문
#try:
#    실행할 코드
#finally:
#    예외 발생 여부와 상관없이 항상 실행할 코드
#finally 블록은 예외가 발생하든 발생하지 않든 항상 실행됨
#예외가 발생하지 않으면 try 블록의 모든 코드가 실행된 후 finally 블록이 실행됨
try:
    4 / 0
finally:
    print("무조건 실행")
#출력: 무조건 실행
#예외가 발생했지만 프로그램이 종료되지 않음 (예외가 발생했음을 알리는 메시지가 출력됨)

#3 여러개의 오류 처리하기
#try:
#    실행할 코드
#except 발생오류1:
#    예외 발생 시 실행할 코드1
#except 발생오류2:
#    예외 발생 시 실행할 코드2
#except 발생오류3:
#    예외 발생 시 실행할 코드3
#...
#except 발생오류n:
#    예외 발생 시 실행할 코드n
#except 구문은 여러 개 사용할 수 있음
#예: ZeroDivisionError, IndexError, KeyError, TypeError, ValueError 등
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("잘못된 인덱스입니다.")
#출력: 잘못된 인덱스입니다.
#예외가 발생했지만 프로그램이 종료되지 않음


#4 try-else 구문
#try:
#    실행할 코드
#except [발생오류[as 오류변수]]:
#    예외 발생 시 실행할 코드
#else:
#    예외가 발생하지 않았을 때 실행할 코드
# []는 생략 가능, 여러 개의 오류를 한꺼번에 처리할 수도 있음
#예: ZeroDivisionError, IndexError, KeyError, TypeError, ValueError 등
#예외가 발생하지 않으면 try 블록의 모든 코드가 실행된 후 else 블록이 실행됨
#예외가 발생하지 않으면 except 블록은 실행되지 않음
#예외가 발생하면 except 블록이 실행되고 프로그램이 종료되지 않음
try:
    4 / 2
except ZeroDivisionError as e: 
    print("0으로 나눌 수 없습니다.")
    print(e)
else:
    print("예외가 발생하지 않았습니다.")
#출력: 예외가 발생하지 않았습니다.
#예외가 발생하지 않았지만 프로그램이 종료되지 않음


#오류 회피하기
1. pass 문 사용하기
#try:
#    실행할 코드
#except [발생오류[as 오류변수]]:
#    pass
2. continue 문 사용하기
#for i in 반복가능객체:
#    try:
#        실행할 코드
#    except [발생오류[as 오류변수]]:
#        continue

#오류 일부러 발생시키기
#raise [발생오류[as 오류변수]]
class Bird:
    def fly(self):
        raise NotImplementedError
class Eagle(Bird):
    def fly(self):
        print("very fast")
eagle = Eagle()
eagle.fly()  #출력: very fast
bird = Bird()
bird.fly()  #NotImplementedError 예외 발생

#예외 만들기
#class 예외클래스이름(Exception):
#    pass
class MyError(Exception):
    def __str__(self):
        return "MyError 발생"
try:
    raise MyError
except MyError as e:
    print(e)
#출력: MyError 발생