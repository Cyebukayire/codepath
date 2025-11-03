print([2]+[90])
nums = [1,2,3,4,5]
s = 0
prefixsum = [0] + [(s := s + x) for x in nums]
print(prefixsum)
