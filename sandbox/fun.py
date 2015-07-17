__author__ = 'John'
"""
Test module
"""

def fib(n):
    if n > 0:
        a, b = 0, 1
        i = 0
        while i < n:
            i += 1
            a, b = b, a+b
    return b


if __name__  == "__main__":
    print(fib(8))
