from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_pointer = current_pointer = 0
        right_pointer = len(nums) - 1

        while current_pointer <= right_pointer:
            current_color = nums[current_pointer]

            if current_color == 0:
                nums[left_pointer], nums[current_pointer] = nums[current_pointer], nums[left_pointer]
                current_pointer += 1
                left_pointer += 1

            elif current_color == 1:
                current_pointer += 1
            elif current_color == 2:
                nums[current_pointer], nums[right_pointer] = nums[right_pointer], nums[current_pointer]
                right_pointer -= 1
            else:
                raise NotImplementedError("Colors must be only 0, 1 or 2!")


        print(nums)

if __name__ == '__main__':
    # print(Solution().sortColors([1, 1, 2, 0, 1, 0]))
    print(Solution().sortColors([2, 0, 1]))