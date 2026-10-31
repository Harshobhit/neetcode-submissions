class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result_set = set()
        curr_hash_map = set()
        left, right = 0, 0

        while right < len(s):
            if s[right] in curr_hash_map:
                result_set.add(s[left:right])
                curr_hash_map = set()
                left = right
            else:
                curr_hash_map.add(s[right])
                right += 1

        if curr_hash_map:#In case if all are unique curr_hash_map will go on adding til last
            result_set.add(s[left:right])
        
        max_len = 0
        for sub_str in result_set:
                max_len = max(len(sub_str), max_len)

        return max_len               
            