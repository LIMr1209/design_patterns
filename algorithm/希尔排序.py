# //TODO 将数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（步长更长了，列数更少了）来进行。最后整个表就只有一列了。将数组转换至表是为了更好地理解这算法，算法本身还是使用数组进行排序。

# //TODO 最优时间复杂度：根据步长序列的不同而不同
# //TODO 最坏时间复杂度：O(n2)
# //TODO 稳定想：不稳定

def shell_sort(alist):
    n = len(alist)

    # 初始步长

    gap = n // 2

    while gap > 0:

        # 按步长进行插入排序

        for i in range(gap, n):

            j = i

            # 插入排序

            while j >= gap and alist[j - gap] > alist[j]:
                alist[j - gap], alist[j] = alist[j], alist[j - gap]

                j -= gap

        # 得到新的步长

        gap = gap // 2


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

shell_sort(alist)

print(alist)
