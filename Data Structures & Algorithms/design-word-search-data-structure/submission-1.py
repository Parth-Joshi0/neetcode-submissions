class WordDictionary:

    def __init__(self):
        self.nodes = [None] * 26
        self.end = False

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            if not node.nodes[self.get_index(c)]:
                node.nodes[self.get_index(c)] = WordDictionary()
            node = node.nodes[self.get_index(c)]
        node.end = True

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.end
        char = self.get_index(word[0])
        if word[0] != '.':
            if not self.nodes[char]:
                return False
            else:
                return self.nodes[char].search(word[1:])
        else:
            for node in self.nodes:
                if not node:
                    continue
                output = node.search(word[1:])
                if output == True:
                    return True
            return False

    def get_index(self, char):
        return ord(char) - ord('a')
