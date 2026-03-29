class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapper = defaultdict(int)

        left = 0
        right = 0
        answer = 0
        for right in range(len(fruits)):
            mapper[fruits[right]] += 1
            while len(mapper) > 2:
                mapper[fruits[left]] -= 1
                if mapper[fruits[left]] == 0:
                    mapper.pop(fruits[left])
                left += 1
            answer = max(answer, right - left + 1)
        
        return answer
                    
