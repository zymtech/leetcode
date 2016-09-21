import collections

class Solution(object):
    def findSubstring(self, s, words):
        ret = []
        memo, step = collections.defaultdict(int), len(words[0])
        for i in words:
            memo[i] += 1
        for i in range(len(s) - len(words)*step + 1):
            curr, j = collections.defaultdict(int), 0
            while j < len(words):
                word = s[i + j*step:i + j*step + step]
                if word not in memo:
                    break
                curr[word] += 1
                if curr[word] > memo[word]:
                    break
                j += 1
            if j == len(words):
                ret.append(i)
        return ret


if __name__ == "__main__":
    s = "barfoothebarfooman"
    words = ['foo','bar']
    print Solution().findSubstring(s,words)