# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    # create a list of children for each node
    children = [[] for _ in range(n)]
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            children[parent].append(i)

    # recursive function to compute height of a subtree
    def height(node):
        if not children[node]:
            return 1
        return 1 + max(height(child) for child in children[node])

    # compute height of the whole tree
    return height(root)

# read input values
n = int(input())
parents = list(map(int, input().split()))

# compute and print the height of the tree
print(compute_height(n, parents))