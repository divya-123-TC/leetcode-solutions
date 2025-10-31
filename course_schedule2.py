class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for course,pre in prerequisites:
            graph[pre].append(course)
        visited={}
        order=[]
        def dfs(course):
            if visited.get(course)==1:
                return False
            if visited.get(course)==2:
                return True
            visited[course]=1
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited[course]=2
            order.append(course)
            return True
        for course in range (numCourses):
            if not dfs(course):
                return []
        return  order[::-1]
