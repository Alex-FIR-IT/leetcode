from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start_indexes = {}
        max_fruits_count = 0
        current_fruits_count = 0
        previous_fruit = None

        for index, fruit in enumerate(fruits):
            if fruit in start_indexes or len(start_indexes) < 2:
                current_fruits_count += 1
            else:
                last_fruit_in_sequence, last_fruit_index = max(
                    start_indexes.popitem(),
                    start_indexes.popitem(),
                    key=lambda x: x[-1]
                )

                start_indexes[last_fruit_in_sequence] = last_fruit_index
                current_fruits_count = index - last_fruit_index + 1

            if previous_fruit != fruit:
                start_indexes[fruit] = index

            previous_fruit = fruit
            max_fruits_count = max(max_fruits_count, current_fruits_count)

        return max_fruits_count


print(Solution().totalFruit([1, 1, 2, 3, 2, 3, 3, 3, 2, 2, 4, 4, 4, 4, 4, 3, 3, 2, 2, 2]))