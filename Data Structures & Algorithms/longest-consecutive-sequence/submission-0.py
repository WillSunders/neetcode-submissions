class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = {}
        for num in nums:
            numbers[num] = 1
        maxcount = 0
        for num in nums:
            count = 0
            while(numbers.get(num + count)): 
                count += 1
                maxcount = max(maxcount, count)
        return maxcount