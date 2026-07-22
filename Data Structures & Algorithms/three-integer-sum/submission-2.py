class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for x, num in enumerate(nums):
            if x > 0 and num == nums[x - 1]: continue
            head = x + 1
            tail = len(nums) - 1
            while head < tail:
                diff = nums[head] + nums[tail]
                if diff == -num: 
                    output.append([num, nums[head], nums[tail]])
                    head += 1
                    tail -= 1
                    while head < tail and nums[head] == nums[head - 1]: head +=1
                    while head < tail and nums[tail] == nums[tail + 1]: tail -=1
                elif diff < -num: head += 1
                else: tail -= 1
        return(output)

                    


        