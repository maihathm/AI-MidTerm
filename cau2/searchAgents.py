import fringes
from problems import SingleFoodSearchProblem,MultiFoodSearchProblem
import copy

class searchAgents:
    def Euclidean_heuristic(self,state,goal_state:dict):
        row_s,col_s=[int(i) for i in state]
        heuristic=goal_state.copy()
        for i in goal_state:
            row_g,col_g=[int(j) for j in goal_state[i]]
            heuristic[i]=((row_g-row_s)**2+(col_g-col_s)**2)**0.5
        return min(heuristic.values())
    def Manhattan_heuristic(self,state,goal_state:dict):
        row_s,col_s=[int(i) for i in state]
        heuristic=goal_state.copy()
        for i in goal_state:
            row_g,col_g=[int(j) for j in goal_state[i]]
            heuristic[i]=abs(row_g-row_s)+abs(col_g-col_s)
        return min(heuristic.values())

    def astar(self, g: SingleFoodSearchProblem or MultiFoodSearchProblem, fn_heuristic) -> list:
        m=copy.deepcopy(g)
        pacman_state=m.P
        PriorityQueue=fringes.PriorityQueue(key=lambda x:x[2])
        PriorityQueue.enQueue((pacman_state,[],0))
        visited=[]
        while(PriorityQueue.empty()!=True):
            state,path,cost=PriorityQueue.deQueue()
            heuristic=fn_heuristic(state,m.F)
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
            for new_state, action in m.get_successor(state):
                heuristic=fn_heuristic(new_state,m.F)
                if new_state not in visited:
                    visited.append(new_state)
                    newpath=path+[action]
                    PriorityQueue.enQueue((new_state,newpath,m.path_cost(cost)+heuristic))
        return []

    def gbfs(self, g: SingleFoodSearchProblem or MultiFoodSearchProblem, fn_heuristic) -> list:
        m=copy.deepcopy(g)
        pacman_state=m.P
        PriorityQueue=fringes.PriorityQueue(key=lambda x:x[2])
        PriorityQueue.enQueue((pacman_state,[],0,0))
        visited=[]
        while(PriorityQueue.empty()!=True):
            state,path,weight,cost=PriorityQueue.deQueue()
            heuristic=fn_heuristic(state,m.F)
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
            for new_state, action in m.get_successor(state):
                heuristic=fn_heuristic(new_state,m.F)
                if new_state not in visited:
                    visited.append(new_state)
                    newpath=path+[action]
                    cost=m.path_cost(cost)
                    PriorityQueue.enQueue((new_state,newpath,cost+heuristic,cost))
        return []

MFSP=MultiFoodSearchProblem()
while True:
    number=input("Testcase:\n1.Single01\t2.Single02\t3.Single03\t4.Multi01\t5.Multi02\t6.Multi03\n")
    number=int(number)
    if number==1:
        MFSP.load_from_file('sample_inputs/pacman_single01.txt')
        break
    elif number==2:
        MFSP.load_from_file('sample_inputs/pacman_single02.txt')
        break
    elif number==3:
        MFSP.load_from_file('sample_inputs/pacman_single03.txt')
        break
    elif number==4:
        MFSP.load_from_file('sample_inputs/pacman_multi01.txt')
        break
    elif number==5:
        MFSP.load_from_file('sample_inputs/pacman_multi02.txt')
        break
    elif number==6:
        MFSP.load_from_file('sample_inputs/pacman_multi03.txt')
        break
    else:
        continue
searcher=searchAgents()
while True:
    number=input("algorithm:\n1.A*\t2.GBFS\n")
    number=int(number)
    if number==1 or number==2:
        heuristic=input("heuristic:\n1.Euclidean_heuristic\t2.Manhattan_heuristic\n")
        heuristic=int(heuristic)
    if number==1:
        if heuristic==1:
            path=searcher.astar(MFSP,searcher.Euclidean_heuristic)
        elif heuristic==2:
            path=searcher.astar(MFSP,searcher.Manhattan_heuristic)
        else:
            break
    elif number==2:
        if heuristic==1:
            path=searcher.gbfs(MFSP,searcher.Euclidean_heuristic)
        elif heuristic==2:
            path=searcher.gbfs(MFSP,searcher.Manhattan_heuristic)
        else:
            break
    else:
        break
    MFSP.animate(path)