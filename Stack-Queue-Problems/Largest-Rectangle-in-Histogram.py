# <!-- question https://leetcode.com/problems/largest-rectangle-in-histogram/description/ 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        leftMin = [None] * n
        rightMin = [None] * n

        for i in range(0,n): 
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop() 

            if len(stack) == 0:
                leftMin[i] =0
            else:
                leftMin[i] = (stack[-1]+1)
            stack.append(i)
        
        while stack : stack.pop()
        for j in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[j]:
                stack.pop() 
            if len(stack) == 0:
                rightMin[j]=(n-1)
            else:
                rightMin[j] =(stack[-1]-1)
            stack.append(j)
        
        maxi = 0
        for i in range(0,n):
            maxi = max(maxi,(rightMin[i]-leftMin[i]+1) * heights[i])
        return maxi



                