f = open('test2.txt', 'r')
f.seek(0,0) # 시작위치 (offset, 위치) : 파일에 시작점에서 0번째 문자
# (0,0) : 0행 0열 (파일 시작위치)

# 첫번째 행만 출력
f.seek(0,0)
line = f.readline()
print(line, end='')

f.seek(7,0)
line = f.readline()
print(line, end='')

f.seek(14,0)
line = f.readline()
print(line, end='')

f.close()