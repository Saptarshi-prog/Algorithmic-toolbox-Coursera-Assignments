n = int(input())
lesser_n = n%60
lesser_nplus = (n+1)%60

def fibonacci(n):
    a, b = 0, 1
    for _ in range(2, n+1):
        c = a+b
        c = c% 10
        b, a = c, b
    return c

if lesser_n<=1:
    a = lesser_n
else:
    a = fibonacci(lesser_n)
if lesser_nplus<=1:
    b = lesser_nplus
else:
    b = fibonacci(lesser_nplus)

 
ans = (a*b)%10
print(ans)
