# Uses python3
import sys
import math

def get_change(m):
    counter = 0
    
    while (m >= 10):
        counter += 1
        m -= 10

    while (m >= 5):
        counter += 1
        m -= 5

    while (m >= 1):
        counter += 1
        m -= 1

    return (counter)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
