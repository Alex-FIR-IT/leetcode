from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        even_length = 0
        odd_length = 0
        previous_number = nums[0] - 1
        alternation_length = 0

        for number in nums:
            if (previous_number + number) % 2 == 1:
                alternation_length += 1
                previous_number = number

            if number % 2 == 0:
                even_length += 1
            else:
                odd_length += 1

        return max(even_length, odd_length, alternation_length)
