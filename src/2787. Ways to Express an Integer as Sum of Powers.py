from typing import List

class Solution:
    MODULO = 10**9 + 7

    def numberOfWays(self, target_sum: int, exponent: int) -> int:
        # Собираем все степени i^exponent <= targetsum
        power_values: List[int] = []
        base = 1
        while True:
            power_value = pow(base, exponent)
            if power_value > target_sum:
                break
            power_values.append(power_value)
            base += 1

        # dp[s] = количество способов получить сумму s
        dp: List[int] = [0] * (target_sum + 1)
        dp[0] = 1
        # Для каждого значения обновляем dp по убыванию, чтобы элемент использовался не более одного раза
        for value in power_values:
            for current_sum in range(target_sum, value - 1, -1):
                dp[current_sum] = (dp[current_sum] + dp[current_sum - value])

        return dp[target_sum]

if __name__ == '__main__':
    print(Solution().numberOfWays(10, 2))