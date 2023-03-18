import fringes
from problem import SingleFoodSearchProblem,MultiFoodSearchProblem
import copy
class searchAgents:
    def BFS(self, g:SingleFoodSearchProblem or MultiFoodSearchProblem) -> list:
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
            for new_state, action in m.getSuccessor(state):
                if new_state not in visited:
                    visited.append(new_state)
                    queue.enQueue((new_state,path+[action]))
        return path
    def DFS(self, g:SingleFoodSearchProblem or MultiFoodSearchProblem) -> list:
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
            for new_state, action in m.getSuccessor(state):
                if new_state not in visited:
                    visited.append(new_state)
                    stack.push((new_state,path+[action]))
        return path
    def UCS(self, g:SingleFoodSearchProblem or MultiFoodSearchProblem) -> list:
        actions=[]
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
            for new_state, action in m.getSuccessor(state):
                if new_state not in visited:
                    visited.append(new_state)
                    newpath=path+[action]
                    PriorityQueue.enQueue((new_state,newpath,m.path_cost(cost)))
        return path
SFSP=MultiFoodSearchProblem()
while True:
    number=input("Testcase:\n1.Single01\t2.Single02\t3.Single03\t4.Multi01\t5.Multi02\t6.Multi03\n")
    number=int(number)
    if number==1:
        SFSP.load_from_file('sample_inputs/pacman_single01.txt')
        break
    elif number==2:
        SFSP.load_from_file('sample_inputs/pacman_single02.txt')
        break
    elif number==3:
        SFSP.load_from_file('sample_inputs/pacman_single03.txt')
        break
    elif number==4:
        SFSP.load_from_file('sample_inputs/pacman_multi01.txt')
        break
    elif number==5:
        SFSP.load_from_file('sample_inputs/pacman_multi02.txt')
        break
    elif number==6:
        SFSP.load_from_file('sample_inputs/pacman_multi03.txt')
        break
    else:
        continue
searcher=searchAgents()
while True:
    number=input("algorithm:\n1.BFS\t2.DFS\t3.UCS\n")
    number=int(number)
    if number==1:
        path=searcher.BFS(SFSP)
    elif number==2:
        path=searcher.DFS(SFSP)
    elif number==3:
        path=searcher.UCS(SFSP)
    else:
        break
    SFSP.animate(path)