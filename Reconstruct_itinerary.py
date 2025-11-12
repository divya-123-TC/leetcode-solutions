from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Build graph: departure → list of arrivals
        graph = defaultdict(list)
        # Sort tickets in reverse lex order so that we can pop from end and get smallest lex
        for frm, to in sorted(tickets, reverse=True):
            graph[frm].append(to)

        result = []
        def dfs(current: str):
            # while there are outgoing flights from current
            while graph[current]:
                next_airport = graph[current].pop()  # pop the last, which is lex smallest
                dfs(next_airport)
            # no more outgoing edges from current, add to result
            result.append(current)

        # Start from "JFK"
        dfs("JFK")
        # result is built in reverse order
        return result[::-1]