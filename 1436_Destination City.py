from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = {}
        for allpath in paths:
            city1, city2 = allpath
            cities[city1] = cities.get(city1, 0) + 1
            cities[city2] = cities.get(city2, 0)

        for i in cities:
            if cities[i] == 0:
                return i

output = Solution()
print(output.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])) # Sao Paulo