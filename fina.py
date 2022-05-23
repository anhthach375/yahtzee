def fun1(x:int, y:int) -> int:
    if y == 0:
        return 1
    else:
        return x*fun1(x,y-1)

def fun2(n:int) -> int:
    if n < 1:
        return -1
    elif n == 1:
        return 0
    else:
        return 1 + fun2(n//2)

def main():
    print(fun1(2,3))
    print(fun1(3,2))
    print(fun2(1))
    print(fun2(2))
    print(fun2(8))

main()