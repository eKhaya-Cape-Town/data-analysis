#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 21:26:10 2020

@author: Alaisha Naidu
Practice

"""

#Question 1
#Fibonaci Sequence Iteration
def fibI(n):
    terms = [0,1]
    i = 2 
    while i <= n:
        terms.append(terms[i-1] + terms[i -2])
        i = i + 1
    return terms


#Question 2
#Fibonaci Sequence Recursion 
def fibR(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return (fibR(n-1) + fibR(n-2)) #note problem of redundancy 


#Question 3
#Palindrome check
def PalCheck1(string): 
    # Comparing first and last, working inwards saves half the number of comparisons
    # than inverting each word and comparing every letter
    char_index1 = 0 
    char_index2 = len(string)-1
    while char_index1 <= char_index2:
        if string[char_index1] == string[char_index2]:
            print(string[char_index1],string[char_index2], "True")
            char_index1 +=1
            char_index2 -=1
        else:
            return False

#print(PalCheck1("alaisha"))

#Question 4
#Anagram check
from collections import Counter
def AnaCheck(string1, string2):
    str1 = string1.replace(" ", "")
    str2 = string2.replace(" ", "")
    if len(str1) == len(str2):
        count1 = Counter(str1)
        count2 = Counter(str2)
        print (count1-count2) #If it returns empty then it is an anagram
        if count1 == count2:
            print(string1,"-", string2, "\n", "This is an anagram")
        else:
            print(string1,"-", string2, "\n", "not an anagram")
    else:
        print(string1,"-", string2, "\n", "not an anagram")
        
#print(AnaCheck("school master", "the classroom")) 

#Question 5
#Determine if a Binary tree is a binary search tree or not 
class Node(object):
    def _init_(self, value):
        self.value = value
        self.left = None #initial left child is none
        self.right = None #initial right child is none
        
class BinaryTree(object):
    def _init_(self, root):
        self.root = Node(root)
        
tree = BinaryTree(1)                #         1
tree.root.left = Node(2)            #       /   \
tree.root.right = Node(3)           #     2       3
tree.root.left.left = Node(4)       #    / \     / \
tree.root.left.right = Node(5)      #   4   5   6   7
tree.root.right.left = Node(6) 
tree.root.right.right = Node(7) 


