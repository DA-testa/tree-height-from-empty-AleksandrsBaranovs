# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    tree = {i: [] for i in range(n)}
    for i in range(n):
        if parents[i] != -1:
            tree[parents[i]].append(i)
    
    def height(node):
        if not tree[node]:
            return 0
        else:
            return 1 + max(height(child) for child in tree[node])

   
    return height(parents.index(-1))

def main():
    n = int(input(""))
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()