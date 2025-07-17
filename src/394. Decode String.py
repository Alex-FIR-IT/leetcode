from collections import deque


class Solution:
    def decodeString(self, encoded_string: str) -> str:
        output_string = []

        for symbol in encoded_string:
            if symbol == ']':
                repeated_symbols = deque()

                while output_string[-1] != '[':
                    repeated_symbols.appendleft(output_string.pop())

                output_string.pop()
                number = deque()
                while output_string and output_string[-1].isdigit():
                    number.appendleft(output_string.pop())

                number = int(''.join(number))
                output_string.extend(repeated_symbols * number)
                del repeated_symbols
            else:
                output_string.append(symbol)

        return ''.join(output_string)

if __name__ == '__main__':
    print(Solution().decodeString("3[a]2[bc]"))