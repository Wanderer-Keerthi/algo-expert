# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
class UnionFind:
    def __init__(self):
        # Write your code here
        self.parents = {}
        self.ranks = {}

    # O(α(n)), approximately O(1) time | O(α(n)), approximately O(1) space - where n is the total number of values
    def createSet(self, value):
        # Write your code here
        self.parents[value] = value
        self.ranks[value] = 0

    # O(α(n)), approximately O(1) time | O(α(n)), approximately O(1) space - where n is the total number of values
    def find(self, value):
        # Write your code here
        if value not in self.parents:
            return None

        if value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])

        return self.parents[value]

    # O(α(n)), approximately O(1) time | O(α(n)), approximately O(1) space - where n is the total number of values
    def union(self, valueOne, valueTwo):
        # Write your code here
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)
        if self.ranks[valueOneRoot] < self.ranks[valueTwoRoot]:
            self.parents[valueOneRoot] = valueTwoRoot
        elif self.ranks[valueOneRoot] > self.ranks[valueTwoRoot]:
            self.parents[valueTwoRoot] = valueOneRoot
        else:
            self.parents[valueTwoRoot] = valueOneRoot
            self.ranks[valueOneRoot] += 1



# Solution 2
# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
# class UnionFind:
#     def __init__(self):
#         # Write your code here
#         self.parents = {}
#         self.ranks = {}

#     # O(1) time | O(1) space
#     def createSet(self, value):
#         # Write your code here
#         self.parents[value] = value
#         self.ranks[value] = 0

#     # O(log(n)) time | O(1) space - where n is the total number of values
#     def find(self, value):
#         # Write your code here
#         if value not in self.parents:
#             return None

#         currentParent = value
#         while currentParent != self.parents[currentParent]:
#             currentParent = self.parents[currentParent]
#         return currentParent

#     # O(log(n)) time | O(1) space - where n is the total number of values
#     def union(self, valueOne, valueTwo):
#         # Write your code here
#         if valueOne not in self.parents or valueTwo not in self.parents:
#             return

#         valueOneRoot = self.find(valueOne)
#         valueTwoRoot = self.find(valueTwo)
#         if self.ranks[valueOneRoot] < self.ranks[valueTwoRoot]:
#             self.parents[valueOneRoot] = valueTwoRoot
#         elif self.ranks[valueOneRoot] > self.ranks[valueTwoRoot]:
#             self.parents[valueTwoRoot] = valueOneRoot
#         else:
#             self.parents[valueTwoRoot] = valueOneRoot
#             self.ranks[valueOneRoot] += 1



# Solution 3
# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
# class UnionFind:
#     def __init__(self):
#         # Write your code here
#         self.parents = {}

#     # O(1) time | O(1) space
#     def createSet(self, value):
#         # Write your code here
#         self.parents[value] = value

#     # O(n) time | O(1) space - where n is the total number of values
#     def find(self, value):
#         # Write your code here
#         if value not in self.parents:
#             return None

#         currentParent = value
#         while currentParent != self.parents[currentParent]:
#             currentParent = self.parents[currentParent]
#         return currentParent

#     # O(n) time | O(1) space - where n is the total number of values
#     def union(self, valueOne, valueTwo):
#         # Write your code here
#         if valueOne not in self.parents or valueTwo not in self.parents:
#             return

#         valueOneRoot = self.find(valueOne)
#         valueTwoRoot = self.find(valueTwo)
#         self.parents[valueTwoRoot] = valueOneRoot
