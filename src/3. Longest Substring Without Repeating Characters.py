# Сохраняю последние индексы и если вижу, что буква повторяеться, то сдвигаю left_pointer на индекс от этой буквы + 1


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
#
#         left_pointer = 0
#         right_pointer = 0
#
#         longest_substring_len = 0
#         current_substring_len = 0
#
#         mappings = {1: set(),
#                    2: set()
#                    }
#         lst = []
#         while right_pointer < len(s):
#             if mappings[2]:
#                 left_symbol = s[left_pointer]
#
#                 left_pointer += 1
#                 current_substring_len -= 1
#                 if left_symbol in mappings[1]:
#                     mappings[1].discard(left_symbol)
#                 else:
#                     mappings[2].discard(left_symbol)
#                     mappings[1].add(left_symbol)
#
#             else:
#                 right_symbol = s[right_pointer]
#
#                 right_pointer += 1
#                 current_substring_len += 1
#                 if right_symbol in mappings[1]:
#                     mappings[1].discard(right_symbol)
#                     mappings[2].add(right_symbol)
#                     continue
#                 else:
#                     mappings[1].add(right_symbol)
#
#                     if current_substring_len > longest_substring_len:
#                         longest_substring_len = current_substring_len
#                         lst.append((right_symbol, right_pointer))
#                         if longest_substring_len == 8:
#
#
#                             print(mappings, len(mappings[1]), right_pointer, right_symbol)
#                             print(lst, len(lst))
#                             break
#         return longest_substring_len
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left_pointer = 0
        right_pointer = 0

        max_substring_len = 0
        current_substring_len = 0

        mappings = {}  # symbol to its index

        while right_pointer < len(s):
            right_symbol = s[right_pointer]

            if right_symbol in mappings and left_pointer <= mappings.get(right_symbol):
                left_pointer = mappings.get(right_symbol) + 1
                current_substring_len = right_pointer - left_pointer + 1
            else:
                current_substring_len += 1

                if current_substring_len > max_substring_len:
                    max_substring_len = current_substring_len

            mappings[right_symbol] = right_pointer
            right_pointer += 1

        return max_substring_len




if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    # print(Solution().lengthOfLongestSubstring("jfdkjfjrhgdjhkafhidjkdjfjeqhruijjkvrhiejfhkfhdgjjfdkjfjrhgdjhkafhidjkdjfjeqhruijjkvrhiejfhkfhdgjfjdkjfjfdkjfjrhgdjhkafhidjkdjfjeqhruijjkvrhiejfhkfhdgjfjkjsjfkhvjdjfhakdghjdksahgkdbjdksjvdkfhdjkjjdkfdjghkbvdjhiwjkjgkfcjdjfjkldnfksjjrnvnfjjskfdkfkklgdlkkjdjvkdjfkjdkfjkdhkv4"))
    # print(Solution().lengthOfLongestSubstring("tmmzuxt"))