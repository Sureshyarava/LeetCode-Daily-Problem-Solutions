class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = dict()

        def rank_of(word, tree):
            rank = 0
            for i in word:
                rank+=tree[i]['count']
                tree = tree[i]
            return rank

        def fit(word, tree):
            for i in word:
                if i not in tree:
                    tree[i] = dict()
                    tree[i]["count"] = 1
                else:
                    tree[i]['count']+=1
                tree = tree[i]

        for word in words:
            fit(word, trie)
        
        res = []
        for word in words:
            res.append(rank_of(word, trie))
        return res
