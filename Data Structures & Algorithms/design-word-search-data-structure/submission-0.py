class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def search_trie(curr, index):
            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if search_trie(child, i+1):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word
        
        return search_trie(self.root, 0)