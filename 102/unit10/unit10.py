collaborations = {
    "Chadwick Boseman": [("Lupita Nyong'o", 2), ("Robert Downey Jr.", 3), ("Mark Ruffalo", 2)],
    "Lupita Nyong'o":[("Chadwick Boseman",2), ("Mark Ruffalo", 1)],
    "Robert Downey Jr.":[("Chadwick Boseman",3), ("Mark Ruffalo", 5)],
    "Mark Ruffalo":[("Lupita Nyong'o", 1), ("Robert Downey Jr.", 5), ("Chadwick Boseman", 2), ("Rosario Dawson", 2)],
    "Rosario Dawson":[("Mark Ruffalo", 2)]
    }

# print(collaborations["Chadwick Boseman"])

"""
U
    i: adj list 
    o: two list one with cast and other with crew
    c: n/a
    e: list is empty 

    
P
    - Initialize an empty list of visited nodes
    - Initialize an empty queue 
    - Add the node we would like to start our traversal from to the queue 
    - Add the node we would like to start our traversal from to visited
    - While the queue is not empty:
        - Remove an element from the queue and store it in a variable, `current`
        - Loop through each of the current node's neighbors:
            - If the neighbor has not yet been visited:
                - Add the neighbor to the queue
                - Add the neighbor to the list of visited nodes
    - Return the list of visited nodes
"""

from collections import deque

def get_groups(cast_and_crew):
    l1 = []
    
    visited = set()
    
    queue = deque(next(iter(cast_and_crew.keys()))) # think this should fix it :)
    
    while queue:
        key = queue.popleft()
        
        if key in visited:
            continue
            
        l1.append(key)
        values = cast_and_crew[key]
        
        for v in values:
            if v not in visited:
                queue.append(v)
                l1.append(key)
    
        visited.add(key)
    
    
    l2= [i for i in cast_and_crew.keys() if i not in visited]
        
    
    return l1 , l2
    
    
    




get_out_movie = {
    "Daniel Kaluuya": ["Allison Williams"],
    "Allison Williams": ["Daniel Kaluuya", "Catherine Keener", "Bradley Whitford"],
    "Bradley Whitford": ["Allison Williams", "Catherine Keener"],
    "Catherine Keener": ["Allison Williams", "Bradley Whitford"],
    "Jordan Peele": ["Jason Blum", "Gregory Plotkin", "Toby Oliver"],
    "Toby Oliver": ["Jordan Peele", "Gregory Plotkin"],
    "Gregory Plotkin": ["Jason Blum", "Toby Oliver", "Jordan Peele"],
    "Jason Blum": ["Jordan Peele", "Gregory Plotkin"]
}

print(get_groups(get_out_movie))