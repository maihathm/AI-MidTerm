from problems import SingleFoodSearchProblem, MultiFoodSearchProblem, EightQueenProblem
from searchAgents import bfs, dfs, ucs, astar, gbfs, Euclidean_heuristic, Manhattan_heuristic


def cau1_2():
    while True:
        number = int(input(
            "Testcase:\n1.Single01\t2.Single02\t3.Single03\t4.Multi01\t5.Multi02\t6.Multi03\n"))
        if number == 1:
            problem = SingleFoodSearchProblem()
            problem.load_from_file("sample_inputs/pacman_single01.txt")
            algorithm1_2(problem)
        elif number == 2:
            problem = SingleFoodSearchProblem()
            problem.load_from_file("sample_inputs/pacman_single02.txt")
            algorithm1_2(problem)
        elif number == 3:
            problem = SingleFoodSearchProblem()
            problem.load_from_file("sample_inputs/pacman_single03.txt")
            algorithm1_2(problem)
        elif number == 4:
            problem = MultiFoodSearchProblem()
            problem.load_from_file("sample_inputs/pacman_multi01.txt")
            algorithm1_2(problem)
        elif number == 5:
            problem = MultiFoodSearchProblem()
            problem.load_from_file("sample_inputs/pacman_multi02.txt")
            algorithm1_2(problem)
        elif number == 6:
            problem = MultiFoodSearchProblem()
            problem.load_from_file("sample_inputs/pacman_multi03.txt")
            algorithm1_2(problem)
        else:
            break


def algorithm1_2(problem: SingleFoodSearchProblem or MultiFoodSearchProblem):
    while True:
        number = int(
            input("Algorithm:\n1.BFS\t2.DFS\t3.UCS\t4.AStar\t5.GBFS\n"))
        if number == 1:
            path = bfs(problem)
            print(path)
        elif number == 2:
            path = dfs(problem)
            print(path)
        elif number == 3:
            path = ucs(problem)
            print(path)
        elif number == 4:
            heuristic = choose_heuristic()
            if heuristic == 1:
                path = astar(problem, Euclidean_heuristic)
                print(path)
            elif heuristic == 2:
                path = astar(problem, Manhattan_heuristic)
                print(path)
        elif number == 5:
            heuristic = choose_heuristic()
            if heuristic == 1:
                path = gbfs(problem, Euclidean_heuristic)
                print(path)
            elif heuristic == 2:
                path = gbfs(problem, Manhattan_heuristic)
                print(path)
        else:
            break


def choose_heuristic():
    while True:
        number = int(input("Heuristic:\n1.Euclidean\t2.Manhattan\n"))
        if number == 1 or number == 2:
            return number


def cau3():
    while True:
        number = int(input("Testcase:\n1.Queen01\t2.Queen02\t3.Queen03\n"))
        if number == 1:
            problem = EightQueenProblem()
            problem.load_from_file("sample_inputs/eight_queens01.txt")
            algorithm3(problem)
        elif number == 2:
            problem = EightQueenProblem()
            problem.load_from_file("sample_inputs/eight_queens02.txt")
            algorithm3(problem)
        elif number == 3:
            problem = EightQueenProblem()
            problem.load_from_file("sample_inputs/eight_queens03.txt")
            algorithm3(problem)
        else:
            break

def algorithm3(problem):
    problem.print()
    problem.__newinit__()
    print(problem.h([0, 7]))
    problem.print_board()



# cau1_2()
#cau3()
