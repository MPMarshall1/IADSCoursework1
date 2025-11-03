
# File:    smartsort.py
# Author:  John Longley
# Date:    October 2025

# Template file for Inf2-IADS (2025-26) Coursework 1, Part A:
# Implementation of hybrid Merge Sort / Insert Sort,
# with optimization for already sorted segments.


import peekqueue
from peekqueue import PeekQueue

# Global variables

comp = lambda x,y: x<=y       # comparison function used for sorting

insertSortThreshold = 10

sortedRunThreshold = 10
    
# TODO: Task 1. Hybrid Merge/Insert Sort

# In-place Insert Sort on A[m],...,A[n-1]:

def insertSort(A,m,n):
    """In-place Insert Sort on A[m],..,A[n-1]"""
    for i in range(m+1,n):
        temp = A[i]
        j = i - 1
        while ((j >= m) & (comp(temp, A[j]))):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = temp
    return A


def merge(C,D,m,p,n):
    """Merge C[m],...,C[p-1] and C[p],...,C[n-1] into D[m],...,D[n-1]"""
    a = m
    b = p
    for i in range(m, n):
        if (a==p): 
            D[i] = C[b]
            b = b + 1
        elif (b==n):
            D[i] = C[a]
            a = a + 1
        elif (comp(C[b], C[a])):
            D[i] = C[b]
            b = b + 1
        else:
            D[i] = C[a]
            a = a + 1
    


def greenMergeSort(A,B,m,n):
    """Merge Sort A[m],...,A[n-1] using just B[m],...,B[n-1] as workspace.
    Deferr to Insert Sort if length <= insertSortThreshold"""
    if (n-m <= insertSortThreshold):
        A = insertSort(A, m, n)
    else:
        q = (m+n) // 2
        p = (m+q) // 2
        r = (q+n) // 2
        greenMergeSort(A, B, m, p)
        greenMergeSort(A, B, p, q)
        greenMergeSort(A, B, q, r)
        greenMergeSort(A, B, r, n)
        merge(A, B, m, p, q)
        merge(A, B, q, r, n)
        merge(B, A, m, q, n)

# Provided code:

def greenMergeSortAll(A):
    B = [None] * len(A)
    greenMergeSort(A,B,0,len(A))
    return A


# TODO: Task 2. Detecting already sorted runs.

def allSortedRuns(A):
    """Build and return queue of sorted runs of length >= sortedRunThreshold.
    Queue items should be pairs (i,j) such that A[i],...,A[j-1] is sorted."""
    queue = PeekQueue()
    i = 0
    while (i < len(A)):
        j = i
        k = j + 1
        while (k < len(A) and comp(A[j], A[k])):
            j = j + 1
            k = j + 1
        if ((j - i) >= sortedRunThreshold):
            queue.push((i, k))
        i = k
    return queue
        


def isWithinRun(Q,i,j):
    """Test whether A[i],...,A[j-1] is sorted according to info in Q."""
    while (Q.peek() != None):
        if (Q.peek()[1] < i):
            Q.pop()
        else:
            return (Q.peek()[0] <= i and Q.peek()[1] >= j)
    return False


def smartMergeSort(A,B,Q,m,n):
    """Improvement on greenMergeSort taking advantage of sorted runs."""
    if (isWithinRun(Q, m, n)):
        return A
    if (n-m <= insertSortThreshold):
        A = insertSort(A, m, n)
    else:
        q = (m+n) // 2
        p = (m+q) // 2
        r = (q+n) // 2
        smartMergeSort(A, B, Q, m, p)
        smartMergeSort(A, B, Q, p, q)
        smartMergeSort(A, B, Q, q, r)
        smartMergeSort(A, B, Q, r, n)
        merge(A, B, m, p, q)
        merge(A, B, q, r, n)
        merge(B, A, m, q, n)

# Provided code:

def smartMergeSortAll(A):
    B = [None] * len(A)
    Q = allSortedRuns(A)
    smartMergeSort(A,B,Q,0,len(A))
    return A


# TODO: Task 3. Asymptotic analysis of smartMergeSortAll

# 1. Justification of O(n lg n) bound.
#
#
#
#
# (continue as necessary)

# 2. Runtime analysis for nearly-sorted inputs.
#
#
#
#
# (continue as necessary)


# Functions added for automarking purposes - please don't touch these!

def set_comp(f):
    global comp
    comp = f

def set_insertSortThreshold(n):
    global insertSortThreshold
    insertSortThreshold = n

def set_sortedRunThreshold(n):
    global sortedRunThreshold
    sortedRunThreshold = n

def set_insertSort(f):
    global insertSort
    insertSort = f

# End of file
