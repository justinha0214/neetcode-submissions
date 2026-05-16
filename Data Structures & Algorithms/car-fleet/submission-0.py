class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # MOST IMPORTANT THING TO KNOW ABOUT THIS PROBLEM!!!
        # ARRIVAL TIME = (TARGET - POSITION) / SPEED
        # Can use stack like NeetCode, or just track slowest time! 
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for pos, speed in sorted(pairs, reverse=True):
            stack.append((target - pos) / speed)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)