from copy import deepcopy
from problems import SingleFoodSearchProblem, MultiFoodSearchProblem
from fringes import Stack, Queue, PriorityQueue


def bfs(problem: SingleFoodSearchProblem or MultiFoodSearchProblem) -> list:
    m = deepcopy(problem)
    pacman_state = m.P
    queue = Queue()
    queue.en_queue((pacman_state, []))
    visited = []
    while not queue.empty():
        state, path = queue.de_queue()
        if m.goal_test(state):
            if len(m.F) <= 1:
                return path+['Stop']
            for i in m.F.copy():
                if m.F[i] == state:
                    m.F.pop(i)
                    visited.clear()
                    queue.clear()
                    queue.en_queue((state, path))
                    break
        else:
            for new_state, action in m.get_successor(state):
                if new_state not in visited:
                    visited.append(new_state)
                    queue.en_queue((new_state, path+[action]))
    return []


def dfs(problem: SingleFoodSearchProblem or MultiFoodSearchProblem) -> list:
    m = deepcopy(problem)
    pacman_state = m.P
    stack = Stack()
    stack.push((pacman_state, []))
    visited = []
    while (stack.empty() != True):
        state, path = stack.pop()
        if m.goal_test(state):
            if len(m.F) <= 1:
                return path+['Stop']
            for i in m.F.copy():
                if m.F[i] == state:
                    m.F.pop(i)
                    visited.clear()
                    stack.clear()
                    stack.push((state, path))
                    break
        else:
            for new_state, action in m.get_successor(state):
                if new_state not in visited:
                    visited.append(new_state)
                    stack.push((new_state, path+[action]))
    return []


def ucs(problem: SingleFoodSearchProblem or MultiFoodSearchProblem) -> list:
    m = deepcopy(problem)
    pacman_state = m.P
    priority_queue = PriorityQueue(key=lambda x: x[2])
    priority_queue.en_queue((pacman_state, [], 0))
    visited = []
    while (priority_queue.empty() != True):
        state, path, cost = priority_queue.de_queue()
        if m.goal_test(state) == True:
            if len(m.F) <= 1:
                return path+['Stop']
            for i in m.F.copy():
                if m.F[i] == state:
                    m.F.pop(i)
                    visited.clear()
                    priority_queue.clear()
                    priority_queue.en_queue((state, path, m.path_cost(cost)))
                    break
        else:
            for new_state, action in m.get_successor(state):
                if new_state not in visited:
                    new_path = path+[action]
                    visited.append(new_state)
                    priority_queue.en_queue((new_state, new_path, m.path_cost(cost)))
    return []


def Euclidean_heuristic(state, goal_state: dict):
    row_s, col_s = [int(i) for i in state]
    heuristic = goal_state.copy()
    for i in goal_state:
        row_g, col_g = [int(j) for j in goal_state[i]]
        heuristic[i] = ((row_g-row_s)**2+(col_g-col_s)**2)**0.5
    return min(heuristic.values())


def Manhattan_heuristic(state, goal_state: dict):
    row_s, col_s = [int(i) for i in state]
    heuristic = goal_state.copy()
    for i in goal_state:
        row_g, col_g = [int(j) for j in goal_state[i]]
        heuristic[i] = abs(row_g-row_s)+abs(col_g-col_s)
    return heuristic


def astar(problem: SingleFoodSearchProblem or MultiFoodSearchProblem, fn_heuristic) -> list:
    m = deepcopy(problem)
    pacman_state = m.P
    priority_queue = PriorityQueue(key=lambda x: x[2])
    priority_queue.en_queue((pacman_state, [], 0))
    visited = []
    while (priority_queue.empty() != True):
        state, path,weight, cost = priority_queue.de_queue()
        heuristic = fn_heuristic(state, m.F)
        if m.goal_test(state) == True:
            if len(m.F) <= 1:
                return path+['Stop']
            for i in m.F.copy():
                if m.F[i] == state:
                    m.F.pop(i)
                    visited.clear()
                    priority_queue.clear()
                    priority_queue.en_queue((state, path,cost+heuristic,cost))
                    break
        else:
            for new_state, action in m.get_successor(state):
                heuristic = fn_heuristic(new_state, m.F)
                if new_state not in visited:
                    visited.append(new_state)
                    new_path = path+[action]
                    cost = m.path_cost(cost)
                    priority_queue.en_queue((new_state, new_path,cost+heuristic,cost))
    return []


def gbfs(problem: SingleFoodSearchProblem or MultiFoodSearchProblem, fn_heuristic) -> list:
    m = deepcopy(problem)
    pacman_state = m.P
    priority_queue = PriorityQueue(key=lambda x: x[2])
    priority_queue.en_queue((pacman_state, [], 0, 0))
    visited = []
    while (priority_queue.empty() != True):
        state, path, weight, cost = priority_queue.de_queue()
        heuristic = fn_heuristic(state, m.F)
        if m.goal_test(state) == True:
            if len(m.F) <= 1:
                return path+['Stop']
            for i in m.F.copy():
                if m.F[i] == state:
                    m.F.pop(i)
                    visited.clear()
                    priority_queue.clear()
                    priority_queue.en_queue((state, path, cost+heuristic, cost))
                    break
        else:
            for new_state, action in m.get_successor(state):
                heuristic = fn_heuristic(new_state, m.F)
                if new_state not in visited:
                    visited.append(new_state)
                    newpath = path+[action]
                    cost = m.path_cost(cost)
                    priority_queue.en_queue((new_state, newpath, cost+heuristic, cost))
    return []
