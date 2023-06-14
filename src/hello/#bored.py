
def clock(b, p, e, op):
    if p == 0:
        return e
    elif p == 1:
        return b
    else:
        return op(b, clock(b, p-1, e, op))


def concat_str(str1, str2):
    return str1 + str2


#print(clock("hello-", 6, "", concat_str))


def monoid_fast_power(b,p,e,op):
    if p == 0:
        return e
    elif p == 1:
        return b
    elif p % 2 == 0:    #even
        return monoid_fast_power(op(b,b), p//2,e,op)
    else:               #odd
        return op(b,monoid_fast_power(b,p-1,e,op))

print(monoid_fast_power("hello-", 103, "", concat_str))