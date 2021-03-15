from Graphs import Graph

def main():
    graph = Graph()

    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.AddVertex(3)
    graph.AddVertex(4)

    graph.addEdges(1,2)
    graph.addEdges(1,3)

    graph.addEdges(2,4)

    graph.addEdges(3,2)
    graph.addEdges(3,1)
    graph.addEdges(4,1)
    graph.addEdges(4,3)

    graph.showAllConnection()
if __name__ == '__main__':
    main()
