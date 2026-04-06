class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1
        
        answer = 0
        for key in freq.keys():
            remainder = freq[key] % 2
            answer += freq[key] - remainder
            freq[key] -= freq[key] - remainder

        for key in freq.keys():
            if freq[key] == 1:
                answer += 1
                break

        return answer
