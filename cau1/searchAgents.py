import fringes
from problem import SingleFoodSearchProblem
class searchAgents(SingleFoodSearchProblem):
    def BFS(self, m:SingleFoodSearchProblem) -> list:
        actions=[]
        # TODO
        
        return actions
    def DFS(self, m:SingleFoodSearchProblem) -> list:
        actions=[]
        #TODO
        return actions
    def UCS(self, m:SingleFoodSearchProblem) -> list:
        actions=[]
        #TODO
        return actions
SFSP=SingleFoodSearchProblem()
SFSP.load_from_file('sample_inputs/pacman_single01.txt')
searcher=searchAgents()
print(searcher.BFS(SFSP))