from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = {}

        for city, connected_cities in enumerate(isConnected):
            graph[city] = {idx for idx, is_connected in enumerate(connected_cities)
                           if is_connected}

        provinces_count = 0

        for city in range(len(isConnected)):

            if city in graph:
                connected_cities = graph.pop(city)

                while connected_cities:
                    connected_city = connected_cities.pop()

                    if connected_city in graph:
                        connected_cities |= graph.pop(connected_city)

                provinces_count += 1

        return provinces_count

if __name__ == '__main__':
    print(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
