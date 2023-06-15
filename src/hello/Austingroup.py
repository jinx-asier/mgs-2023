def is_group(q, op):
    return isMonoiod(q, op) and hasInverse(q, op)


def isMonoiod(q, op):
    return isClosed() and isAssociative() and findIdentity()


def isClosed(q, op):
    return all(op(x, y) in q
               for x in q
               for y in q)


def isAssociative(q,op):
    raise NotImplemented


def findIdentity(q,op):
    for x in q:
        if all(op(x, y) == y and op(y, x) == y for y in q):
            return x
    return None


def hasInverse(q, op):
    return all(findInverse(x) for x in q)


def findInverse(x, q, op):
    e = findIdentity(q, op)
    if e is False:
        return False
    else:
        for y in q:
            if op(y, x) == e:
                return y
        assert GetBetter


q1 = {0, 1, 2, 3, 4, 5, 6}
q2 = {1, 2, 3, 4, 5, 6}


def mult(a, b):
    return a * b % 7


print(is_group(q1, mult))
print(is_group(q2, mult))
