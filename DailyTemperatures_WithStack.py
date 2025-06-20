class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Brute Force Approch
        #Time Complexity O(N^2)
        # n = len(temperatures)
        # result = [0] * n
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = j - i
        #             break
        # return result
        
        # Optimze approch, Using stack
        #Time Complexity O(N)
        #Space COmplexity O(N)
        n = len(temperatures)
        result = [0] * n
        stack = [] #Pair [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndx = stack.pop()
                result[stackIndx] = (i - stackIndx)
            stack.append([t, i])
        
        return result