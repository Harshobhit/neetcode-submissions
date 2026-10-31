class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
          return False
        
        freq_dict = {}
        for letter in s:
          if letter in freq_dict:
            freq_dict[letter] += 1
          else:
            freq_dict[letter] = 1
        
        for letter in t:
          if letter in freq_dict:
            freq_dict[letter] -= 1
        
        for letter, freq in freq_dict.items():
          if freq != 0:
            return False
        
        return True
