class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in hashmap:
                    hashmap[s[i]] = 1
                else:
                    hashmap[s[i]] += 1
            
            for c in t:
                if c not in hashmap:
                    return False
                else:
                    hashmap[c] -= 1
                    if hashmap[c] < 0:
                        return False
                
            return True
                