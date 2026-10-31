class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash_map = {}
        for char in s1:
            s1_hash_map[char] = 1 + s1_hash_map.get(char, 0)
        
        for i in range(len(s2)):
            curr_hash_map = {}
            count = 0
            for j in range(i, len(s2)):
                curr_hash_map[s2[j]] = 1 + curr_hash_map.get(s2[j], 0)

                if curr_hash_map[s2[j]] > s1_hash_map.get(s2[j], 0): #In case if char hash map does not match with s1
                    break
                
                if curr_hash_map[s2[j]] == s1_hash_map[s2[j]]: #If hashmap of char matches with s1 then increase count
                    count += 1
                
                if count == len(s1): #if we get the required chars in cur_hash_map as seen is s1 then we found it.
                    return True
        
        return False