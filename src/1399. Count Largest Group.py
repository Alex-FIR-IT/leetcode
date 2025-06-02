# class Solution(object):
#     def countLargestGroup(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         mapping = {}
#         max_len = 0
#         for number in range(1, n + 1):
#             digits_sum = 0
#
#             for digit in str(number):
#                 digits_sum += int(digit)
#
#             if mapping.get(digits_sum):
#                 mapping[digits_sum].append(number)
#             else:
#                 mapping[digits_sum] = [number]
#
#             if len(mapping[digits_sum]) > max_len:
#                 max_len = len(mapping[digits_sum])
#
#         answer = 0
#         for m in mapping.values():
#             if max_len == len(m):
#                 answer += 1
#
#         return answer


# class Solution(object):
#     def countLargestGroup(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         frequency = {}
#         max_len = 0
#         groups_with_max_length = 0
#
#         for number in range(1, n + 1):
#             digits_sum = 0
#
#             while number > 0:
#                 digits_sum += number % 10
#                 number //= 10
#
#             if frequency.get(digits_sum):
#                 frequency[digits_sum] += 1
#             else:
#                 frequency[digits_sum] = 1
#
#             if frequency[digits_sum] > max_len:
#                 max_len = frequency[digits_sum]
#                 groups_with_max_length = 0
#
#             if frequency[digits_sum] == max_len:
#                 groups_with_max_length += 1
#
#         return groups_with_max_length

from collections import Counter

# class Solution(object):
#     def countLargestGroup(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         frequency = Counter()
#         for number in range(1, n + 1):
#             digits_sum = 0
#
#             while number > 0:
#                 digits_sum += number % 10
#                 number //= 10
#
#             frequency[digits_sum] += 1
#
#         max_len = 0
#         answer = 0
#         for digits_sum, numbers_count in frequency.items():
#             if max_len < numbers_count:
#                 max_len = numbers_count
#                 answer = 0
#
#             if numbers_count == max_len:
#                 answer += 1
#
#         return answer
#

from itertools import combinations
from collections import Counter

class Solution(object):
    def countLargestGroup(self, n):
        digit_sum = [0] * (n + 1)
        for num in range(1, n + 1):

            digit_sum[num] = digit_sum[num // 10] + num % 10

        frequency = Counter(digit_sum[1:])

        max_freq = max(frequency.values())
        return sum(1 for v in frequency.values() if v == max_freq)


from collections import Counter

class Solution(object):
    def countLargestGroup(self, n):
        digit_sum = [0]
        for num in range(1, n + 1):
            digit_sum.append(digit_sum[num // 10] + num % 10)



        frequency = Counter(digit_sum[1:])

        max_freq = max(frequency.values())
        return sum(1 for v in frequency.values() if v == max_freq)


# class Solution(object):
#
#     digits_sum = {}
#     def countLargestGroup(self, n):
#         for number in range(1, n + 1):
#             digits = []
#             digits_sum = {}
#
#             while number > 0:
#                 digit = number % 10
#                 number //= 10
#                 digits.append(digit)
#
#             if
#             digits_sum[tuple(sorted(digits))] = sum(digits)
#
#

if __name__ == '__main__':
    print(Solution().countLargestGroup(1434))

