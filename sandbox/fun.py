__author__ = 'John'
"""
Test module
"""

def fib(n):
    a = 0
    if n > 0:
        b = 1
        i = 0
        while i < n:
            i += 1
            a, b = b, a+b
    return b


if __name__  == "__main__":
    print(fib(6))
