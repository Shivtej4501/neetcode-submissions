class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        a = [1]*len(nums)
        j = 0
        for i in range(0, len(nums)-1):
            if nums[i+1] == (nums[i] +1):
                a[j] += 1
            else : 
                j +=1
        a.sort()
        return a[-1]