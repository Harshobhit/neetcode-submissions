class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_numeric_str = re.findall(r'\w', s)
        alpha_numeric_str = [char.lower() for char in alpha_numeric_str]
        return alpha_numeric_str == alpha_numeric_str[::-1]
