# 01_File_creation.py

# 파일 생성 : 파일명만 적으면 현재 디렉터리에 생성

f = open('file1.txt', 'w') # f변수에 파일을 참조할 수 있는 포인터(화살표) 저장
f.close() # f가 포인터하고 있는 file을 닫는다.
# w 모드는 해당 파일이 없으면 생성
# 해당 파일이 존재하면 기존 파일을 초기화 해서 열어주게 되는데 저장되어 있던 내용은 삭제 된다.

# 존재하지 않는 디렉터리에 생성하면 에러
# f = open('c:/python/file.txt', 'w') # 현재 폴더 외 다른 폴더에 파일을 만들고 싶으면 전체 경로를 적는다.
# f.close() # FileNotFoundError: [Errno 2] No such file or directory: 'c:/python/file.txt'
# f.close()

# 파이썬은 경로 표시로 / 를 사용
f = open('d:/pythonstudy/file1.txt', 'w')
f.close()

# # 경로에 \ 사용하려면 \\ 표시
# a = open('c:\\pythonstudy\\file2.txt', 'w')
# a.close()

# 파일에 data 보내기(쓰기) : 파일을 쓰기모드(w)로 열고
# 파일 객체의 write() 함수로 값을 파일에 기록
data = 'hi22222'
f = open('d:/pythonstudy/file1.txt', 'w')
f.write(data) # 파일에 data 쓰기
f.close()























