class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        head = 0
        while(head < len(nums)):
            tail = head + 1;
            while tail < len(nums):
                if nums[head] + nums[tail] == target:
                    return [head, tail]
                tail += 1
            head += 1
        return None

