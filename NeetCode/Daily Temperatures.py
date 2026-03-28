class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                stackI, stackT = stack.pop()
                results[stackI] = index - stackI
            stack.append((index,temperature))
        return results