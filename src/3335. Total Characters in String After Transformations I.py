import string
from collections import Counter
from typing import List


# class Solution:
#     def lengthAfterTransformations(self, s: str, t: int) -> int:
#
#         mappings = {symbol: index
#                     for index, symbol
#                     in enumerate(string.ascii_lowercase)
#                     }
#         for transformation_number in range(t):
#             print(f"{transformation_number=}, {len(s)=}")
#             new_string: List[str] = []
#
#             for index, symbol in enumerate(s):
#                 if symbol == 'z':
#                     new_string.append('a')
#                     new_string.append('b')
#                 else:
#                     new_string.append(string.ascii_lowercase[mappings.get(symbol) + 1])
#             s = new_string
#
#         return len(s)

import string
from typing import List
from collections import Counter, deque

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        counter = Counter(s)
        letters_frecuency = deque()

        for letter in string.ascii_lowercase:
            letters_frecuency.append(counter.get(letter, 0))

        for iteration_number in range(t):
            z_letter_count = letters_frecuency.pop()

            letters_frecuency.appendleft(z_letter_count)
            letters_frecuency[1] += z_letter_count

        return sum(letters_frecuency)




if __name__ == '__main__':
    print(Solution().lengthAfterTransformations("jqktcurgdvlibczdsvnsg", 7517))