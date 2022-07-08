li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30, 
1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]


def is_sorted(li):
    for i in range(len(li) - 1):
        if (li[i] > li[i+1]):
           return False
        
    return True

def insertion_sort(li):
    # iterate over the entire list, loop downward when we find a value that is smaller than what is to the left
    for index in range(len(li)):
        # current number for comparison
        current_num = li[index]
        # position sliding back down list
        comparison_pos = li[index - 1]
        while current_num >= 0 and current_num > li[comparison_pos]:
            li[comparison_pos], li[comparison_pos + 1] = li[comparison_pos + 1], li[comparison_pos]
            comparison_pos -= 1


insertion_sort(li)
print(li)
print(is_sorted(li))