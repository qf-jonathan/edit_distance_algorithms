from utils import edit_distance


class BruteForceDistance:
    def __init__(self):
        self.words = []

    def add(self, word):
        self.words.append(word)

    def get_similar(self, word, tolerance):
        similar = []
        for wd in self.words:
            distance = edit_distance(wd, word)
            if distance <= tolerance:
                similar.append(wd)
        return similar
