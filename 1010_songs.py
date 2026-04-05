class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mapper = defaultdict(int)
        answer = 0
        for times in time:
            complement = times % 60
            if (60 - complement) % 60 in mapper:
                needed = (60 - complement) % 60

                answer += mapper[needed]
                
            mapper[complement] += 1
        

        return answer
