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