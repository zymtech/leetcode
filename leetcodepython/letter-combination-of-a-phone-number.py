# -*- coding: utf-8 -*-

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return []

        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", \
                          "pqrs", "tuv", "wxyz"], [""]

        for digit in reversed(digits):
            choices = lookup[int(digit)]
            m, n = len(choices), len(result)
            result += [result[i % n] for i in xrange(n, m * n)]

            for i in xrange(m * n):
                result[i] = choices[i / n] + result[i]

        return result

if __name__ == "__main__":
    print Solution().letterCombinations("23")