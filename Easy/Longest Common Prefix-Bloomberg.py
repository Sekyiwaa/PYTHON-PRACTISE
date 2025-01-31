class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        ans = ""
        strs.sort()  # Sort the list of strings
        first = strs[0]  # First string (smallest in lexicographical order)
        last = strs[-1]  # Last string (largest in lexicographical order)

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:  # Stop when characters don't match
                return ans
            ans += first[i]

        return ans
