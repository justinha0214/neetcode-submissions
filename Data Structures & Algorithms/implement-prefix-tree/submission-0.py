class PrefixTree:

    def __init__(self):
        self.words = [[]] * 26 # 26 lowercase letters

    def insert(self, word: str) -> None:
        c = ord("a") - ord(word[0])
        self.words[c].append(word)

    def search(self, word: str) -> bool:
        c = ord("a") - ord(word[0])     
        if word in self.words[c]:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        c = ord("a") - ord(prefix[0])
        pLen = len(prefix) 
        for s in self.words[c]:
            if pLen <= len(s) and prefix == s[:pLen]:
                return True
        return False

        
        