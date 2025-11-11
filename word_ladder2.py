from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Build pattern dictionary OVER (wordSet ∪ {beginWord})
        pattern_map = defaultdict(list)
        all_words = wordSet | {beginWord}
        L = len(beginWord)
        for word in all_words:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        # 1) BFS: shortest distance from beginWord to every reachable word
        dist = {beginWord: 0}
        q = deque([beginWord])

        while q:
            w = q.popleft()
            d = dist[w]
            for i in range(L):
                pat = w[:i] + "*" + w[i+1:]
                for nei in pattern_map[pat]:
                    if nei not in dist:
                        dist[nei] = d + 1
                        q.append(nei)

        if endWord not in dist:
            return []

        # 2) DFS/backtrack from endWord → beginWord using dist map
        res, path = [], [endWord]

        def dfs(w: str):
            if w == beginWord:
                res.append(path[::-1])
                return
            d = dist[w]
            for i in range(L):
                pat = w[:i] + "*" + w[i+1:]
                for nei in pattern_map[pat]:
                    # only move to predecessors that are exactly one step closer
                    if nei in dist and dist[nei] == d - 1:
                        path.append(nei)
                        dfs(nei)
                        path.pop()

        dfs(endWord)
        return res