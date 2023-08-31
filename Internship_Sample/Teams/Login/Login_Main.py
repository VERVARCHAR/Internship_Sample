def format(i):
    if i == 0:
        return 0
    elif i == 1:
        return 0
    else:
        return 1

def Login():
    i = 99
    while format(i):
        print("Login")
        print("0:Admin,1:User,others:Error  : ",end="")
        i = input()
        i = int(i)
        if i >= 2:
            print("Too Large")
        elif i == 0:
            args = i
        else:
            args = i
    return args
    