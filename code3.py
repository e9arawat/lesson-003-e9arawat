# code 
def func(l1):
    ans = [i if i>=0 else i*-1 for i in l1]
    return ans

l1 = [-2, 13, -5, 0, 1, 2]
print(func(l1))