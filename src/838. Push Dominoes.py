class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        main_points = []
        final_state = list(dominoes)

        for index, domino in enumerate(dominoes):
            if domino in ("R", 'L'):
                main_points.append((index, domino))

        if not main_points:
            return dominoes

        if main_points[0][-1] == 'L':
            for index in range(main_points[0][0]):
                final_state[index] = 'L'

        previous_point = None

        for current_point in main_points:
            if previous_point:
                if previous_point[-1] == current_point[-1]:
                    for index in range(previous_point[0], current_point[0] + 1):
                        final_state[index] = current_point[-1]
                elif previous_point[-1] == 'R':
                    left_pointer = previous_point[0]
                    right_pointer = current_point[0]

                    while left_pointer < right_pointer:
                        final_state[left_pointer] = 'R'
                        final_state[right_pointer] = 'L'

                        left_pointer += 1
                        right_pointer -= 1
                else:
                    pass

            previous_point = current_point

        if main_points[-1][-1] == 'R':
            for index in range(main_points[-1][0] + 1, len(dominoes)):
                final_state[index] = 'R'

        return ''.join(final_state)


if __name__ == '__main__':
    print(Solution().pushDominoes("..L..R.L.R.."))