from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        not_visited_rooms = set(range(1, len(rooms)))
        keys = set(rooms[0])

        while keys:
            key = keys.pop()

            if key in not_visited_rooms:
                not_visited_rooms.remove(key)
                keys.update(rooms[key])

        return not not_visited_rooms


if __name__ == '__main__':
    print(Solution().canVisitAllRooms([[1], [2], [3], []]))