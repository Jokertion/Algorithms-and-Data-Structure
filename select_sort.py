def select_sort(alist):
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[i] < alist[min_index]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


li = [6, 4, 8, 9, 35, 78, 250, 46, 91, 24]
print(li)
select_sort(li)
print(li)
