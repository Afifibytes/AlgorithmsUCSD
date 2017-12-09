# Uses python3
import random

def main():
	while(True):
		n = int(random.getrandbits(8))
		print(n)
		a = [int(random.getrandbits(40)) for x in range(n)]
		for i in a:
			print("{} ".format(i), end="")
		print()
		assert(len(a) == n)
		res1 = max_pairwise1(a)
		res2 = max_pairwise2(a, n)
		if not res1 == res2:
			print("wrong answer: res1: {}  res2: {}".format(res1, res2))
			break
		else:
			print("OK")


def max_pairwise1(a):
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
	return result1 * result2


def max_pairwise2(a, n):
	result = 0
	for i in range(0, n):
		for j in range(i+1, n):
			if a[i]*a[j] > result:
				result = a[i]*a[j]
	return result

if __name__ == '__main__':
	main()
