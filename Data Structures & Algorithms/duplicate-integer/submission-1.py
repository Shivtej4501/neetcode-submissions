class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_len = len(nums)
        set_con = set(nums)
        set_len = len(set_con)
        if list_len == set_len:
            return False
        else:
            return True