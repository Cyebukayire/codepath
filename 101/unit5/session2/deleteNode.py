class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def printNode(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.val, ' -> ', end='')
        else:
            print(curr.val)
        curr = curr.next

        
    
def delete1Node(head: Node, val: int):
    """
    A method to delete a node with a given value
    """
    if not head:
        return None
    temp_head = Node("temp")
    temp_head.next = head

    prev = temp_head
    curr = head
    while curr:
        if curr.val == val:
            prev.next = curr.next
            break

        prev = curr
        curr = curr.next

    return temp_head.next

def deleteAllNode(head: Node, val: int):
    temp_head = Node(-1)
    temp_head.next = head

    prev = temp_head
    curr = head
    while curr:
        if curr.val == val:
            prev.next = curr.next
            
        else:
            prev.next = curr
            prev = curr
        
        curr = curr.next

    return temp_head.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4

printNode(node1)
printNode(delete1Node(node1, 1))
printNode(node1)
printNode(deleteAllNode(node1, 1))






            


