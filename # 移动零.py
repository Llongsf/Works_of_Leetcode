# 移动零
class Solution:
    def moveZeroes() -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = [0,1,0,3,12]
        b = 0
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[b] = nums[i]
                b += 1
        for j in range(b,len(nums)):
            nums[j] = 0
        print(nums)
    moveZeroes()
    
        

                