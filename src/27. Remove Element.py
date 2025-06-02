class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = 0
        index = 0

        while True:

            if len(nums) <= index:
                break

            current_number = nums[index]

            if current_number == val:
                nums.pop(index)
                k += 1
            else:
                index += 1

        print(nums)
        return len(nums) - k


class PossibleNeedle:

    def __init__(self, start_index):
        self.start_index = start_index
        self.current_index = None
        self.word = ''

    def __add__(self, other: str):
        self.word += other

        if self.current_index is None:
            self.current_index = 0
        else:
            self.current_index += 1


if __name__ == '__main__':
    print(Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))