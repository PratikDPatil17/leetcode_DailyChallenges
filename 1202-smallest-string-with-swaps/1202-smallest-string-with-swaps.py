class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N=len(s)
        DSU=UnionFind(N)
        for x,y in pairs:
            DSU.union(x,y)
        
        parent_mapping = {i:DSU.find(i) for i in range(N)}
        
        components=defaultdict(list)
        for i in range(N):
            components[parent_mapping[i]].append(i)
                
        s_list = list(s)
        for _, component in components.items():
            component.sort()
            component_char = [s_list[index] for index in component]
            component_char.sort()

            for index, char in zip(component, component_char):
                s_list[index] = char

        return "".join(s_list)