class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        gap = 1
    
        for i in range(len(temperatures)):
            while (i + gap < len(temperatures)):
                if temperatures[i + gap] > temperatures[i]:
                    result[i] = gap
                    break
                gap += 1
            gap = 1

        return result