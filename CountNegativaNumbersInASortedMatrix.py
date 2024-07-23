class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negativeCount = 0
        for row in grid:
            for num in row:
                if num < 0:
                    negativeCount += 1
        return negativeCount
'''
status: Accepted
Runtime: 106 ms
problem: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/?envType=study-plan-v2&envId=binary-search
'''