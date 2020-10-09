t = int(input())
for i in range(t):
	a = [int(i) for i in input().split(" ")]
	val = (a[0] - a[2] + a[3])%a[1]
	
	if val:
		print("NO")
	else:
		print("YES")
