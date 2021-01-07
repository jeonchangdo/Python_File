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