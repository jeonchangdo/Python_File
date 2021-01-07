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

# --readlines() 없이 파일 읽어오기 --
f3 = open('test.txt', 'r')

for line in f3 : # 파일객체를 직접 반복요소로 사용 가능 내부적으로 f3.readlines() 자동수행 되면서
    print(line, end= '') # 1행씩 출력

f3.close()



