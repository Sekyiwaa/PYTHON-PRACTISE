class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        left = 0
        right = len(s) -1
        answer = list(s)
        lent = len(s)

        while left < right:
            while left < right and answer[left] not in vowels:
                left += 1

            while left < right and answer[right] not in vowels:
                right -= 1
            
            if answer[left] in vowels and answer[right] in vowels:
                answer[left], answer[right] = answer[right], answer[left]
                left += 1
                right -= 1
          
            

        return ''.join(answer)
