# 클로저 : 외부 함수의 변수를 기억하는 내부 함수, 함수가 생성 될때의(번수 값)을 기억하는 특별한 함수
# 외부함수는 클로저를 리턴값으로 반환한다. 
# 클로저 팩토리 함수 : 기존함수를 감싸서 새로운 함수를 만들어내게 하는 함수
# 데코레이터 : 기존 함수를 바꾸지 않고 기능을 추가할 수 있게 만드는 함수 (함수를 꾸미는 함수라고 함)
# 클로저는 계속해서 새로운 함수를 만들어낼 수 있도록 찍어내고, 데코레이터는 기존 함수를 감싸는 함수


# decorator.py
import time

def elapsed(original_func):   # 기존 함수를 인수로 받는다.
    def wrapper():
        start = time.time()
        result = original_func()    # 기존 함수를 수행한다.
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 반환한다.
    return wrapper

@elapsed
def myfunc():
    print("함수가 실행됩니다.")

# decorated_myfunc = elapsed(myfunc)  # @elapsed 데코레이터로 인해 더이상 필요하지 않다.
# decorated_myfunc()

myfunc()


# 데코레이터 함수 는 기존 함수의 입력 인수에 상관없이 동작하도록 만들어야 한다!
# 왜냐면 데코레이터는 기존 함수가 어떤 입력 인수를 취할지 알 수 없기 때문이다.
# 만약에 데코레이터 함수로 입력값을 받고 싶으면 *args와 **kwargs를 wrapper 함수의 매개변수로 설정하면 된다.
# args : 모든 입력 인수를 튜플로 변환하는 매개변수
# kwargs : 모든 '키=값'형태의 인수를 딕셔너리로 변환하는 매개변수 

