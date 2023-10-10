import math

def koef(n):
    c = []
    for i in range (n + 1):
        c.append(int(math.factorial(n) / (math.factorial(n - i) * math.factorial(i))))
    print(c)
    return (c)


def binom(power):
    negative = False
    if power == 0:
        return 1
    elif power < 0:
        power = -power
        negative = True
    c = koef(power)
    ans = []
    a = str()
    b = str()
    for i in range(power + 1):

        a = "a" if power - i == 1 else "a^" + str(power - i) if power - i != 0 else str()
        b = "b" if i == 1 else "b^" + str(i) if i != 0 else str()

        ans.append((str(c[i]) if c[i] != 1 else "") + a + b)
    
    ans2  = ans[0]
    for i in range(len(ans)-1):
        ans2 += " + " + ans[i+1] 
    ans2  = ("1/(" + ans2 + ")" if negative else ans2)
    return ans2

n = int(input())
print(binom(n))
