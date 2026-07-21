class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1
        while head < tail:
            diff = numbers[head] + numbers[tail]
            if  diff == target:
                return [head + 1, tail + 1]
            elif diff < target:
                head += 1
            else:
                tail -= 1
        head += 1
            