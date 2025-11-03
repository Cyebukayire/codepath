"""

class KthLargest:
    def __init__ (self, k, nums = []):
        self.k = k
        self.nums = nums

    def add(self, val):
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.nums.sort()
        elif val > self.nums[0]:
            self.nums[0] = val
            self.nums.sort()
        print(self.nums)
        return self.nums[0]

obj = KthLargest(3)
print(obj.add(8))
print(obj.add(3))
print(obj.add(8))
print(obj.add(18))
print(obj.add(5))
print(obj.add(9))

"""

"""
# USING THE BISECT Module
import bisect
class KthLargest:
    def __init__ (self, k, nums = []):
        self.k = k
        if nums:
            nums.sort()
        self.nums = nums

    def add(self, val):
        if len(self.nums) < self.k:
            bisect.insort(self.nums, val)
        elif val > self.nums[0]:
            self.nums.remove(self.nums[0]) # O(k)
            bisect.insort(self.nums, val) # O(k)
        print(self.nums)
        return self.nums[0]

obj = KthLargest(3)
print(obj.add(8))
print(obj.add(3))
print(obj.add(8))
print(obj.add(18))
print(obj.add(5))
print(obj.add(9))
"""

# USING HEAPQ Module
import heapq
min_heap = [23,4,0, 3, 1]
heapq.heapify(min_heap)
print(heapq.nlargest(3, min_heap))