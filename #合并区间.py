# 合并区间
def merge():
    intervals = [[1,4],[4,5]]
    ans_list = [intervals[0]]#第一个元素肯定是答案

    def panduan(a,b):
        if a[0] <= b[0] and a[1] >= b[0]:
            return True
            # 如果是重叠的状态
        return False
    # 给列表排序
    # 对于列表 x 中的每个子列表，我们都取其第一个元素作为排序的依据
    # key 参数应该是一个函数，该函数用于从每个待排序的元素中提取一个比较键
    intervals = sorted(intervals,key = lambda x: x[0])
    
    for i in range(1,len(intervals)):
        if panduan(ans_list[-1] ,intervals[i]):
            ans_list[-1][0] = min(ans_list[-1][0], intervals[i][0])
            ans_list[-1][1] = max(ans_list[-1][0], intervals[i][1])
        else:
            ans_list.append(intervals[i])

    return ans_list

lis = merge()
print(lis)