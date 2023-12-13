def func(li):
    ans = {i:len(i) for i in li if len(i) > 4}
    return ans

li = ['fruit', 'car', 'board']
print(func(li))