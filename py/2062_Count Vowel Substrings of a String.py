from typing import DefaultDict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if (len(word) < 5):
            return 0
        count = 0
        vowels = "aeiou"
        for i in range(0, len(word) - 4):
            current = set()
            if word[i] in vowels:
                current.add(word[i])

                for j in range(i + 1, len(word)):
                    if word[j] in vowels:
                        current.add(word[j])
                    else:
                        break

                    if len(current) == 5:
                        count += 1

        return count


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if len(word) < 5:
            return 0
        count = 0
        vowels = "aeiou"
        l = r = 0
        freq = DefaultDict(int)

        for i in range(len(word)):
            if word[i] in vowels:
                if not i or word[i-1] not in vowels:
                    l = r = i
                    freq.clear()
                freq[word[i]] += 1

                while len(freq) == 5 and all(freq.values()):
                    freq[word[r]] -= 1
                    r += 1
                count += r - l
        return count
