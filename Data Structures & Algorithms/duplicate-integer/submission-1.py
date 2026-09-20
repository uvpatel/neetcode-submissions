class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = nums
        if(len(set(nums2)) != len(nums)):
            return True
        else:
            return False