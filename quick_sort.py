def quick_sort(alist, first, last):
    # 退出递归
    if first >= last:
        return

    low = first
    high = last
    mid_value = alist[first]

    while low < high:
        # 移动high游标，碰到小值停止，将其放到low上
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        # 移动low游标，碰到大值停止，将其放到high上
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value

    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)


li = [6, 4, 8, 9, 35, 78, 250, 46, 91, 24]
quick_sort(li, 0, len(li)-1)
print(li)
