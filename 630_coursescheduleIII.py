class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []

        def diddy(key):
            return key[1]

        courses.sort(key=diddy)
        

        time = 0
        for i in range(len(courses)):
            if courses[i][0] + time <= courses[i][1]:
                time += courses[i][0]
                heapq.heappush(heap, -courses[i][0])
            elif heap and time > time - (-heap[0]) + courses[i][0]:
                course = heapq.heappop(heap)
                time -= (-course)
                time += courses[i][0]
                heapq.heappush(heap, -courses[i][0])

                
        return len(heap)
