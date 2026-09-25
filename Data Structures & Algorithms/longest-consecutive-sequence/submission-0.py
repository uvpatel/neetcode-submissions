class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Check if num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                count = 1

                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    count += 1

                longest = max(longest, count)

        return longest