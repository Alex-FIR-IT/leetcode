# from collections import deque
#
#
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#
#         stack = deque()
#
#         nums1_index = 0
#         nums2_index = 0
#         max_nums1_len = m + n
#
#         while nums1_index < max_nums1_len or nums2_index < n or stack:
#
#             min_numbers_array = []
#             if stack:
#                 min_numbers_array.append(stack[0])
#             if nums1_index < m:
#                 min_numbers_array.append(nums1[nums1_index])
#             if nums2_index < n:
#                 min_numbers_array.append(nums2[nums2_index])
#
#             min_number = min(min_numbers_array)
#
#             if stack and min_number == stack[0]:
#                 if nums1_index < m:
#                     stack.append(nums1[nums1_index])
#                 nums1[nums1_index] = stack.popleft()
#                 nums1_index += 1
#
#             elif m > nums1_index and min_number == nums1[nums1_index]:
#                 nums1_index += 1
#             else:
#                 #  len(nums2) > nums2_index and min_number == nums2[nums2_index]
#
#                 if nums1_index < m:
#                     stack.append(nums1[nums1_index])
#                 nums1[nums1_index] = min_number
#                 nums1_index += 1
#                 nums2_index += 1
#
#
#
#         print(nums1)


class Solution:
    def merge(self, nums1, m, nums2, n):
        # Указатели с конца неиспользуемых частей
        i, j, k = m - 1, n - 1, m + n - 1
        # Пока есть что сравнивать
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # Если в nums2 ещё остались элементы — переносим их
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1



if __name__ == '__main__':
    # Solution().merge([1,2,3,0,0,0], 3, [2, 5, 5], 3)
    # Solution().merge([2,0], 1, [1], 1)
    # Solution().merge([-1,-1,0,0,0,0], 4, [-1,0], 2)
    # Solution().merge([-1,0,0,0,3,0,0,0,0,0,0], 5, [-1,-1,0,0,1,2], 6)
    Solution().merge([4,5,6,0,0,0], 3, [1,2, 3], 3)

