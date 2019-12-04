
def isValid(pw):
    if (124075 < int(pw) < 580769):
        for i in range(0,5):
            if (pw[i] == pw[i+1]
            and not (i>0 and pw[i-1] == pw[i])
            and not (i<4 and pw[i+2] == pw[i])):
                return True
    return False

count = 0
isValid('222233')
for a in range(1, 10):
    for b in range(a, 10):
        for c in range(b, 10):
            for d in range(c, 10):
                for e in range(d, 10):
                    for f in range(e, 10):
                        pw = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                        if isValid(pw):
                            count += 1
print(count)
