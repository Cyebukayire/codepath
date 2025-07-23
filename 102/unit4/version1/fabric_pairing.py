"""
n: number of fabrics
s: average size of the input frabic name

Space complexity: O(n*s) ==> O(n) comes from extra memory by the inplace sorting method, in addition to that 
the output size is depending on the string length, which is length of fabric names, this is changing with input, so 
length of fabric names significantly affects the space cost. We didn't coniser the size of output list, which is 2, because
this is a constant
"""

def find_best_fabric_pair(fabrics, budget):
    if not fabrics: return ()

    # Sort fabrics by cost
    fabrics.sort(key=lambda x: x[1]) # O(NlogN) time complexity and O(N) space complexity for the auxillary extra memory cost

    l = 0
    r = len(fabrics)-1

    while l+1 < r and fabrics[l][1] + fabrics[r][1] != budget: # O(N)
        cost = fabrics[l][1] + fabrics[r][1]
        if cost < budget:
            l += 1
        elif cost > budget:
            r -= 1
        # else:
        #     print("\n\n.....REACHED HERE......\n\n")
        #     return (fabrics[l][0], fabrics[r][0])

    cost = fabrics[l][1] + fabrics[r][1]
    return () if cost > budget else (fabrics[l][0], fabrics[r][0]) 

fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))



