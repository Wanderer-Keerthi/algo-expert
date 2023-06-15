# O(v + e) time | O(v) space - where v is the number of
# vertices and e is the number of edges in the graph
def twoColorable(edges):
    # Write your code here.
    colors = [None for _ in edges]
    colors[0] = True
    stack = [0]

    while len(stack) > 0:
        node = stack.pop()
        for connection in edges[node]:
            if colors[connection] is None:
                colors[connection] = not colors[node]
                stack.append(connection)
            elif colors[connection] == colors[node]:
                return False
                
    return True
