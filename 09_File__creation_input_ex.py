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