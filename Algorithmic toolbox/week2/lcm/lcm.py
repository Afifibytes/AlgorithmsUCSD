# Uses python3
import sys

def lcm(a, b):
    x = a * b
    y = gcd(a, b)
    return int(x // y)

def gcd(a, b):
    if b == 0:
        return a
    else:
        s = a % b
        return gcd(b, s)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

