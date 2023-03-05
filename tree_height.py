# python3

import sys
import threading
import numpy

def compute_height(n, parents):  
    heights = [0] * n

    def calc_height(node):
        if heights[node] != 0:
            return heights[node]
        
        if parents[node] == -1:
            heights[node] = 1
            return heights[node]
        
        heights[node] = 1 + calc_height(parents[node])
        return heights[node]
    
    max_heights = 0
    for i in range(n):
        max_heights = max(max_heights, calc_height(i))

    return max_heights  


def main():
    source = input("K/F: ")

    if source in ['F', 'f']:
        file_name = input("filename: ")

        while 'a' in file_name:
            file_name = input("filename ")

            while 'a' in file_name:
                file_name = input("valid file name: ")

        try:
            with open(f"folder{file_name}") as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))

        except FileNotFoundError:
            print("file not found.")
            sys.exit()

    else:
        n = int(input("enter num: "))
        parents = list(map(int, input("Enter the parents node: ").split()))

    height = compute_height(n, parents)

    print(f"The height of the tree is {height}.")    


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()