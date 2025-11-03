"""
You are given the head of two linked lists, playlist1 and playlist2 with lengths n and m respectively. Remove playlist1's nodes from the ath to the bth node and put playlist2 in its place. Assume the lists are 0-indexed.

The blue edges and nodes in the figure below indicate the result:

Merged playlists

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
    """
    # a = 2, b= 4
    0    x    a                        b y
    0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0


        x.next = playlist2
        playlist2.next = y
    # find x and y
    x // node before a
    y // node after b
    curr_node = playlist1
    while curr_node.next:
        if i = a-1:
            x =curr_node
        if i == b:
            y = curr_node.next # Good move
            break
        curr_node = curr_node.next
# 
    #while curr_node.next:
        
    
    temp_playlist2 = playlist2
    while temp_playlist2.next is not None: 
        temp_playlist2.next

    x.next = playlist2
    temp_playlist2.next = y    

    return playlist1
    """
    i = 0
    curr_node = playlist1
    while curr_node.next:
        if i == a-1:
            x =curr_node
        if i == b+1:
            y = curr_node
            break
        curr_node = curr_node.next
        # print(i)
        i += 1
    
    temp_playlist2 = playlist2
    while temp_playlist2.next: 
        temp_playlist2 = temp_playlist2.next

    x.next = playlist2
    temp_playlist2.next = y    

    return playlist1
    


playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))
