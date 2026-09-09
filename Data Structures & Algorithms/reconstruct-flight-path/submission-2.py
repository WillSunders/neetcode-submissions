class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for dep, des in sorted(tickets, reverse= True):
            adj[dep].append(des)

        stack, result = ["JFK"],[]
        while stack:
            while adj[stack[-1]]:
                stack.append(adj[stack[-1]].pop())
            result.append(stack.pop())
        return result[::-1]                