def even(a,b,c):
    # Use of if statement to provide the diffrent situations that will return true
    #~Only even numbers above 0 are considered to output true
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