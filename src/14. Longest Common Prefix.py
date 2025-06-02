class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        longest_prefix = ''
        break_external_loop = False

        for letter_index, letter in enumerate(strs[0]):
            for str_word in strs:

                if len(str_word) < letter_index + 1 or not letter == str_word[letter_index]:
                    break_external_loop = True
                    break
            else:
                longest_prefix += letter

            if break_external_loop is True:
                break

        return longest_prefix


if __name__ == '__main__':
    # print(Solution().longestCommonPrefix(strs=["flower", "flow", "flight"]))
    # print(Solution().longestCommonPrefix(strs=["fkow", "flower"]))
    print(Solution().longestCommonPrefix(strs=["ab", "a"]))
