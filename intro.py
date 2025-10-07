# 파이썬(Python)은 1991년 네덜란드의 귀도 반 로섬(Guido van Rossum)이 개발한 인터프리터 언어이다. 귀도는 파이썬이라는 이름을 자신이 좋아하는 코미디 쇼인 ‘몬티 파이썬의 날아다니는 서커스(Monty python's flying circus)’에서 따왔다고 한다.
# 파이썬은 문법이 간결하고 쉬워서 초보자들이 배우기에 좋다. 또한 다양한 라이브러리와 프레임워크를 제공하여 데이터 분석, 인공지능, 웹 개발 등 다양한 분야에서 활용되고 있다.
# 파이썬은 인터프리터 언어로, 코드를 작성한 후 바로 실행할 수 있다. 이는 개발자들이 코드를 빠르게 테스트하고 디버깅 할 수 있게 해준다. 또한 파이썬은 객체지향 프로그래밍(OOP)을 지원하여 코드의 재사용성과 유지보수성을 높여준다.
# 파이썬은 다양한 운영체제에서 사용할 수 있으며, 무료로 배포되고 있다. 이러한 장점들 덕분에 파이썬은 전 세계적으로 많은 개발자들 사이에서 인기를 끌고 있다.


# 파이썬 macos 설치
# 1. 홈브류 설치
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# 2. 파이썬 설치
# brew install python
# 3. 파이썬 버전 확인
# python3 --version
# 4. pip 버전 확인
# pip3 --version
# 5. 가상환경 설치
# python3 -m venv 가상환경이름
# 6. 가상환경 실행
# source 가상환경이름/bin/activate
# 7. 가상환경 종료
# deactivate  
# 8. 가상환경 삭제
# rm -rf 가상환경이름
# 9. 패키지 설치
# pip3 install 패키지이름
# 10. 설치된 패키지 확인
# pip3 list
# 11. 패키지 삭제
# pip3 uninstall 패키지이름
# 12. 설치된 패키지를 requirements.txt 파일로 저장
# pip3 freeze > requirements.txt
# 13. requirements.txt 파일로 패키지 설치
# pip3 install -r requirements.txt
# 14. 파이썬 종료
# exit()
# 15. 파이썬 실행
# python3
# 16. 파이썬 파일 실행
# python3 파일이름.py
# 17. 파이썬 파일 실행(가상환경)
# 가상환경이름/bin/python 파일이름.py


# VS Code 마켓플레이스에서 'Code Runner' 확장 프로그램 설치
# 단축키: Ctrl + Alt + N (실행)
# 실행 결과는 우측 상단의 OUTPUT 창에서 확인 가능
# 실행 취소 단축키: Ctrl + Alt + M (실행 취소)
# 실행 결과 창 클리어 단축키: Ctrl + Alt C (실행 결과 창 클리어)


# vscode auto save 설정
# 1. Command + , (설정 열기)
# 2. "Auto Save" 검색
# 3. "Files: Auto Save" 옵션을 "afterDelay"로 설정
# 4. "Files: Auto Save Delay" 옵션을 원하는 시간(밀리초)으로 설정 (예: 1000ms = 1초)
# 5. 설정 창 닫기
# 6. 이제 파일을 저장하지 않아도 설정한 시간 후에 자동으로 저장됨