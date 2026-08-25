class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position, speed)]
        # create pairings for each car's starting position and speed

        stack = [] # create a stack and traverse in greater -> less order
        for p, s in sorted(pairs, reverse=True):
            stack.append((target - p) / s) # add the 'time' of the car
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # check if the curr car is faster
                stack.pop() # pop if so because that means they met and combined to be a fleet
        return len(stack)