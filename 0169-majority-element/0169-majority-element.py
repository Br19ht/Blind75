class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        res, occurrence = 0, 0

        for i in nums:
            if occurrence == 0:
                res = i
            
            if res == i:
                occurrence += 1
            else:
                occurrence -= 1
        
        return res
