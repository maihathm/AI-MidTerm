import fringes
from problems import SingleFoodSearchProblem,MultiFoodSearchProblem
import copy
class searchAgents:
    def EuclideanHeuristic(seft,state,goal_state:dict):
        row_s,col_s=[int(i) for i in state]
        heuristic=goal_state.copy()
        for i in goal_state:
            row_g,col_g=[int(j) for j in goal_state[i]]
            heuristic[i]=((row_g-row_s)**2+(col_g-col_s)**2)**0.5
        return min(heuristic.values())
    def ManhattanHeuristic(seft,state,goal_state:dict):
        row_s,col_s=[int(i) for i in state]
        heuristic=goal_state.copy()
        for i in goal_state:
            row_g,col_g=[int(j) for j in goal_state[i]]
            heuristic[i]=abs(row_g-row_s)+abs(col_g-col_s)
        return heuristic
    def BFS(self,g:SingleFoodSearchProblem or MultiFoodSearchProblem) -> list:
        m=copy.deepcopy(g)
        pacman_state=m.P
        queue=fringes.Queue()
        queue.enQueue((pacman_state,[]))
        visited=[]
        while not queue.empty():
            state,path=queue.deQueue()
            if m.goal_test(state):
                if len(m.F)<=1:
                    return path+['Stop']
                for i in m.F.copy():
                    if m.F[i]==state:
                        m.F.pop(i)
                        visited.clear()
                        queue.clear()
                        queue.enQueue((state,path))
                        break
            else:
                for new_state, action in m.get_successor(state):
                    if new_state not in visited:
                        visited.append(new_state)
                        queue.enQueue((new_state,path+[action]))
            print(queue.size())
        return []
    def DFS(self,g:SingleFoodSearchProblem or MultiFoodSearchProblem) -> list:
        m=copy.deepcopy(g)
        pacman_state=m.P
        stack=fringes.Stack()
        stack.push((pacman_state,[]))
        visited=[]
        while(stack.empty()!=True):
            state,path=stack.pop()
            if m.goal_test(state)==True:
                if len(m.F)<=1:
                    return path+['Stop']
                for i in m.F.copy():
                    if m.F[i]==state:
                        m.F.pop(i)
                        visited.clear()
                        stack.clear()
                        stack.push((state,path))
                        break
            else:
                for new_state, action in m.get_successor(state):
                    if new_state not in visited:
                        visited.append(new_state)
                        stack.push((new_state,path+[action]))
        return []
    def UCS(self,g:SingleFoodSearchProblem or MultiFoodSearchProblem) -> list:
        m=copy.deepcopy(g)
        pacman_state=m.P
        PriorityQueue=fringes.PriorityQueue(key=lambda x:x[2])
        PriorityQueue.enQueue((pacman_state,[],0))
        visited=[]
        while(PriorityQueue.empty()!=True):
            state,path,cost=PriorityQueue.deQueue()
            if m.goal_test(state)==True:
                if len(m.F)<=1:
                    return path+['Stop']
                for i in m.F.copy():
                    if m.F[i]==state:
                        m.F.pop(i)
                        visited.clear()
                        PriorityQueue.clear()
                        PriorityQueue.enQueue((state,path,m.path_cost(cost)))
                        break
            else:
                for new_state, action in m.get_successor(state):
                    if new_state not in visited:
                        visited.append(new_state)
                        newpath=path+[action]
                        PriorityQueue.enQueue((new_state,newpath,m.path_cost(cost)))
        return []
    def astar(self,g:SingleFoodSearchProblem or MultiFoodSearchProblem) -> list:
        m=copy.deepcopy(g)
        pacman_state=m.P
        PriorityQueue=fringes.PriorityQueue(key=lambda x:x[2])
        PriorityQueue.enQueue((pacman_state,[],0))
        visited=[]
        while(PriorityQueue.empty()!=True):
            state,path,cost=PriorityQueue.deQueue()
            heuristic=self.EuclideanHeuristic(state,m.F)
            if m.goal_test(state)==True:
                if len(m.F)<=1:
                    return path+['Stop']
                for i in m.F.copy():
                    if m.F[i]==state:
                        m.F.pop(i)
                        visited.clear()
                        PriorityQueue.clear()
                        PriorityQueue.enQueue((state,path,m.path_cost(cost)+heuristic))
                        break
            else:
                for new_state, action in m.get_successor(state):
                    heuristic=self.EuclideanHeuristic(new_state,m.F)
                    if new_state not in visited:
                        visited.append(new_state)
                        newpath=path+[action]
                        PriorityQueue.enQueue((new_state,newpath,m.path_cost(cost)+heuristic))
        return []
    def gbfs(self,g:SingleFoodSearchProblem or MultiFoodSearchProblem) -> list:
        m=copy.deepcopy(g)
        pacman_state=m.P
        PriorityQueue=fringes.PriorityQueue(key=lambda x:x[2])
        PriorityQueue.enQueue((pacman_state,[],0,0))
        visited=[]
        while(PriorityQueue.empty()!=True):
            state,path,weight,cost=PriorityQueue.deQueue()
            heuristic=self.EuclideanHeuristic(state,m.F)
            if m.goal_test(state)==True:
                if len(m.F)<=1:
                    return path+['Stop']
                for i in m.F.copy():
                    if m.F[i]==state:
                        m.F.pop(i)
                        visited.clear()
                        PriorityQueue.clear()
                        PriorityQueue.enQueue((state,path,cost+heuristic,cost))
                        break
            else:
                for new_state, action in m.get_successor(state):
                    heuristic=self.EuclideanHeuristic(new_state,m.F)
                    if new_state not in visited:
                        visited.append(new_state)
                        newpath=path+[action]
                        cost=m.path_cost(cost)
                        PriorityQueue.enQueue((new_state,newpath,cost+heuristic,cost))
        return []
SFSP=SingleFoodSearchProblem()
MFSP=MultiFoodSearchProblem()
searcher=searchAgents()



def algorithm(problems:SingleFoodSearchProblem or MultiFoodSearchProblem):
    while True:
        number=input("algorithm:\n1.BFS\t2.DFS\t3.UCS\t4.AStar\t5.GBFS\n")
        number=int(number)
        if number==1:
            path=searcher.BFS(problems)
        elif number==2:
            path=searcher.DFS(problems)
        elif number==3:
            path=searcher.UCS(problems)
        elif number==4:
            path=searcher.astar(problems)
        elif number==5:
            path=searcher.gbfs(problems)
        else:
            break
        problems.animate(path)
while True:
    number=input("Testcase:\n1.Single01\t2.Single02\t3.Single03\t4.Multi01\t5.Multi02\t6.Multi03\n")
    number=int(number)
    if number==1:
        SFSP.load_from_file('sample_inputs/pacman_single01.txt')
        algorithm(SFSP)
        break
    elif number==2:
        SFSP.load_from_file('sample_inputs/pacman_single02.txt')
        algorithm(SFSP)
        break
    elif number==3:
        SFSP.load_from_file('sample_inputs/pacman_single03.txt')
        algorithm(SFSP)
        break
    elif number==4:
        MFSP.load_from_file('sample_inputs/pacman_multi01.txt')
        algorithm(MFSP)
        break
    elif number==5:
        MFSP.load_from_file('sample_inputs/pacman_multi02.txt')
        algorithm(MFSP)
        break
    elif number==6:
        MFSP.load_from_file('sample_inputs/pacman_multi03.txt')
        algorithm(MFSP)
        break
    else:
        continue