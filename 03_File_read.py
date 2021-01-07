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












