class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ascii_sum_s = 0
        ascii_sum_t = 0
        for letter in s:
            ascii_sum_s += ord(letter)
        for letter in t:
            ascii_sum_t += ord(letter)
        return ascii_sum_s == ascii_sum_t
    
        