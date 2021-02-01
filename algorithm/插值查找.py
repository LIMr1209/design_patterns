'''
算法简介

    插值查找是根据要查找的关键字key与查找表中最大最小记录的关键字比较后的 查找方法，其核心就在于插值的计算公式 (key-a[low])/(a[high]-a[low])*(high-low)。
    时间复杂度o(logn)但对于表长较大而关键字分布比较均匀的查找表来说，效率较高。
算法思想
    基于二分查找算法，将查找点的选择改进为自适应选择，可以提高查找效率。当然，差值查找也属于有序查找。
    注：对于表长较大，而关键字分布又比较均匀的查找表来说，插值查找算法的平均性能比折半查找要好的多。反之，数组中如果分布非常不均匀，那么插值查找未必是很合适的选择。
复杂度分析
    时间复杂性：如果元素均匀分布，则O（log log n）），在最坏的情况下可能需要 O（n）。
    空间复杂度：O（1）。
'''


def binary_search(lis, key):
    low = 0
    high = len(lis) - 1
    time = 0
    while low < high:
        time += 1
        # 计算mid值是插值算法的核心代码
        mid = low + int((high - low) * (key - lis[low]) / (lis[high] - lis[low]))
        print("mid=%s, low=%s, high=%s" % (mid, low, high))
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            # 打印查找的次数
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False


if __name__ == '__main__':
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = binary_search(LIST, 222)
    print(result)
