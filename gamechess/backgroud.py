def background(v,t):
    for i in range (1,7):
        a=" "
        for k in range (1,7):
            if t==[i,k]:
                a=a+" ## "
            elif v==[i,k]:
                a=a+" ** "
            else:
                a=a +' __ '

        print(a)



