import numpy
import timeit

'''
This file contains the implementation of a hashtable using a binary search tree as a
collision resolution method
'''
class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class HashTable:
    MaxArraySize = 509


    def __init__(self):
        self.buckets = [None]*self.MaxArraySize
        self.size = 0

    def hash(self, x):

        if x == 0:
            return 0

        elif x <= 3:
            return x

        else:
            key = x * x
            a = str(key)
            output = a[len(a) // 2]

            g = int(output)
            hash_func = g % self.MaxArraySize

            return hash_func

    def insertData(self, node, x):
        if node is None:
            node = Node(x)

        else:
            if x <= node.data:
                node.left = self.insertData(node.left, x)

            if x > node.data:
                node.right = self.insertData(node.right, x)

        return node


    def insert(self,x):
        self.size += 1

        index = self.hash(x)
        root = self.buckets[index]
        root = self.insertData(root,x)
        self.buckets[index] = root


    def inOrder(self, root):

        if root is not None:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)

    def printHashtable(self):
        for i in range(self.MaxArraySize):
            if self.buckets[i] is not None:
                print("Bucket ", i , ":  ")
                print(self.inOrder(self.buckets[i]))
                print(" ")