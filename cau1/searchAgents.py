import fringes
from problem import SingleFoodSearchProblem
class searchAgents(SingleFoodSearchProblem):
    def BFS(self, m:SingleFoodSearchProblem) -> list:
        pacman_state=m.P
        queue=fringes.Queue()
        queue.enQueue((pacman_state,[]))
        cost=0
        visited=[]
        while(queue.empty()!=True and cost<20):
            state,path=queue.deQueue()
            if m.goal_test(state)==True:
                return path
            successor=m.getSuccessor(state)
            for new_state, action in successor:
                if new_state not in visited:
                    visited.append(new_state)
                    queue.enQueue((new_state,path+[action]))
        return path
    def DFS(self, m:SingleFoodSearchProblem) -> list:
        pacman_state=m.P
        stack=fringes.Stack()
        stack.push((pacman_state,[]))
        cost=0
        visited=[]
        while(stack.empty()!=True and cost<20):
            state,path=stack.pop()
            if m.goal_test(state)==True:
                return path
            successor=m.getSuccessor(state)
            for new_state, action in successor:
                if new_state not in visited:
                    visited.append(new_state)
                    stack.push((new_state,path+[action]))
        return path
    def UCS(self, m:SingleFoodSearchProblem) -> list:
        actions=[]
        #TODO
        return actions
SFSP=SingleFoodSearchProblem()
SFSP.load_from_file('sample_inputs/pacman_single01.txt')
searcher=searchAgents()
path=searcher.BFS(SFSP)
print(path)
# SFSP.animate(path)