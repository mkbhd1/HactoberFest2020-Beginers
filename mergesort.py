def MergeSort(L):
    if len(L)>1:
        mid = len(L)//2
        ltree = L[:mid]
        rtree = L[mid:]
        MergeSort(ltree)
        MergeSort(rtree)
        i=j=k=0      
        while i < len(ltree) and j < len(rtree):
            if ltree[i] < rtree[j]:
                L[k]=ltree[i]
                i=i+1
            else:
                L[k]=rtree[j]
                j=j+1
            k=k+1
        while i < len(ltree):
            L[k]=ltree[i]
            i=i+1
            k=k+1
        while j < len(rtree):
            L[k]=rtree[j]
            j=j+1
            k=k+1
import time 
L = eval(input("ENTER A LIST :"))
MergeSort(L)
print("PERFORMING MERGE SORT...")
time.sleep(5)
print("\nSORTED LIST IS :", L)