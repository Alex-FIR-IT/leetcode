from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(set)
        prices = {}

        for vars, value in zip(equations, values):
            graph[vars[0]].add(vars[1])
            prices[vars[0], vars[1]] = value

            graph[vars[1]].add(vars[0])
            prices[(vars[1], vars[0])] = 1 / value

        output = []

        for query in queries:
            a, b = query

            if a in graph and b in graph:
                price = 1
                cur_var = a
                stack = deque([(price, cur_var)])
                checked = set()

                while stack and cur_var != b:
                    price, cur_var = stack.popleft()

                    if cur_var in checked:
                        continue

                    checked.add(cur_var)

                    for next_var in graph[cur_var]:
                        price_to_next_var = prices.get((cur_var, next_var))
                        if prices.get((cur_var, next_var)):

                            new_relation_price = price * price_to_next_var
                            stack.append((new_relation_price, next_var))
                            graph[a].add(next_var)
                            prices[(a, next_var)] = new_relation_price

                if cur_var != b:
                    price = -1

            else:
                price = -1

            output.append(price)

        return output
