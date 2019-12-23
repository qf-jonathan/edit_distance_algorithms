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
        st, similar = [(0, 0, 0, '')], {}
        while st:
            p, index, tol, curr = st.pop()
            if p == len(word):
                if self.trie[index][0]:
                    similar[curr] = True
            if p < len(word):
                if word[p] in self.trie[index][1]:
                    st.append((p + 1, self.trie[index][1][word[p]], tol, curr + word[p]))
                if tol < tolerance:
                    st.append((p + 1, index, tol + 1, curr))
                    for c, ind in self.trie[index][1].items():
                        st.append((p + 1, ind, tol + 1, curr + c))
            if tol < tolerance:
                for c, ind in self.trie[index][1].items():
                    st.append((p, ind, tol + 1, curr + c))
        return similar.keys()
