# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result1 = 0
result2 = 0
	
for i in a:
	if i > result1:
		result1 = i

s = []
for i in a:
	s.append(i)
for i in s:
	if i == result1:
		s.remove(i)
		break

for i in s:
	if i > result2:
		result2 = i
print (result1 * result2)