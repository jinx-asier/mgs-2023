#mess around
def gold_rat(x,n):
    if n == 0:
        return(x)
    else:
        print(1 /(1 + gold_rat(x, n - 1)))
        return(gold_rat(x, n - 1))

gold_rat(int(input("""
x value here
>>>""")), int(input("""
n value here>>>""")))
