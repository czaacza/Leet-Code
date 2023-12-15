class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = {}
        for city_from, city_to in paths:
            if city_from not in graph:
                graph[city_from] = []
            if city_to not in graph:
                graph[city_to] = []
                
            graph[city_from].append(city_to)
            
        for city in graph:
            if len(graph[city]) == 0:
                return city
        