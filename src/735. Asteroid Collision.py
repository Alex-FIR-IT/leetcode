from typing import List
from itertools import islice


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        new_asteroids = [asteroids[0]]  # asteroids_after_collisions

        for asteroid in islice(asteroids, 1, None):
            new_asteroids.append(asteroid)

            while len(new_asteroids) > 1 and asteroid < 0 and new_asteroids[-2] > 0:
                if new_asteroids[-2] + asteroid > 0:
                    new_asteroids.pop()
                    break
                elif new_asteroids[-2] + asteroid < 0:
                    new_asteroids.pop(-2)
                else:
                    new_asteroids.pop()
                    new_asteroids.pop()
                    break

        return new_asteroids
