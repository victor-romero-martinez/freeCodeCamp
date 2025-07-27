def fiboEvenSum(n: int) -> int:
    a, b = 1, 2
    sum = 0

    while b <= n:
        if b % 2 == 0:
            sum += b
            
        a, b = b, a + b

    return sum
#end

print(fiboEvenSum(10)) # 10
print(fiboEvenSum(60)) # 44
print(fiboEvenSum(1000)) # 798