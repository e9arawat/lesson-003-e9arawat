"""def func(li):
    ans = [i for x in li for i in range(x)]
    return ans
li = [1,2,3]
print(func(li))"""


def func(li):
    ans = [i for x in li for i in x]
    return ans

li = [[1,2], [3,16], [8,9]]
print(func(li))