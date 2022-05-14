class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network={}
        for u,v,time in times:
            if u not in network:
                network[u]=[]
            network[u].append((time,v))
        
        import heapq as hp
        
        visited=set()
        summits_delay=[(0,k)]
        max_delay=0
        
        while summits_delay:
            curr_delay,curr_summit=hp.heappop(summits_delay)
            if curr_summit in visited:
                continue
                
            visited.add(curr_summit)
            max_delay=curr_delay
            
            if curr_summit in network:
                for time,next_summit in network[curr_summit]:
                    if next_summit in visited:
                        continue
                    hp.heappush(summits_delay,(curr_delay+time,next_summit))
                    
        return max_delay if len(visited)==n else -1