class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = {}
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):
            # 1. Use s[right] (character) as key, not right (index)
            char_set[s[right]] = char_set.get(s[right], 0) + 1
            
            # Track the max frequency in the current window
            max_freq = max(max_freq, char_set[s[right]])

            # 2. Window length is (right - left + 1)
            # If replacements needed > k, shrink window from left
            while (right - left + 1) - max_freq > k:
                char_set[s[left]] -= 1
                left += 1

            # Update max valid window length seen so far
            result = max(result, right - left + 1)

        return result