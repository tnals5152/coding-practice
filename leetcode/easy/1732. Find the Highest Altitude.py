class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        before = 0
        max_altitude = 0
        
        for g in gain:
            before += g
            max_altitude = max(max_altitude, before)
        
        return max_altitude
        
