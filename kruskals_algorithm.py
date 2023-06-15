# O(e * log(e)) time | O(e + v) space - where e is the number
# of edges in the input edges and v is the number of vertices
def kruskalsAlgorithm(edges):
    # Write your code here.
    edgeList = []
    for sourceIndex, vertex in enumerate(edges):
        for edge in vertex:
            if edge[0] > sourceIndex:
                edgeList.append([sourceIndex, edge[0], edge[1]])
    sortedEdges = sorted(edgeList, key=lambda edge: edge[2])

    parents = [vertex for vertex in range(len(edges))]
    ranks = [0 for _ in range(len(edges))]
    mst = [[] for _ in range(len(edges))]
    for edge in sortedEdges:
        vertex1Root = find(edge[0], parents)
        vertex2Root = find(edge[1], parents)
        if vertex1Root != vertex2Root:
            mst[edge[0]].append([edge[1], edge[2]])
            mst[edge[1]].append([edge[0], edge[2]])
            union(vertex1Root, vertex2Root, parents, ranks)

    return mst


def find(vertex, parents):
    if vertex != parents[vertex]:
        parents[vertex] = find(parents[vertex], parents)

    return parents[vertex]


def union(vertex1Root, vertex2Root, parents, ranks):
    if ranks[vertex1Root] < ranks[vertex2Root]:
        parents[vertex1Root] = vertex2Root
    elif ranks[vertex1Root] > ranks[vertex2Root]:
        parents[vertex2Root] = vertex1Root
    else:
        parents[vertex2Root] = vertex1Root
        ranks[vertex1Root] += 1
