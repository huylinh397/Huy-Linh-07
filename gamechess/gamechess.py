from backgroud import background
import random
vua_height=random.randint(1,6)
vua_lenght=random.randint(1,6)
tot_height=int(input("Nhập toạ độ quân tốt"))
tot_lenght=int(input("Nhập toạ độ quân tốt"))
while True:
    v=[vua_height,vua_lenght]
    t=[tot_height,tot_lenght]
    background(v,t)
    if v==t:
        print('chiến thẳng')
        break
    tot_move=str(input("Nhập hướng di chuyển quân tốt"))
    if tot_move=="w":
        tot_height=tot_height-1
    elif tot_move=="a":
        tot_lenght=tot_lenght-1
    elif tot_move=="d":
        tot_lenght=tot_lenght+1
    elif tot_move=="s":
        tot_height=tot_height+1
    v=[vua_height,vua_lenght]
    t=[tot_height,tot_lenght]
    background(v,t)
    if v==t:
        print('chiến thẳng')
        break
    vua_move=str(input("Nhập hướng di chuyển quân vua"))
    if vua_move=="w":
        vua_height=vua_height-1
    elif vua_move=="a":
        vua_lenght=vua_lenght-1
    elif vua_move=="d":
        vua_lenght=vua_lenght+1
    elif vua_move=="s":
        vua_height=vua_height+1
