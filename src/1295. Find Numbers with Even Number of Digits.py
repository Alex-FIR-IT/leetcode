from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_numbers_count = 0

        mappings_number_to_digits_count = {}

        for number in nums:
            digits_count = mappings_number_to_digits_count.get(number, 0)

            if not digits_count:
                number_copy = number
                sub_number = 0

                while number_copy != sub_number:
                    remainder = number % 10
                    sub_number = remainder * pow(10, digits_count) + sub_number

                    sub_digits_count = mappings_number_to_digits_count.get(number, 0)
                    if sub_digits_count:
                        digits_count += sub_digits_count
                        mappings_number_to_digits_count[number_copy] = digits_count
                        break

                    number //= 10
                    digits_count += 1

                    sub_number_digits_count = mappings_number_to_digits_count.get(sub_number, 0)

                    if not sub_number_digits_count:
                        mappings_number_to_digits_count[sub_number] = digits_count

            if digits_count % 2 == 0:
                even_numbers_count += 1

        return even_numbers_count



if __name__ == '__main__':
    # print(Solution().findNumbers([252]))
    print(Solution().findNumbers([580,317,640,957,718,764]))