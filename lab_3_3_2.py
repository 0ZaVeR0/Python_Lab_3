def hofstadter_q(x: int) -> int:

    def rec(n: int) -> int:
        if n == 1 or n == 2:
            Q = 1
        if n > 2:
            Q =  rec(n - rec(n - 1)) + rec(n - rec(n - 2))
        return Q
    
    for n in range(1,x + 1):
        yield rec(n)

def main():
    n = int(input())
    for x in hofstadter_q(n):
        print (x)

if __name__ == "__main__":
    main()
