""""
1 -> 2 -> 3 -> 4
      \ _  _  _/  
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
     if not head or not head.next:
         return False
     
     p1 = head
     p2 = head

     while p2.next:
         p1 = p1.next
         p2 = p2.next.next

         if p1 == p2:
             return True
         
     return False
 

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node1
# node3.next = None
print(is_circular(node1))
