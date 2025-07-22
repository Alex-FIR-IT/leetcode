from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums:  List[int]) -> int:

        max_subarray_sum = 0
        subarray_sum = 0
        unique_values = set()
        left_pointer = 0

        for number in nums:
            while number in unique_values:
                subarray_sum -= nums[left_pointer]
                unique_values.remove(nums[left_pointer])
                left_pointer += 1

            subarray_sum += number
            unique_values.add(number)

            max_subarray_sum = max(subarray_sum, max_subarray_sum)

        return max_subarray_sum
