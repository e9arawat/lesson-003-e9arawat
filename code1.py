# Code to print first 10 multiples of a number using LIST compre.
def func(n):

    """ ans = []
    for i in range(1,11):
        ans.append(n * i) """

    ans = [n*i for i in range(1,11)]
    return ans

print(func(int(input("Enter a value: "))))