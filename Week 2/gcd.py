a,b = [int(i) for i in input().split()]
def gcd(a,b):
	if b==0:
		print(a)
		quit()
	c = a%b
	gcd(b,c)
if a>b:
	gcd(a,b)
else:
	gcd(b,a)