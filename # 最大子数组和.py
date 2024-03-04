# 最大子数组和
def maxSubArray() -> int:
    nums = [-2,-1]
    max_num = nums[0]
    cur_max_num = 0
    curr_num = 0
    if len(nums) == 1:
        return nums[0]

    for i in range(len(nums)):
        cur_max_num = nums[i]
        curr_num = nums[i]
        
        j = i + 1
        # 要看j是否越界
        while j < len(nums): 
            curr_num += nums[j]
            if cur_max_num < curr_num:
                cur_max_num = curr_num
            j += 1 
        max_num = max(max_num, cur_max_num)
    return max_num
a = maxSubArray()
print(a)
# 上面的方法时间复杂度太高了