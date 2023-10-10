def hofstadter_q(x):
    ans = (rec(n) for n in range (1,x + 1))
    return ans

def rec(n):
    if n == 1 or n == 2:
        Q = 1
    if n > 2:
        Q =  rec(n - rec(n - 1)) + rec(n - rec(n - 2))
    return Q

n = int(input())
for x in hofstadter_q(n):
    print (x)