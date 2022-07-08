swap = [1, 2, 'four', 3]

# # swapping easily in python
swap[2], swap[3] = swap[3], swap[2]

print(swap)

li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30, 
1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]

# check if a list is sorted or not

def is_sorted(li):
    for i in range(len(li) - 1):
        if (li[i] > li[i+1]):
           return False
        
    return True
        
print(is_sorted(li))
    
