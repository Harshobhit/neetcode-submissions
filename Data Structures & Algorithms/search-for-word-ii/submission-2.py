class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False

    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.add_word(word)
        
        rows, cols = len(board), len(board[0])
        visited, result = set(), set()

        def traverse(node, row, col, word_till_now):
            if  row < 0 or\
                col < 0 or\
                row >= rows or\
                col >= cols or\
                (row, col) in visited or\
                board[row][col] not in node.children:
                
                return
            
            visited.add((row, col))
            node = node.children[board[row][col]]
            word_till_now += board[row][col]
            if node.isWord:
                result.add(word_till_now)
            
            traverse(node, row+1, col, word_till_now)
            traverse(node, row-1, col, word_till_now)
            traverse(node, row, col+1, word_till_now)
            traverse(node, row, col-1, word_till_now)
            visited.remove((row, col))
        
        for row in range(rows):
            for col in range(cols):
                traverse(root, row, col, "")

        return list(result)
