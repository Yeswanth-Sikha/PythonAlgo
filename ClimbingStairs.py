def climbStairs(n: int) -> int:
    a, b = 1, 2
    if(n == 1):
        return 1
    elif(n == 2):
        return 2
    else:
        for i in range(n-2):
            c = a + b
            a = b
            b = c
    return c


if __name__ == '__main__':
    n = int(input())
    print(climbStairs(n))
