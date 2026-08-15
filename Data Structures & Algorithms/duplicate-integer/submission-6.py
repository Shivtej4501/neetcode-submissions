class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_len = len(nums)
        set_con = set(nums)
        set_len = len(set_con)
        return list_len != set_len
        # if list_len == set_len:
        #     return False
        # else:
        #     return True

# Logic is Set does not contain duplicate elements 