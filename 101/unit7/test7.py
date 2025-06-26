#Problem 1
# def repeat_hello_iterative(n: int):
#     """"
#     loop n times printing hello
#     """
#     for i in range(n):
#         print("hello")


# repeat_hello_iterative(3)

"""
Given the base case and recursive case, write a function factorial() that returns the factorial of a non-negative integer n. The factorial of a number is the product of all numbers between 1 and n.

Base Case: The smallest number we can find a factorial of is 0. By definition, the factorial of 0 is 1.

Recursive Case: We can restate the problem to say that the factorial of n is n * the factorial of n-1.


sample:
def repeat_hello(n):
	if n > 0:
        
		repeat_hello(n - 1)
		
n=5
return => 5 * 4 * 3 * 2 * 1
"""
#Problem 2
# #Recursively find product between 1 and n
# n = 3
# def factorial(n):
# 	# Base case
# 	if n <= 1:
# 		return 1
	
# 	fact = n * factorial(n-1) # O(1)
# 	return fact

# print(factorial(5))

"""
Without using the built-in sum() function, write a function sum_list() that calculates the sum of all values in a list recursively.

What is the time complexity of this function? What is the space complexity?

"""
def get_sum(lst, iterator):
    # base case
    if iterator < len(lst):
        pass
    


def sum_list(lst):
    pass



