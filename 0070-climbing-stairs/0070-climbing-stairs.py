class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        total = 0

        if n == 1:
            return 1

        for i in range(n-1):
            total = one + two
            two = one
            one = total
        
        return total