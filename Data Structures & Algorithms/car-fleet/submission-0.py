class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # tuple car position and speed and make into one list
        pair = [(p, s) for p, s in zip(position, speed)]
        # sort in descending order (pos)
        pair.sort(reverse = True)
        # make stack
        stack = []
        # for every pos, spd in tuple, compute time to reach target
        # push time to stack
        # if new car time <= to time before it, it will catch up
        # and become part of the fleet. pop it.
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        # num of remaining times in stack is the # of fleets
        # return that num
        return len(stack)