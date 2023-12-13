# import math
def func(n):
    #ans = {i:True if math.sqrt(i) == int(math.sqrt(i)) else False for i in range(n+1)}
    ans = {i:True if i ** (0.5) == int(i ** (0.5)) else False for i in range(n+1)}

    return ans

print(func(int(input("Enter a number: "))))