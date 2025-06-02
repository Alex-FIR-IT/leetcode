import dis
from typing import List


class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target_subarrays_count = 0
        first_index = 0
        nums_len = len(nums)

        while first_index + 2 < nums_len:
            if (nums[first_index] + nums[first_index + 2]) * 2== nums[first_index + 1]:
                target_subarrays_count += 1

            first_index += 1

        return target_subarrays_count

class Solution2:
    def countSubarrays(self, nums: List[int]) -> int:

        total_subarrays = 0
        start_index = 0
        end_index = 2
        n = len(nums)
        while end_index < n:

            if (nums[start_index] + nums[end_index]) * 2 == nums[start_index + 1]:
                total_subarrays += 1

            start_index += 1
            end_index += 1

        return total_subarrays

if __name__ == '__main__':
    print(Solution().countSubarrays([2, -7, -6]))
    print(Solution2().countSubarrays([2, -7, -6]))

    dis.dis(Solution.countSubarrays)
    print('-------------')
    # dis.dis(Solution2.countSubarrays)



# import time
#
# N = 10_000_000
#
# # def one_var():
# #     i = 0
# #     while i + 3 < N:
# #         i += 1
#
# def two_vars():
#     i = 0
#     j = 3
#     while j < N:
#         i += 1
#         j += 1
#
# # t1 = time.time()
# # one_var()
# # print('one_var:', time.time() - t1)
#
# t2 = time.time()
# two_vars()
# print('two_vars:', time.time() - t2)