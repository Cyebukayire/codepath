class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def printl(l):
    res = []
    while l:
        res.append(l.data)
        l = l.next
    print(res)

def weave(A,B):
    if not A:
        return B
    if not B:
        return A
    curr_A = A
    curr_B = B
    next_A = A.next
    next_B = B.next

    curr_A.next = curr_B
    curr_A.next.next = next_A

    weave(next_A, next_B)

    return A


def weave_rec(A,B):
    if not A:
        return B
    if not B:
        return A

    A.next = weave(B, A.next)

    return A

A = Node('A1',Node('A2', Node('A3', Node('A4'))))
B = Node('B1',Node('B2', Node('B3', Node('B4'))))
# A = Node('A1',Node('A2'))
# B = Node('B1',Node('B2',Node('B3', Node('B4'))))
# printl(A)
# printl(B)
# printl(weave(A,B))
printl(weave_rec(A,B))



