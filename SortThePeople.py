class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nameHeight = list(zip(names, heights))# zip the names and heights
        sortedNameHeight = sorted(nameHeight, key=lambda x: x[1], reverse=True)# sort the names and heights
        sortedNames = [name for name, height in sortedNameHeight]# get the sorted names
        return sortedNames

'''
status: Accepted
Runtime: 42 ms
problem: https://leetcode.com/problems/sort-the-people/?envType=daily-question&envId=2024-07-22
'''
