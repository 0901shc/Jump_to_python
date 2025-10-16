# 자바는 한 변수에 타입을 지정하면 지정한 타입 외에 다른 타입은 사용할 수 없는 정적 언어다.
# 파이썬과 같은 동적언어는 타입을 쉽게 변경 가능하지만 프로젝트 규모가 커질수록 타입을 잘못 사용하여 버그가 생길 확률도 높아진다.
'''
파이썬은 동적 언어의 단점을 극복하기 위해 3.5 버전부터 타입 어노테이션 기능을 지원하기 시작했다. 
다만 정적 언어에서와 같은 강제적인 타입 체크가 아니라 타입 어노테이션(type annotation), 
즉 타입에 대한 힌트를 제공하는 정도의 기능만 지원한다. 
이는 동적 언어의 장점을 잃지 않으면서 
기존에 작성된 코드와의 호환성을 유지하려는 당연한 선택이라고 할 수 있다.
'''

num: int = 1
name: str = "홍길동"
numbers: list = [1, 2, 3]
#': 자료명' ->  이런식으로 변수의 타입을 명시할 수 있음


def add(a: int, b: int) -> int: 
    return a + b

def greet(name: str) -> str:
    return f"안녕하세요, {name}님!"

def get_user_info(user_id: int) -> dict:
    return {"id": user_id, "name": "홍길동"}
# 함수의 매개변수에도 같은 규칙을 적용하여 타입을 명시가능. 
# '-> 자료명'과 같이 화살표를 이용해서 함수의 반환값 타입도 명시가능










# typing 모듈
# 앞서 본 기본 타입 어노테이션만으로도 많은 경우를 처리할 수 있지만, 더 구체적인 타입 정보가 필요할 때가 있다.
# 이 때 사용하는 것이 typing 모듈이다.


# 1. 파이썬 버전별 타입 어노테이션의 발전
# 파이썬 3.5~3.8: typing 모듈 필수
from typing import List, Dict, Tuple, Optional

numbers: List[int] = [1, 2, 3]
user_info: Dict[str, int] = {"age": 30}

# 파이썬 3.9 이상: 내장 타입 사용 가능  
numbers: list[int] = [1, 2, 3]
user_info: dict[str, int] = {"age": 30}








# 2. typing 모듈이 여전히 필요한 경우들
from typing import Optional, Union, Callable, Any

# 1) Optional - None이 가능한 경우
user_name: Optional[str] = None  # str 또는 None

# 2) Union - 여러 타입이 가능한 경우  
user_id: Union[int, str] = "jenny"  # 정수 또는 문자열 (user_id로 정수도 사용가능)

# 3) Callable - 함수 타입 지정
def process_data(callback: Callable[[int], str]) -> str:
    return callback(42)

# 4) Any - 모든 타입 허용 (비상시에만 사용)
unknown_data: Any = {"key": "value"}

# 5) 복잡한 중첩 구조
nested_data: dict[str, list[Optional[int]]] = {
    "scores": [95, None, 87, None]
}






# 3. 실무에서의 권장사항
# 파이썬 3.9 이상을 사용한다면
from typing import Optional, Union  # 필요한 것만 가져오기

# 기본 타입은 내장 타입 사용
scores: list[int] = [95, 87, 92]
user_data: dict[str, str] = {"name": "홍길동"}

# 특별한 경우에만 typing 모듈 사용
def find_user(user_id: int) -> Optional[dict[str, str]]:
    # 사용자를 찾으면 딕셔너리 반환, 없으면 None 반환
    if user_id > 0:
        return {"name": "홍길동", "email": "hong@example.com"}
    return None





# mypy
# mypy는 정적 타입 검사기로, 코드를 실행하기 전에 타입 어노테이션이 올바른지 미리 확인해준다.
# 파이썬은 타입 어노테이션으로 매개변수의 타입을 명시하더라도 다음과 같이 다른 타입의 인수를 입력할 수 있다.
def add(a: int, b: int) -> int: 
    return a+b

result = add(3, 3.4)
print(result)  # 6.4 출력






