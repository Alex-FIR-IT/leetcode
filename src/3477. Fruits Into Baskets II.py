from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced_fruits_count = 0
        filled_baskets = set()

        for fruit in fruits:
            for basket_index, basket in enumerate(baskets):
                if basket >= fruit and basket_index not in filled_baskets:
                    filled_baskets.add(basket_index)
                    break
            else:
                unplaced_fruits_count += 1

        return unplaced_fruits_count
