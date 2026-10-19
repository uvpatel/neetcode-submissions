
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()  # Stores indices
        result = []

        for i in range(len(nums)):
            # Remove indices outside the current window
            while q and q[0] <= i - k:
                q.popleft()

            # Remove smaller elements from the back
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # Start recording once the first window is complete
            if i >= k - 1:
                result.append(nums[q[0]])

        return result
