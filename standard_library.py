#표준 라이브러리
#파이썬에서 기본적으로 제공하는 라이브러리
#예: os, sys, math, random, datetime, time, re, json, urllib, threading, multiprocessing, collections, itertools, functools, subprocess 등

import datetime
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)
diff = day2 - day1
print(diff.days)  #출력: 477

import time
time.time()  #출력: 1617181920.123456
time.localtime()  #출력: time.struct_time(tm_year=2021, tm_mon=3, tm_mday=30, tm_hour=12, tm_min=34, tm_sec=56, tm_wday=1, tm_yday=89, tm_isdst=0)
time.asctime()  #출력: 'Tue Mar 30 12:34:56 2021'
time.ctime() #출력: 'Tue Mar 30 12:34:56 2021'
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  #출력: '2021-03-30 12:34:56'
time.sleep(1)  #1초 대기 

import math 
math.gcd(60, 100, 80)  #출력: 20
math.lcm(60, 100, 80)  #출력: 240 

import random
random.random()  #출력: 0.1234567890123456 
random.randint(1, 10)  #출력: 7
random.choice(['apple', 'banana', 'cherry'])  #출력: 'banana' 
random.sample(range(1, 46), 6)  #출력: [3, 15, 22, 27, 33, 41] 
random.shuffle([1, 2, 3, 4, 5])  #출력: [3, 1, 4, 5, 2] 

import itertools 
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks =['사탕', '초콜릿', '젤리']
result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))
#출력: [('한민서', '사탕'), ('황지민', '초콜릿'), ('이영철', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')]   
#itertools.permutations(iterable, r) #순열
#itertools.combinations(iterable, r) #조합

import functools
data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)  #출력: 15
#functools.partial(함수, 고정값) #함수의 일부 매개변수를 고정시켜 새로운 함수 생성

from operator import itemgetter
data = [('apple', 3), ('banana', 1), ('cherry', 2)]
data.sort(key=itemgetter(1))
print(data)  #출력: [('banana', 1), ('cherry', 2), ('apple', 3)]
students = [{'name': '한민서', 'age': 20}, {'name': '황지민', 'age': 22}, {'name': '이영철', 'age': 21}]
result = sorted(students, key=itemgetter('age'))
print(result)  #출력: [{'name': '한민서', 'age': 20}, {'name': '이영철', 'age': 21}, {'name': '황지민', 'age': 22}]

from operator import attrgetter
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
students = [Student('한민서', 20), Student('황지민', 22), Student('이영철', 21)]
result = sorted(students, key=attrgetter('age'))
for student in result:
    print(student.name, student.age)
print(result)
#출력: 한민서 20
#      이영철 21
#      황지민 22
#attrgetter는 객체의 속성을 기준으로 정렬할 때 사용
#operator 모듈은 다양한 연산자 함수를 제공하여 함수형 프로그래밍에 유용하게 사용될 수 있음

import shutil
shutil.copy('source.txt', 'destination.txt')  #파일 복사 , 원본 파일을 복사하여 새 파일 생성
shutil.move('old_location.txt', 'new_location.txt')  #파일 이동 , 원본 파일을 새 위치로 이동

import glob
print(glob.glob('*.py'))  #현재 디렉터리의 모든 .py 파일 목록 출력
print(glob.glob('data/*.txt'))  #data 디렉터리의 모든 .txt 파일 목록 출력
#glob 모듈은 특정 패턴과 일치하는 파일 및 디렉터리 목록을 쉽게 가져올 수 있음

import pickle
f = open('test.txt', 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

import os
os.environ  #출력: environ({'PATH': '/usr/local/bin:/usr/bin:/bin', ...})
os.environ['PATH']  #출력: '/usr/local/bin:/usr/bin:/bin'
os.environ['MY_VAR'] = 'my_value'
os.chdir('/path/to/directory')  #디렉터리 변경
os.system("명령어")  #시스템 명령어 실행      
os.popen("dir")  #명령어 실행 결과를 파일 객체로 반환
os.mkdir('new_directory')  #새 디렉터리 생성
os.rmdir('old_directory')  #빈 디렉터리 삭제
os.remove('file.txt')  #파일 삭제
os.rename('old_name.txt', 'new_name.txt')  #파일 이름 변경

import zipfile
with zipfile.ZipFile('archive.zip', 'w') as myzip:   #파일 합치기
    myzip.write('file1.txt')  
    myzip.write('file2.txt')
    myzip.write('file3.txt')
with zipfile.ZipFile('archive.zip', 'r') as myzip:   #파일 해체하기
    myzip.extractall('extracted_files')

with zipfile.zipFile('archive.zip') as myzip:  #특정 파일만 추출하기
    myzip.extract('file1.txt')

with zipfile.ZipFile('archive.zip', 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as myzip:  #압축률 설정하기
    myzip.write('file1.txt')
    myzip.write('file2.txt')


#멀티스레드
#멀티스레드는 하나의 프로그램 내에서 여러 개의 스레드를 생성하여 동시에 작업을 수행하는 것
#스레드는 프로세스 내에서 실행되는 작은 단위
#멀티스레드를 사용하면 CPU 자원을 효율적으로 활용할 수 있음
#예: import threading
#     def 함수이름():
#         실행할 코드
#     스레드 = threading.Thread(target=함수이름)
#     스레드.start()
#     스레드.join()  #스레드가 종료될 때까지 기다림
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()  # join으로 스레드가 종료될 때까지 기다린다.

print("End")


import tempfile
filename = tempfile.mkstemp()
filename
f = tempfile.TemporaryFile()
f.close()



#트레이스백
#트레이스백은 파이썬에서 예외가 발생했을 때, 예외가 발생한 위치와 호출 스택을 출력하는 기능
#트레이스백을 통해 예외 발생 원인을 파악하고 디버깅할 수 있음
#예: import traceback
#     try:
#         실행할 코드
#     except 예외이름:
#         traceback.print_exc()  #트레이스백 출력
import traceback

def a():
    return 1/0
def b():
    a()

def mail():
    try: 
        b()
    except e:
        print("오류가 발생했습니다.")
        print(traceback.format_exc ())
    
main()


#json
#json은 자바스크립트 객체 표기법(JavaScript Object Notation)의 약자
#데이터를 교환하기 위한 경량 형식                                      
#파이썬에서는 json 모듈을 사용하여 json 데이터를 다룰 수 있음
#예: import json
#     json_data = '{"name": "홍길동", "age": 30, "city": "서울"}'
#     data = json.loads(json_data)  #json 문자열을 파이썬 객체로 변환
#     print(data['name'])  #출력: 홍길동
#     data['age'] = 31  #파이썬 객체 수정
#     new_json_data = json.dumps(data)  #파이썬 객체를 json 문자열로 변환
#     print(new_json_data)  #출력: {"name": "홍길동", "age": 31, "city": "서울"}
import json
with open('myinfo.json', 'r') as f:
    data = json.load(f)  #json 파일을 파이썬 객체로 변환
    print(data)
    print(data['name'])  #출력: 홍길동
type(data)  #출력: <class 'dict'>
data['age'] = 31  #파이썬 객체 수정
with open('myinfo.json', 'w') as f:
    json.dump(data, f)  #파이썬 객체를 json 파일로 변환
with open('myinfo.json', 'r') as f:
    new_data = json.load(f)
    print(new_data)
    print(new_data['age'])  #출력: 31
type(new_data)  #출력: <class 'dict'>
#json 모듈을 사용하면 파이썬 객체와 json 데이터 간의 변환이 용이하며, 파일 입출력도 간편하게 처리할 수 있음
#json 모듈은 파이썬 표준 라이브러리에 포함되어 있어 별도의 설치 없이 사용할 수 있음
#json 모듈은 다양한 데이터 타입을 지원하며, 복잡한 데이터 구조도 쉽게 표현할 수 있음
#json 모듈은 데이터 교환 및 저장에 널리 사용되며, 웹 개발, API 통신 등 다양한 분야에서 활용됨

#urllib
#urllib 모듈은 파이썬에서 URL을 다루기 위한 표준 라이브러리
#URL 요청, 응답 처리, URL 파싱 등의 기능을 제공
import urllib.request

def get_wikidocs(page):
    resource = 'https://wikidocs.net/{}'.format(page)
    with urllib.request.urlopen(resource) as s :
        with open('wikidocs_%s.html' % page, 'wb') as f:
            f.write(s.read())

#webbrowser
#webbrowser 모듈은 파이썬에서 기본 웹 브라우저를 제어하기 위한 표준 라이브러리
#웹 페이지 열기, 새 창 또는 새 탭에서 열기 등의 기능을 제공
import webbrowser
webbrowser.open('http://google.com')  #기본 웹 브라우저에서 구글 열기
webbrowser.open_new('http://google.com')  #새 창에서 구글 열기
webbrowser.open_new_tab('http://google.com')  #새 탭에서 구글 열기