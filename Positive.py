def even(a,b,c):
    if a>0 and b>0 and a % 2 == 0 and b % 2==0 and c % 2!=0:
        print(True)
        return True
    elif a>0 and c>0 and a % 2 == 0 and c % 2==0 and b % 2!=0:
        print(True)
        return True
    elif b>0 and c>0 and b % 2 == 0 and c % 2==0 and c % 2!=0:
        print(True)
        return True
    else:
        print(False)
        return False
even(4,8,9)