class Node:
    def __init__(self, val: int, next = None):
        self. val = val
        self.next = next
    
def get_tail(head: Node):
    curr = head
    while curr.next:
        curr = curr.next
    
    # print("Head is still: ", head.val)
    return curr

def ll_replace(head, original, replacement):
    curr = head
    while curr:
        if curr.val == original:
            curr.val = replacement

        curr = curr.next

def ll_print(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.val, "--> ", end="")
        else:
            print(curr.val)
        curr = curr.next
    

node1, node2, node3 = Node(1), Node(2), Node(3)
node1.next = node2
node2.next = node3
print(get_tail(node1).val)
ll_print(node1)

ll_replace(node1, 2, 80)
ll_print(node1)

ll_replace(node1, 3, 80)
ll_print(node1)

ll_replace(node1, 80, 5)
ll_print(node1)

