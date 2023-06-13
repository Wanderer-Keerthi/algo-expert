# Average case: when the tree is balanced
# O(n) time | O(h) space - where n is the number of nodes in
# the Binary Tree and h is the height of the Binary Tree
def allKindsOfNodeDepths(root, depth=0):
    # Write your code here.
    if root is None:
        return 0

    # Formula to calculate 1 + 2 + 3 + ... + depth - 1 + depth
    depthSum = (depth * (depth + 1)) / 2
    return (
        depthSum
        + allKindsOfNodeDepths(root.left, depth + 1) 
        + allKindsOfNodeDepths(root.right, depth + 1) 
    )


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# Solution 2
# Average case: when the tree is balanced
# O(n) time | O(h) space - where n is the number of nodes in
# the Binary Tree and h is the height of the Binary Tree
# def allKindsOfNodeDepths(root, depthSum=0, depth=0):
#     # Write your code here.
#     if root is None:
#         return 0

#     depthSum += depth
#     return (
#         depthSum
#         + allKindsOfNodeDepths(root.left, depthSum, depth + 1) 
#         + allKindsOfNodeDepths(root.right, depthSum, depth + 1) 
#     )


# # This is the class of the input binary tree.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None



# Solution 3
# Average case: when the tree is balanced
# O(n) time | O(h) space - where n is the number of nodes in
# the Binary Tree and h is the height of the Binary Tree
# def allKindsOfNodeDepths(root):
#     # Write your code here.
#     return getTreeInfo(root).sumOfAllDepths


# def getTreeInfo(tree):
#     if tree is None:
#         return TreeInfo(0, 0, 0)

#     leftTreeInfo = getTreeInfo(tree.left)
#     rightTreeInfo = getTreeInfo(tree.right)

#     sumOfLeftDepths = leftTreeInfo.sumOfDepths + leftTreeInfo.numNodesInTree
#     sumOfRightDepths = rightTreeInfo.sumOfDepths + rightTreeInfo.numNodesInTree

#     numNodesInTree = 1 + leftTreeInfo.numNodesInTree + rightTreeInfo.numNodesInTree
#     sumOfDepths = sumOfLeftDepths + sumOfRightDepths
#     sumOfAllDepths = sumOfDepths + leftTreeInfo.sumOfAllDepths + rightTreeInfo.sumOfAllDepths

#     return TreeInfo(numNodesInTree, sumOfDepths, sumOfAllDepths)


# class TreeInfo:
#     def __init__(self, numNodesInTree, sumOfDepths, sumOfAllDepths):
#         self.numNodesInTree = numNodesInTree
#         self.sumOfDepths = sumOfDepths
#         self.sumOfAllDepths = sumOfAllDepths

        
# # This is the class of the input binary tree.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None



# Solution 4
# Average case: when the tree is balanced
# O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
# def allKindsOfNodeDepths(root):
#     # Write your code here.
#     nodeCounts = {}
#     addNodeCounts(root, nodeCounts)
#     nodeDepths = {}
#     addNodeDepths(root, nodeDepths, nodeCounts)
#     return sumAllNodeDepths(root, nodeDepths)


# def sumAllNodeDepths(node, nodeDepths):
#     if node is None:
#         return 0
#     return sumAllNodeDepths(node.left, nodeDepths) + sumAllNodeDepths(node.right, nodeDepths) + nodeDepths[node]


# def addNodeDepths(node, nodeDepths, nodeCounts):
#     nodeDepths[node] = 0
#     if node.left is not None:
#         addNodeDepths(node.left, nodeDepths, nodeCounts)
#         nodeDepths[node] += nodeDepths[node.left] + nodeCounts[node.left]
#     if node.right is not None:
#         addNodeDepths(node.right, nodeDepths, nodeCounts)
#         nodeDepths[node] += nodeDepths[node.right] + nodeCounts[node.right]


# def addNodeCounts(node, nodeCounts):
#     nodeCounts[node] = 1
#     if node.left is not None:
#         addNodeCounts(node.left, nodeCounts)
#         nodeCounts[node] += nodeCounts[node.left]
#     if node.right is not None:
#         addNodeCounts(node.right, nodeCounts)
#         nodeCounts[node] += nodeCounts[node.right]


# # This is the class of the input binary tree.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None



# Solution 5
# Average case: when the tree is balanced
# O(nlog(n)) time | O(h) space - where n is the number of nodes in
# the Binary Tree and h is the height of the Binary Tree
# def allKindsOfNodeDepths(root):
#     # Write your code here.
#     if root is None:
#         return 0
#     return allKindsOfNodeDepths(root.left) + allKindsOfNodeDepths(root.right) + nodeDepths(root)


# def nodeDepths(node, depth=0):
#     if node is None:
#         return 0
#     return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)
    

# # This is the class of the input binary tree.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None



# Solution 6
# Average case: when the tree is balanced
# O(nlog(n)) time | O(h) space - where n is the number of nodes in
# the Binary Tree and h is the height of the Binary Tree
# def allKindsOfNodeDepths(root):
#     # Write your code here.
#     sumOfAllDepths = 0
#     stack = [root]
#     while len(stack) > 0:
#         node = stack.pop()
#         if node is None:
#             continue
#         sumOfAllDepths += nodeDepths(node)
#         stack.append(node.left)
#         stack.append(node.right)
#     return sumOfAllDepths


# def nodeDepths(node, depth=0):
#     if node is None:
#         return 0
#     return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)
    

# # This is the class of the input binary tree.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
