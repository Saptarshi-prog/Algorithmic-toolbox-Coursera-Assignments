a, b = [int(i) for i in input().split()]

def gcd(a,b):
	if b==0:
		return a
	c = a%b
	return gcd(b,c)

if a>b:
	gcd1 = gcd(a,b)
else:
	gcd1 = gcd(b,a)

ans = int(a*b)//int(gcd1)
print(ans)
