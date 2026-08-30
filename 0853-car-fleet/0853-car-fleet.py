class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        last_time = 0
        
        for pos, spd in cars:
            # Force float conversion to prevent Python 2 integer truncation
            time = float(target - pos) / spd
            
            if time > last_time:
                fleets += 1
                last_time = time
                
        return fleets