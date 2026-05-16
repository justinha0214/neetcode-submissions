class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # MOST IMPORTANT THING TO KNOW ABOUT THIS PROBLEM!!!
        # ARRIVAL TIME = (TARGET - POSITION) / SPEED

        # Use slowest speed to determine fleet count
        pairs = [[p, s] for p, s in zip(position, speed)]
        fleet = currTime = 0 # currTime = 0 bcuz no car should reach destination at t=0

        for pos, speed in sorted(pairs, reverse=True):
            destTime = (target - pos) / speed 
            if currTime < destTime:
                fleet += 1
                currTime = destTime
                
        return fleet 