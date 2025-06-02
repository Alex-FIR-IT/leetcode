class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        index = -1

        if len(digits) == 0:
            return digits

        while len(digits) >= abs(index):
            current_digit = digits[index]

            if current_digit < 9:
                digits[index] += 1
                increment_required = False
                break
            else:
                digits[index] = 0
                index -= 1
                increment_required = True
                continue

        if increment_required:
            digits.insert(0, 1)

        return digits




if __name__ == '__main__':
    print(Solution().plusOne(digits=[1, 9]))
    print(Solution().plusOne(digits=[1, 9, 9, 9, 9]))
    print(Solution().plusOne(digits=[1, 9, 4, 9, 9]))
    print(Solution().plusOne(digits=[0]))
    print(Solution().plusOne(digits=[1]))
    print(Solution().plusOne(digits=[9]))
    print(Solution().plusOne(digits=[9, 9]))