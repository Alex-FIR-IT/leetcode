class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        binary_mapping = {
            0: {'current_binary_number': 0,
                'adding_digit': 0
                },
            1: {'current_binary_number': 1,
                'adding_digit': 0
                },
            2: {'current_binary_number': 0,
                'adding_digit': 1
                },
            3: {'current_binary_number': 1,
                'adding_digit': 1
                }
        }

        resulting_number = ''
        adding_digit = 0

        for index in range(1, max(len(a), len(b)) + 1):
            print(index)
            if len(a) >= index:
                a_digit = int(a[-index])
            else:
                a_digit = 0

            if len(b) >= index:
                b_digit = int(b[-index])
            else:
                b_digit = 0

            mapping_result = binary_mapping.get(a_digit + b_digit + adding_digit)

            current_binary_number = mapping_result.get('current_binary_number')
            adding_digit = mapping_result.get('adding_digit')

            resulting_number = str(current_binary_number) + resulting_number

        if adding_digit == 1:
            resulting_number = "1" + resulting_number

        return resulting_number


if __name__ == '__main__':
    # print(Solution().addBinary("11", "1"))
    print(Solution().addBinary("11011", "1101000"))
