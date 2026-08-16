class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dic = {'0': [], '-1':[]}
        for i in range(0, len(nums)):
            if nums[i] == 0:
                dic['0'].append(i)
            if nums[i] < 0:
                dic['-1'].append(i)

        # finding the number of zeros
        if (len(dic['0']) == 0):
            prod = 1
            l =[] 
            for i in nums:
                prod *= i
            for i in nums:
                l.append(int(prod/i))
            return l
        if (len(dic['0']) == 1):
            prod =1
            l =[]
            for i in range(0, len(nums)):
                if i == dic['0'][0]:
                    continue 
                else:
                    prod *= nums[i]
            l = [0] * len(nums)
            l[dic['0'][0]]= prod
            return l          

        if (len(dic['0']) > 1):
            return [0]*len(nums)