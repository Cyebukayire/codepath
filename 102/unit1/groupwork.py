"""
Problem 6: Merge Intervals
You are given an array of intervals, where each interval is represented as [start, end].

Write a function merge_intervals(intervals) that merges all overlapping intervals and returns a new array of the merged, non-overlapping intervals.

def merge_intervals(intervals):
	pass
Example Usage

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)
Example Output:

[[1, 6], [8, 10], [15, 18]]
[[1, 5]]


[[1, 5], [2, 4], [15, 18]]

result array hold intervals at index 0

for start, end in range(1, len(intervals)):
    store end of the last interval in the result array 
	store the last end interval in the result array [-1][1]
    
    choose to merge if overlapping or append new interval
    
 return result
	
"""

# sort intervals by start time

def merge_intervals(intervals):
    if not intervals or len(intervals) <= 0:
        return []
    elif len(intervals) == 1:
        return intervals[0]
        
    intervals.sort()  
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        result_end = result[-1][1]
        
        if intervals[i][0] <= result_end:
             result[-1][1] = max(result_end, intervals[i][1])
        else:
            result.append(intervals[i])
            
    return result
            

intervals = [[1, 5], [2, 4], [15, 18]]
print(merge_intervals(intervals))