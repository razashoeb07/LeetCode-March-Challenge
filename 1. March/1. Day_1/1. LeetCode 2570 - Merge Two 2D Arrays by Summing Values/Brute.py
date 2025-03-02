from typing import List

"""
Time Complexity Analysis
First loop (merging adjacent equal numbers)
Runs O(n-1) ≈ O(n) iterations.

Second loop (collecting non-zero elements)
Runs O(n) iterations.

Appending zeros at the end
Runs O(n) iterations in the worst case.
Total Time Complexity: O(n) + O(n) +O(n) =O(n)


space complexity is O(n) due to the extra result list.
"""

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: Perform operations on array
        for i in range(n-1):
            if nums[i] == nums[i+1] and nums[i] != 0:
                nums[i] *= 2
                nums[i+1] = 0

        # Step 2: Move all non-zero elements to result
        result = []
        zero_count = 0

        for num in nums:
            if num != 0:
                result.append(num)

        # Step 3: Append all zeros at the end
        zero_count = n - len(result)
        for _ in range(zero_count):
            result.append(0)

        return result

sol = Solution()
nums = [1, 2, 2, 1, 1, 0]  # Single test case
output = sol.applyOperations(nums)
print(f"Input: {nums}\nOutput: {output}")