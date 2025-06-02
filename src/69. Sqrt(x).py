class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        lowest_number = 1
        biggest_number = x

        while lowest_number <= biggest_number:
            possible_result = (biggest_number + lowest_number) // 2
            squared = possible_result * possible_result

            if squared > x:
                biggest_number = possible_result - 1
            elif squared < x:
                lowest_number = possible_result + 1
            else:
                return possible_result

        return biggest_number

if __name__ == '__main__':
    # print(Solution().mySqrt(100))
    # print(Solution().mySqrt(1))
    # print(Solution().mySqrt(4))
    print(Solution().mySqrt(10))
    print(Solution().mySqrt(8))
    print(Solution().mySqrt(7))