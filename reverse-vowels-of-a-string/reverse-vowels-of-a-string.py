class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1 
        vowels = set(['a','e','i','o','u', 'A','E','I','O','U'])
        
        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                self.swap(s, left, right)
                left += 1 
                right -= 1 
                continue 
            
            if s[left] in vowels and not s[right] in vowels:
                right -= 1 
                continue 
            
            if not s[left] in vowels and s[right] in vowels: 
                left += 1 
                continue 
            
            left += 1 
            right -= 1 
        
        return ''.join(s)

    def swap(self, s, left, right):
        s[left], s[right] = s[right], s[left]
            