class Solution:
    def ascii_repr(self, input_str:List[str]):
        ascii_arr = [0]*26
        print(id(ascii_arr))
        for letter in input_str:
            ascii_arr[ord(letter.lower()) - ord('a')] += 1
        return ascii_arr

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for input_str in strs:
            ascii_rep = tuple(self.ascii_repr(input_str))
            if ascii_rep in hashmap:
                hashmap[ascii_rep].append(input_str)
            else:
                hashmap[ascii_rep] = [input_str]
        
        return list(hashmap.values())
        