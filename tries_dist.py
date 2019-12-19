class TrieDist:
    def __init__(self):
        self.trie = [[False, {}]]

    def add(self, word):
        index = 0
        for c in word:
            if c not in self.trie[index][1]:
                self.trie[index][1][c] = len(self.trie)
                self.trie.append([False, {}])
            index = self.trie[index][1][c]
        self.trie[index][0] = True

    def get_similar(self, word, tolerance):
        similar = {}

        def recursive_get_similar(p, index, tol, curr, trie):
            if p == len(word):
                if trie[index][0]:
                    similar[curr] = True
                if tol > 0:
                    for c, ind in trie[index][1].items():
                        recursive_get_similar(p, ind, tol - 1, curr + c, trie)
            else:
                if word[p] in trie[index][1]:
                    recursive_get_similar(p + 1, trie[index][1][word[p]], tol, curr + word[p], trie)
                if tol > 0:
                    recursive_get_similar(p + 1, index, tol - 1, curr, trie)
                    for c, ind in trie[index][1].items():
                        recursive_get_similar(p, ind, tol - 1, curr + c, trie)
                        recursive_get_similar(p + 1, ind, tol - 1, curr + c, trie)

        recursive_get_similar(0, 0, tolerance, '', self.trie)
        return similar.keys()
