# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y) # x raised to the power of y
    v = math.factorial(v) # that result factorialed
    v //= (x + y) # floor division of result / x + y
    v %= 982451653 # remainder of result and 982451653

    return v

# sample output:
# 0: 9,4: 738371044
# 1: 5,5: 917230692
# 2: 13,5: 381057234
# 3: 8,4: 211470843
# 4: 9,3: 412684903
# 5: 10,4: 226457743
# etc...

cache = {}

# check for x, y pair if used, pull from cache rather than calculating
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    key = f"({x}, {y})"

    if key not in cache:
        v = math.pow(x, y) # x raised to the power of y
        v = math.factorial(v) # that result factorialed
        v //= (x + y) # floor division of result / x + y
        v %= 982451653 # remainder of result and 982451653
        cache[key] = v

    return cache[key]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

    # prints the iteration it's on
    # followed by a x and y, which are random numbers between the specified ranges
    # 
