class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = defaultdict(set)
        wordList = set(wordList)
        wordList.add(beginWord)
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for word in wordList:
            for i in range(len(word)):
                for letter in alphabet:
                    new_word = word[:i] + letter + word[i+1:]
                    if new_word in wordList and new_word != word:
                        adjList[word].add(new_word)
        
        
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, count = queue.popleft()

            if word == endWord:
                return count

            for neighbor in adjList[word]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, count + 1))

        return 0
                
