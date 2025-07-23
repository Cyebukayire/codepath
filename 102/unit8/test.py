# Ignoring unused data in a loop
# for _ in range(10):
#     print(_, "test")

# 1. Unpacking function returns, 2. Using known keyword names as varialble or object names
# def testing():
#     return ["name", 23, "call", 2]

# str_, num1, _, _= testing()
# print(str_, num1, _)

"""
return 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 = 5
5: return fib(4): fib(3): fib(2): fib(1) + fib(0) + fib(1) + fib(2):fib(1) + fib(0) + fib(3):fib(2): fib(1) + fib(0) + fib(1)
14

4: return fib(3): fib(2): fib(1)+fib(0) + fib(1) +fib(2):fib(1)+fib(0)
8

3: return fib(2): fib(1) + fib(0) +fib(1)
4

2: return fib(1) + fib (0)
2

1: return 1
0

0: return 0
0
"""
def fib(n):
    # print(n)
    if n <=1:
        return n
    
    return fib(n-1) + fib(n-2)

print("Result: ", fib(10))

"""
3, 2, return 5, 0
"""

def fib_count(n, count=0):
    count+=1
    if n <= 1:
        return n, count
    
    fib(n-1)
    fib(n-2)
    return fib(n), count

print("Count Result: ", fib_count(5))


def fib_tree(n, indent=""):
    print(f"{indent}fib({n})")
    if n <= 1:
        return n
    left = fib_tree(n-1, indent + "  ")
    right = fib_tree(n-2, indent + "  ")
    return left + right

fib_tree(6)

def fib_memoization(n, memo={}):
    """
    memo = {
    }

    5: 3 + 2 = 5
    memo[4] = fib_memoizatoin(3) + fib_memoizatoin(2) = 2 + 1 = 3
    memo[3] = fib_memoizatoin(2) + fib_memoizatoin(1) = 1 + 1 = 2
    memo[2] = fib_memoizatoin(1) + fib_memoizatoin(0) = 1 + 0 = 1
    memo[1] = 1
    memo[0] = 0
    
    """
    if n <= 1:
        return n
    
    # if n-1 not in memo:
    memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
    # if n-2 not in memo:
        # memo[n-2] = fib_memoization(n-3, memo) + fib_memoization(n-4, memo)
        # memo[n-2] = fib_memoization(n-2, memo)
    print(memo)
    return memo[n]

print("Fib Memo Result: ", fib_memoization(10))