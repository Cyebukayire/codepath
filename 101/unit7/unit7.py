"""
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. 
For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. 
However, "abA" is not because 'b' appears, but 'B' does not.

Using the divide and conquer approach, write a function longest_nice_substring() that takes in a string s and returns the longest substring of s that is nice. 
If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.


"""

""""
Approach 1: nlogn (?)
s = YazaAay

     [Yaza]         [Aay]
   [Ya]    [za]   [Aa]  [y]
[Y] [a] [z] [a] [A] [a] [y] --> all these return ""

Start at the base case: substrings of length 1
Base case:
if (len(s) == 1):
	return 0 # length of the longest "nice" substring

# three cases when combining two substrings:
	# longest nice substring is in the left one
	# longest nice substring is the right one
	# longest nice substring is found among both
# let's say we are combining two substrings: [A] and [a]
Individually, they returned 0
But, [A] and [a] are nice when combined --> [Aa] returns 2




Brute Force: O(n^3)
- Find all possible substrings O(n^2)
- Check which ones are nice --> this is O(n) for each substring
- Select the longest such substring
- In the case of ties, choose the one that starts at the earlier index

"""

# O(n^2)
def longest_nice_substring(s):
	if len(s) < 2:
		return ""

	charset = set(s) # convert string into set
	for i, c in enumerate(s): # same as using i in range and c = s[i]
		if c.lower() in charset and c.upper() in charset:
			continue 
		# Split at the "bad" character
		left = longest_nice_substring(s[:i])
		right = longest_nice_substring(s[i+1:])
		return left if len(left) >= len(right) else right

	return s

# print(set("YazaAaa"))

# print(longest_nice_substring("YazAaa"))
"""""""""
lns("YazaAaa")
charset = Y, a, z, A
for char in "YazaAaa":

is y and Y in charset? no. go to recursion
left = lns("") --> returns ""

right = lns("azaAaa")
charset = "a, z, A"
is a and A in charset? yes. continue
is z and Z in charset? no. go to recursion
left = lns("a") --> returns ""
right = lns("aAaa")
"""""""""

# Given a sorted(!) list of integers containing duplicates, 
# write a function find_frequencies() that finds each element’s frequency in less than O(n) time.

"""
dict [item: frequ]
m
if lst[mid] in dict:
	dict[lst[mid]] += 1
else:
	dict[lst[mid]] = 1


l = lst[:m]
r = lst[m + 1:]

l = [2, 2, 2, 4, 4, 4]
r = [5, 6, 8, 8, 9]
return dict + find_frequencies(l) + find_frequencies(r)


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1.update(dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}


dict1.keys = {a, b}. dict2.keys = {b, c}. 
{a, b} | {b, c} = {a, b, c} union operator kinda?
# helper for merging two dictionaries

"""
def merge_dicts(dict1, dict2): # O(n)
	merged_dict = {}
	for key in dict1.keys() | dict2.keys():
		merged_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)
		
	return merged_dict


# this is supposed to be done less than O(n)... but GPT says that's not even possible

# this implementation might be ~O(nlogn). 
def find_frequencies(lst):
	dict = {}
	if not lst:
		return dict

	mid = (len(lst) - 1) // 2
	if lst[mid] in dict:
		dict[lst[mid]] += 1
	else:
		dict[lst[mid]] = 1
	left_dict = find_frequencies(lst[:mid])
	right_dict = find_frequencies(lst[(mid + 1):])

	left_plus_right = merge_dicts(left_dict, right_dict) # by itself is O(n)
		
	return merge_dicts(merge_dicts(left_dict, right_dict), dict)

#        L                  M              R
input = [2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]
# Expected Output: {2: 3, 4: 3, 5: 2, 6: 1, 8: 2, 9: 1}
print(find_frequencies(input))


