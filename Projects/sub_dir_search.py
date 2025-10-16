# 특정 디렉터리부터 시작해서 그 하위(디렉터리 포함)의 모든 파일 중 
# 파이썬 파일(*.py)만 출력해 주는 프로그램을 만들려면 어떻게 해야 할까? 
# 이런 프로그램은 프로젝트에서 모든 파이썬 파일을 찾거나, 코드 분석을 할 때 매우 유용하다.


# C:/doit/sub_dir_search.py
import os
import sys

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py': 
                    print(full_filename)
    except PermissionError:
        pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("사용법: python sub_dir_search.py <검색할_디렉터리>")
        sys.exit()

    search_dir = sys.argv[1]
    if os.path.exists(search_dir):
        search(search_dir)
    else:
        print(f"디렉터리가 존재하지 않습니다: {search_dir}")
