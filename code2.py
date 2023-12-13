# Code to find all the positive/non-negative integers in a list using LIST comp.

def func(l1):
    ans = [i for i in l1 if i>=0]
    return ans

l1 = [-2, 13, -5, 0, 1, 2]
print(func(l1))