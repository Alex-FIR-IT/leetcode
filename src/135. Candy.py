from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

        distributed_candies = 0
        streak = 1
        previous_rating = ratings[0]
        ascending_candies_weight = []

        for index, rating in enumerate(ratings):

            if previous_rating < rating:
                streak += 1
            else:
                streak = 1

            previous_rating = rating
            ascending_candies_weight.append(streak)

        streak = 1
        previous_rating = ratings[-1]

        right_pointer = len(ratings) - 1

        while right_pointer >= 0:
            rating = ratings[right_pointer]
            if previous_rating < rating:
                streak += 1
            else:
                streak = 1

            previous_rating = rating

            distributed_candies += max(streak, ascending_candies_weight[right_pointer])
            right_pointer -= 1

        return distributed_candies


if __name__ == '__main__':
    # print(Solution().candy([5, 2, 5, 3, 1, 3, 5, 3, 5, 2, 1, 5, 5, 4, 23]))
    # print(Solution().candy([1,2,2]))
    print(Solution().candy([1,0,2]))