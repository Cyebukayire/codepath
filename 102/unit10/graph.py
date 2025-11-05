class GraphNode:
    def __init__(self,val,edges=[]):
        self.val = val
        self.edges = edges
    def add_connection(self, newGraphNode):
        self.edges.append(newGraphNode)

edges = [
    [0,1],
    [1,2],
    [2,3]
]

