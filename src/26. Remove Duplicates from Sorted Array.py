# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         previous_number = None
#         new_nums = []
#
#         for current_number in nums:
#             if previous_number != current_number:
#                 new_nums.append(current_number)
#
#             previous_number = current_number
#
#         nums = new_nums
#
#         print(nums)
#         return len(nums)
#

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         index = 0
#         previous_number = None
#
#         while len(nums) > index:
#
#             if previous_number == nums[index]:
#                 nums.pop(index)
#                 # index -= 1
#             else:
#                 previous_number = nums[index]
#                 index += 1
#
#
#         print(nums)
#         return len(nums)


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        for index in range(len(nums)):
            if nums[index] == nums[index - 1] and len(nums) != 1:
                count += 1
            else:
                nums[index - count] = nums[index]

        print(nums)
        return len(nums) - count


if __name__ == '__main__':
    print(Solution().removeDuplicates(nums=[1, 1, 2]))
    print(Solution().removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))
    print(Solution().removeDuplicates(nums=[1]))
    print(Solution().removeDuplicates(nums=[1, 1]))
