from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        current_altitude = 0

        for gain_point in gain:
            current_altitude += gain_point
            highest_altitude = max(highest_altitude, current_altitude)

        return highest_altitude
