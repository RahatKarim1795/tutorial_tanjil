def rec(ar):
    ar +=1
    if ar>4:
        return ar

    return rec(ar)

a = 1
print(rec(a))