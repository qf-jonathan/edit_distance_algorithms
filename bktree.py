from utils import edit_distance


class BKTree:
    def __init__(self):
        self.tree = [['', {}]]

    def add(self, word):
        def recursive_add(tree, index):
            if tree[index][0] == '':
                tree[index][0] = word
            else:
                distance = edit_distance(tree[index][0], word)
                if distance != 0:
                    if distance not in tree[index][1]:
                        tree[index][1][distance] = len(tree)
                        tree.append(['', {}])
                    recursive_add(tree, tree[index][1][distance])

        recursive_add(self.tree, 0)

    def get_similar(self, word, tolerance):
        similar = []

        def recursive_get_similar(tree, index):
            distance = edit_distance(tree[index][0], word)
            if distance <= tolerance:
                similar.append(tree[index][0])
            for i in range(distance - tolerance, distance + tolerance + 1):
                if i in tree[index][1]:
                    recursive_get_similar(tree, tree[index][1][i])

        recursive_get_similar(self.tree, 0)
        return similar
