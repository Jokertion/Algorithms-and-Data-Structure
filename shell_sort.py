def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2


li = [6, 4, 8, 9, 35, 78, 250, 22, 91, 24]
shell_sort(li)
print(li)
