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




















