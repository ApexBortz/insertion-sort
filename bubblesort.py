
li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30, 
1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]

# Solution 1 for bubble sort ( for loop )
def sort_list(li):
    for num in range(len(li) - 1, 0, -1):
        for i in range(num):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]

    return True

sort_list(li)
print(li)


# Solution 2 for bubble sort ( while loop )
def bubble_sort(li):
    # flag that tells us if the list is sorted
    swapped = True
    while swapped:
        # assume no swap will be made
        swapped = False
        for i in range(len(li) -1):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
                swapped = True

bubble_sort(li)
print(li)

# Solution 3 - Recursively 
# includes run count to check how many times the loop is iterated over
def list_sort(li, swap):
    run = 0
 
    for i in range(len(li) -1):
        if li[i] > li[i + 1]:
            li[i], li[i + 1] = li[i + 1], li[i]
            run += 1
            swap += 1

    if run == 0:
        print(li, "iterated this many times:", swap)
    else:
        list_sort(li, swap)
            
list_sort(li, 0)