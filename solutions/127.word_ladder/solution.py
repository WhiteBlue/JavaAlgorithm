from typing import List


def is_between(a, b):
    diff = False
    for i in range(len(a)):
        if a[i] != b[i]:
            if diff:
                return False
            diff = True
    return diff


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        edge_map = dict()
        alphabets = set()
        words = set()

        edge_map[beginWord] = set()
        for word in wordList:
            edge_map[word] = set()
            if is_between(beginWord, word):
                edge_map[beginWord].add(word)
                edge_map[word].add(beginWord)

        for w in wordList:
            for c in w:
                alphabets.add(c)
            words.add(w)

        for w in wordList:
            for i in range(len(w)):
                for c in alphabets:
                    if w[i] == c:
                        continue
                    new_word = w[:i] + c + w[i + 1:]
                    if new_word in words:
                        edge_map[w].add(new_word)
                        edge_map[new_word].add(w)

        line = [beginWord]
        next_line = []
        visited = set()

        step = 1
        while len(line) > 0:
            for word in line:
                visited.add(word)
                for target in filter(lambda x: x not in visited, edge_map[word]):
                    if target == endWord:
                        return step + 1
                    next_line.append(target)
            line, next_line = next_line, line
            next_line.clear()
            step += 1

        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
