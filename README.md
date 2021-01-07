# 파일 입출력

## 00_File

​	<img src="md-images/image-20210106172704446.png" alt="image-20210106172704446" style="zoom:50%;" />

​	<img src="md-images/image-20210106172737935.png" alt="image-20210106172737935" style="zoom:50%;" />

​	<img src="md-images/image-20210106173041211.png" alt="image-20210106173041211" style="zoom:50%;" />

​	<img src="md-images/image-20210106173112408.png" alt="image-20210106173112408" style="zoom:50%;" />

​	<img src="md-images/image-20210106174252011.png" alt="image-20210106174252011" style="zoom:50%;" />

## 01_File_creation.py

```python
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
```

## 02_File_data_write.py

```
# 02_File_data_write.py

# 파일에 한글 쓰기 - 한글 인코딩 문제

# 파일에 data 보내기(쓰기) : 파일을 쓰기모드(w)로 열고
# 파일 객체의 write() 함수로 값을 파일에 기록

data = '안녕하세요. 반갑습니다.'
f = open('file1.txt', 'w',encoding= 'utf-8') # 문자 인코딩 방식 지정(utf-8)
f.write(data) # 파일에 data 쓰기
f.close()

# 파일에 여러행 데이터 쓰기('\n')
f = open('file4.txt', 'w', encoding= 'utf-8')

for i in range(1,11) :
    data = '%d 행\n' % i
    f.write(data)
f.close()
```

## 03_File_read.py

<img src="../../AppData/Roaming/Typora/typora-user-images/20210107094134.png" alt="20210107094134" style="zoom:50%;" />

```python
# 03_File_read.py

# readline()
# 1개 행씩 읽어오기
# 1행 끝에 '\n'을 포함
# readlines()
# 모든행을 읽어 라인별로 잘라서 리스트 생성 후 반환
# 그 리스트에는 1개의 행이 1개의 요소로 들어감
# read()
# 내용 전체를 읽어서 문자열로 반환

# open 함수의 mode를 'r'로 설정해서 파일객체 생성

print('---------첫번째 행 읽기------------')
f = open('test.txt', 'r')
line = f.readline() # 첫번째 라인 1개 읽기
print('')
print(line)
print('끝입니다')
f.close()

# readline() 함수를 이용해서 전체라인 읽어오는 코드
# 결과는 1행 출력하고 줄바꿈 그리고 print문이 줄바꿈해서 2줄 간격이 생김
print('---------파일 전체 읽기------------')
f2 = open('test.txt', 'r')

while True : # 무한반복
    line = f2.readline() # 라인 1개 읽고 포인터를 다음행으로 이동
    if not line :
        break
    # print(line) # 2줄 간격으로 출력
    print(line, end='') # print문의 줄바꿈 실행하지 않음

f2.close()
```

## 04_File_read_all.py

```python
# 04_File_read_all.py

# readlines() 함수를 이용
# 리스트형 반환
print('-----전체 라인 읽고 출력-----')

f1 = open('test.txt', 'r')
lines = f1.readlines() # 리스트 생성
print(lines)
f1.close()

# 전체라인 읽어서 1행씩 출력

f2 = open('test.txt', 'r')
lines = f2.readlines() # 리스트 생성

for line in lines :
    print(line, end= '')

f2.close()
```

## 05.File_pointer_move.py

![20210107102212]()<img src="md-images/20210107102031.png" alt="20210107102031" style="zoom:50%;" />



<img src="md-images/20210107102406.png" alt="20210107102406" style="zoom:50%;" /><img src="md-images/20210107102506.png" alt="20210107102506" style="zoom:50%;" />

```python
# 05_File_pointer_move.py
# 파일내 포인터이동 seek()

# 파일내에서 검색(위치이동)
# seek(offset, whence) 함수

print('-------파일내에서 검색 : seek()----------')

f = open('test2.txt', 'r')
f.seek(0,0) # 시작위치 (offset, 위치) : 파일에 시작점에서 0번째 문자
# (0,0) : 0행 0열 (파일 시작위치)

# 파일 전체 읽어오기(리스트 반환)
lines = f.readlines()
print(lines) # 리스트 출력

# 포인터 위치 변경
f.seek(1,0) # offset1, 위치-문서처음
lines = f.readlines()
print(lines)

# 두번째행부터 읽어오기
f.seek(7,0) # offset7, 위치-문서처음
lines = f.readlines()
print(lines)

# 한글은 12바이트
# 시작위치부터 offset 14부터 읽어오기
f.seek(14, 0)
lines = f.readlines()
print(lines)

f.seek(16, 0) # 3번째 행 두번째 글자 (한글이므로 이전 글자 위치에서 2씩 증가 시켜야 함)
lines = f.readlines()
print(lines)
f.close()
```

### 연습문제

<img src="md-images/20210107104401.png" alt="20210107104401" style="zoom:50%;" />![20210107104736](md-images/20210107104736.png)

##  06_File_read_all_list.py

```python
# 06_File_read_all_list.py

# read() : 파일의 내용 전체를 일겅서 1개의 문자열로 반환하는 함수

f = open('test2.txt', 'r')

data = f.read()
print(data)
print(type(data))
print(len(data))

# 사용자로부터 문자를 입력받아 파일 내에서 검색
f = open('test2.txt', 'r')
data = f.read()

value = input('검색값 입력 : ')

# 판단
if value in data :
    print('있음')
else :
    print("없음")
f.close()
```

## 07_File_append.py

```python
# 07_File_append.py

# append() : 파일끝에 데이터를 추가
# 파일열기모드 : a

f = open('test2.txt', 'a')
ap_data = '\n\nPython programming'
f.write(ap_data) # a mode로 열었기 때문에 파일 끝에 데이터 추가
f = open('test2.txt', 'r')
print(f.read())

f.close()
```

## 08_File_with.py

```python
# 08_File_with.py

# with문으로 파일열기
# 파일을 자동으로 close 하는 등 관리르 해주는 문장 - with

# with open(파일명, 열기모드) as 파일객체변수명 :
#     처리코드

# with문이 종료되면 파일객체는 자동으로 close()

with open('test3.txt', 'w') as f :
    f.write('hello')

# 변수로 처리
file = 'test4.txt'
data = '''Python programming
R programming
Web programming'''

with open(file, 'w') as f :
    f.write(data)
```

##  09_File__creation_input_ex.py

<img src="md-images/20210107112049-1609986079275.png" alt="20210107112049" style="zoom:50%;" />

```python
# 09_File__creation_input_ex.py

f = open('memver.scv','w',encoding='utf-8')

while True :
    name = input("이름입력, 종료하려면 이번 입력에서 quit를 입력.")
    if name == 'quit' :
        break
    birth = input("생년월일 : ")
    addr = input("주소 : ")

    mem = name+ ',' +birth+ ',' +addr+'\n'
    f.write(mem)

f.close()
```