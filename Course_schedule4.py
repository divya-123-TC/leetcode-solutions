class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        # step 1: create matrix
        isPre = [[False] * numCourses for _ in range(numCourses)]

        # step 2: mark direct prerequisites
        for a, b in prerequisites:
            isPre[a][b] = True

        # step 3: Floyd–Warshall style
        for k in range(numCourses):
            for i in range(numCourses):
                if isPre[i][k]:                # i → k is true
                    for j in range(numCourses):
                        if isPre[k][j]:        # k → j is true
                            isPre[i][j] = True # so i → j becomes true

        # step 4: answer queries
        ans = []
        for u, v in queries:
            ans.append(isPre[u][v])
        
        return ans