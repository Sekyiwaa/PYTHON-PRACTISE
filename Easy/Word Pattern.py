class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the string into words
        lst = s.split()
        
        # Check length mismatch
        if len(pattern) != len(lst):
            return False
        
        # Check unique counts of characters and words
        if len(set(pattern)) != len(set(lst)):
            return False
        
        # Create a mapping dictionary
        ref = {}
        for i in range(len(pattern)):
            if pattern[i] not in ref:
                ref[pattern[i]] = lst[i]
            elif ref[pattern[i]] != lst[i]:
                return False
        
        return True        