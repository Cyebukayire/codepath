"""
Problem 1: Graphing Flights
The following graph represents the different flights offered by CodePath Airlines. Each node or vertex represents an airport (JFK - New York City, LAX - Los Angeles, DFW - Dallas Fort Worth, and ATL - Atlanta), and an edge between two vertices indicates that CodePath airlines offers flights between those two airports.

Create a variable flights that represents the undirected graph below as an adjacency dictionary, where each node's value is represented by a string with the airport's name (ex. "JFK").
"""

"""
U : i: none
    o: adjacency dictionary
    c
    e: nothing input


P 
"""

"""
JFK ----- LAX
|
|
DFW ----- ATL
"""

flights = {
    
    "JFK": ["LAX", "DFW"],
    "LAX": ["JFK"],
    "DFW": ["ATL","JFK" ],
    "ATL":["DFW"] 
}

# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])


"""
U:  I: adj matrix
    o: boolean -> true when there is a flight from i to j and j to i for all airports in the graph
    c: n/a
    e: empty graph
        only one airport ? true
        
        
flights1 = [[1, 2], [0], [0, 3], [2]]

flights1 = {0:[1, 2], 
            1:[0], 
            2:[0, 3], 
            3:[2]}

runtime = O(vertcies * edges)

P:
    done = set() # O(n^2)
    for airport, destinations in enumerate(flights):
        for a in destinations:
            if a in done:
                continue
            
            if airport not flights[a]:
                return False
        done.add(airport)
    
    return True 
"""

def bidirectional_flights(flights):
    len_range = len(flights)
    for i in range(len_range):
        for airport in flights[i]: # [1, 2]
            if i not in flights[airport]:
                return False
    return True

# Thanks Sneha!
    
    # done = set() # O(V.E)
    # for airport, destinations in enumerate(flights):
    #     for a in destinations:
    #         if a in done:
    #             continue
            
    #         if airport not in flights[a]:
    #             return False
    #     done.add(airport)
    
    # return True 


            # 0      1    2     3
flights1 = [[1, 2], [0], [0, 3], [2]] # [1, 2] => [2, 1]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))


