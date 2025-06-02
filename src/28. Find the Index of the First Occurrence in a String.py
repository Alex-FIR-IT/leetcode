# class PossibleNeedle:
#
#     def __init__(self,
#                  *,
#                  start_index
#                  ):
#         self.start_index = start_index
#         self._current_index = None
#         self.word = ''
#
#     @property
#     def current_index(self):
#         return -1 if self._current_index is None else self._current_index
#
#     @current_index.setter
#     def current_index(self, value):
#         self._current_index = value
#
#     def __add__(self, other):
#         self.word += other
#
#         if self.current_index is None:
#             self.current_index = 0
#         else:
#             self.current_index += 1
#
#         return self
#
#     # def __repr__(self):
#     #     return (f"{self.start_index=}, "
#     #             f"{self._current_index=}, "
#     #             f"{self.word=}"
#     #             )
#
#
# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#
#         possible_needles = []
#
#         for haystack_index, haystack_symbol in enumerate(haystack):
#             index = 0
#
#             if haystack_symbol == needle[0]:
#                 possible_needles.append(PossibleNeedle(start_index=haystack_index
#                                                        )
#                                         )
#
#             while index < len(possible_needles):
#                 possible_needle = possible_needles[index]
#
#                 if haystack_symbol == needle[possible_needle.current_index + 1]:
#                     possible_needle += haystack_symbol
#
#                     index += 1
#                 else:
#                     possible_needles.pop(index)
#
#                 if possible_needle.word == needle:
#                     return possible_needle.start_index
#
#         else:
#             index = 0
#
#             while index < len(possible_needles):
#                 possible_needle = possible_needles[index]
#
#                 if possible_needle.word == needle:
#                     return possible_needle.start_index
#                 index += 1
#         return -1


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        possible_needle = ''
        possible_needle_index = None

        haystack_index = 0

        while haystack_index < len(haystack):
            haystack_symbol = haystack[haystack_index]

            if haystack_symbol == needle[len(possible_needle)]:
                if len(possible_needle) == 0:
                    possible_needle_index = haystack_index

                possible_needle += haystack_symbol

            else:
                if possible_needle_index is not None:
                    haystack_index = possible_needle_index
                    possible_needle_index = None
                    possible_needle = ''

            if len(possible_needle) == len(needle):
                return possible_needle_index
            haystack_index += 1
        else:
            return -1


if __name__ == '__main__':
    # print(Solution().strStr("sadbutsad", "sad"))
    # print(Solution().strStr("a", "a"))
# ?    print(Solution().strStr("aaa", "a"))
    print(Solution().strStr("mississippi", "pi"))

