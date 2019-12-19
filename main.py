from bktree import BKTree as IBKTree
from iterative_bktree import BKTree
from brute_force_distance import BruteForceDistance
from tries_dist import TrieDist
import time


def main():
    tree_a = BKTree()
    tree_b = IBKTree()
    tree_c = BruteForceDistance()
    tree_d = TrieDist()
    with open('spanish.txt', encoding='utf8') as spanish:
        list_words = [wd.rstrip('\n').lower() for wd in spanish.readlines()]

        def insert_test(tree, name):
            start_time = time.time()
            cnt = 1
            for wd in list_words:
                tree.add(wd)
                print('\r[{}] [{:.2f}%]'.format(name, cnt / len(list_words) * 100), end='')
                cnt += 1
            print(' [{:.8f}s]'.format(time.time() - start_time))

        insert_test(tree_a, 'recursive bktree')
        insert_test(tree_b, 'iterative bktree')
        insert_test(tree_c, 'brute force dist')
        insert_test(tree_d, 'trie ds approach')
    print(' --- ', end='')

    while True:
        word = input('\nword: ').lower()

        def test_query_similar(tree, name):
            start_time = time.time()
            similar = tree.get_similar(word, 2)
            total_time = time.time() - start_time
            print('[{}, {:.8f}s] = [{}]'.format(name, total_time, ', '.join(sorted(similar))))

        test_query_similar(tree_a, 'recursive bktree')
        test_query_similar(tree_b, 'iterative bktree')
        test_query_similar(tree_c, 'brute force dist')
        test_query_similar(tree_d, 'trie ds approach')


if __name__ == '__main__':
    main()
