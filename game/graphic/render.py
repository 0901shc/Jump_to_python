# render.py


#상대경로 패키지
#패키지 내에서 상대경로를 사용하여 모듈을 import 할 수 있음
#예: from .모듈이름 import 함수이름

from game.sound.echo import echo_test
def render_test():
    print("render")
    echo_test()
# 출력: render
#      echo 

from ..sound.echo import echo_test as echo_test2
def render_test2():
    print("render2")
    echo_test2()
# 출력: render2
#      echo

#접근자
#.. : 부모 디렉터리
#.  : 현재 디렉터리