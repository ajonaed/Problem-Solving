class Graph:

    def __init__(self):
        self.numberVertices = 0
        self.vertices = {}

    def AddVertex(self,node):
        self.vertices[node] = []
        self.numberVertices += 1

    def addEdges(self,node,link):
        self.vertices[node].append(link)

    def showConnection(self,node):
        for i in self.vertices[node]:
            print(self.vertices[node],' ---> ',i )

    def showAllConnection(self):
        for v in self.vertices.keys():
            for link in self.vertices[v]:
                print(v,' ---> ',link )
            print()
