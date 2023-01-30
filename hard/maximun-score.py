# Problem: https://leetcode.com/problems/maximum-score-words-formed-by-letters/submissions/876874922/

import string
from collections import Counter
from itertools import chain, combinations


class Solution(object):
    def maxScoreWords(self, words, letters, score):
        score_dict = { letter:letter_score for letter, letter_score in zip(list(string.ascii_lowercase), score) }
        letters_repetition = Counter(letters)

        combinacoes = list(chain.from_iterable(combinations(words, r) for r in range(len(words) + 1)))

        final_score = 0
        for combinacao in combinacoes:
            combinacao_repeticoes = Counter((list(''.join(combinacao))))
            valid = True
            for key, value in combinacao_repeticoes.items():
                if value > letters_repetition[key]:
                    valid = False
            if valid:
                comb_score = sum([score_dict[char] for char in ''.join(combinacao)])
                if (comb_score > final_score):
                    final_score = comb_score

        return final_score
