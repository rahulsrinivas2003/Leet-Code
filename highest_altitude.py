class Solution:
    def largestAltitude(self, gain: List[int]) -> int:


        highest_altitude = 0 
        curr_altitude  = 0

        for gains in gain:

            curr_altitude += gains

            if curr_altitude > highest_altitude:

                highest_altitude = curr_altitude 
        
        return highest_altitude
        