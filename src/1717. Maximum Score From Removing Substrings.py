from typing import Union, List


class Solution:

    @staticmethod
    def _delete_substring(
            *,
            symbols: Union[str, List],
            sub_string: str,
            removal_score: int,
            score: int,
    ):

        current_symbols: List[str] = [symbols[0]]

        for right_pointer in range(1, len(symbols)):
            right_symbol = symbols[right_pointer]
            if not current_symbols:
                current_symbols.append(right_symbol)
                continue

            left_symbol = current_symbols[-1]

            if f"{left_symbol}{right_symbol}" == sub_string:
                current_symbols.pop()
                score += removal_score
            else:
                current_symbols.append(right_symbol)

        return current_symbols, score

    def maximumGain(self, string_: str, ab_score: int, ba_score: int) -> int:
        score = 0

        removal_options = (
            {
                'removal_score': ab_score,
                'sub_string': 'ab'
            },
            {
                'removal_score': ba_score,
                'sub_string': 'ba'
            }
        )

        actions = sorted(removal_options, key=lambda option: -option['removal_score'])

        for removal_action in actions:
            if not string_:
                break

            string_, score = self._delete_substring(
                symbols=string_,
                sub_string=removal_action['sub_string'],
                removal_score=removal_action['removal_score'],
                score=score
            )

        return score


if __name__ == '__main__':
    print(Solution().maximumGain("cdbcbbaaabab", 4, 5))
