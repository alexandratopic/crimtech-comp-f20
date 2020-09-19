#1. Write a function that returns the square root 
# of a given variable `n`. If `n` is negative or not 
#a number, returns `-1`. Put your code in 
#`square_root.py`
import math

def square_root(n):
    if isinstance(n, int) and n >= 0:
        return math.sqrt(n)
    else:
        return -1

def test():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root("hello") == -1
    assert square_root(-10) == -1
    print("Success!")

if __name__ == "__main__":
    test()