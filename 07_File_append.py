# 07_File_append.py

# append() : 파일끝에 데이터를 추가
# 파일열기모드 : a

f = open('test2.txt', 'a')
ap_data = '\n\nPython programming'
f.write(ap_data) # a mode로 열었기 때문에 파일 끝에 데이터 추가
f = open('test2.txt', 'r')
print(f.read())

f.close()
