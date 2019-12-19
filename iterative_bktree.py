from utils import edit_distance


class BKTree:
    def __init__(self):
        self.tree = [['', {}]]

    def add(self, word):
        index = 0
        while self.tree[index][0] != '':
            distance = edit_distance(self.tree[index][0], word)
            if distance == 0:
                return
            if distance not in self.tree[index][1]:
                self.tree[index][1][distance] = len(self.tree)
                self.tree.append(['', {}])
            index = self.tree[index][1][distance]
        self.tree[index][0] = word

    def get_similar(self, word, tolerance):
        similar, st = [], [0]
        while st:
            index = st.pop()
            distance = edit_distance(self.tree[index][0], word)
            if distance <= tolerance:
                similar.append(self.tree[index][0])
            for i in range(distance - tolerance, distance + tolerance + 1):
                if i in self.tree[index][1]:
                    st.append(self.tree[index][1][i])
        return similar
