class Solution:
    def longestPalindrome(self, s: str) -> int:

        hashmap = {}
        result = 0

        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1
        
        for c in hashmap:
            result += hashmap[c] // 2 * 2
            if (result % 2 == 0 and hashmap[c] % 2 == 1):
                result += 1
        
        return result
