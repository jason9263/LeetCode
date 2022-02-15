class Solution:
    def countVowels(self, word: str) -> int:
        dp = [0] * (len(word))
        vowels = "aeiou"
        if word[0] in vowels:
            dp[0] = 1

        for i in range(1, len(word)):
            if word[i] in vowels:
                dp[i] = dp[i - 1] + (i + 1)
            else:
                dp[i] = dp[i - 1] 

        return sum(dp)
