def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


li = [6, 4, 8, 9, 35, 78, 25, 46, 91, 24]
insert_sort(li)
print(li)
