# Github: EchTR
def xo(s):
    x_s = 0
    y_s = 0
    for i in s:
        if(i.lower() == "x"):
            x_s = x_s + 1
        elif(i.lower() == "o"):
            y_s = y_s + 1
    if(x_s == y_s):
        return True
    else:
        return False
input(xo("xxoo"))