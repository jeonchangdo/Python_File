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