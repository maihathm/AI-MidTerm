import os
import numpy
import random
from copy import deepcopy


class SingleFoodSearchProblem:
    def __init__(self):
        self.matrix = list()
        self.P = tuple()
        self.F = dict()

    def __str__(self):
        res = ''
        for x in self.matrix:
            temp = ''
            for y in x:
                temp += y
            temp += '\n'
            res += temp
        return res

    def print(self):
        print(str(self))

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename) as g:
                temp_map = []
                allmap = g.read().split('\n')
                row = 0
                for line in allmap:
                    arr = [x for x in line]
                    if '.' in arr:
                        self.F.update({len(self.F): (row, arr.index('.'))})
                    if 'P' in arr:
                        self.P = (row, arr.index('P'))
                    temp_map.append(arr)
                    row += 1
                self.matrix = numpy.array(temp_map)

    def get_successor(self, state):
        successor = []
        row, col = state
        new_state = tuple()
        if self.matrix[row-1][col] != '%':
            new_state = (row-1, col)
            successor.append((new_state, 'N'))
        if self.matrix[row+1][col] != '%':
            new_state = (row+1, col)
            successor.append((new_state, 'S'))
        if self.matrix[row][col-1] != '%':
            new_state = (row, col-1)
            successor.append((new_state, "W"))
        if self.matrix[row][col+1] != '%':
            new_state = (row, col+1)
            successor.append((new_state, 'E'))
        return successor

    def path_cost(self, cost):
        return cost+1

    def goal_test(self, state):
        return state in self.F.values()

    def animate(self, actions: list) -> None:
        temp = self.matrix.copy()
        matrix = self.matrix
        current = self.P
        os.system('cls')
        self.print()
        input("Press Enter to continue...")
        while (len(actions) >= 0):
            row, col = current
            if len(actions) == 0:
                self.matrix[row][col] = ' '
                r, c = self.P
                self.matrix[r][c] = 'P'
                break
            action = actions.pop(0)
            self.matrix[row][col] = ' '
            if action == 'E':
                matrix[row][col+1] = 'P'
                current = (row, col+1)
            elif action == 'N':
                matrix[row-1][col] = 'P'
                current = (row-1, col)
            elif action == 'S':
                matrix[row+1][col] = 'P'
                current = (row+1, col)
            elif action == 'W':
                matrix[row][col-1] = 'P'
                current = (row, col-1)
            else:
                break
            os.system('cls')
            self.print()
            input("Press Enter to continue...")
        self.matrix = temp


class MultiFoodSearchProblem(SingleFoodSearchProblem):
    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename) as g:
                temp_map = []
                allmap = g.read().split('\n')
                row = 0
                for line in allmap:
                    arr = [x for x in line]
                    if '.' in arr:
                        for i in range(len(arr)):
                            if arr[i] == '.':
                                self.F.update({len(self.F): (row, i)})
                    if 'P' in arr:
                        self.P = (row, arr.index('P'))
                    temp_map.append(arr)
                    row += 1
                self.matrix = numpy.array(temp_map)


class EightQueenProblem:
    def __init__(self):
        self.matrix = list()
        self.Q = dict()

    def __newinit__(self):
        n = len(self.Q)
        self.board = [[0 for x in range(8)] for y in range(8)]
        for i in range(n):
            self.board[i][random.randint(0, 7)] = 1

    def __str__(self):
        res = 'Queen: '+str(self.Q)+"\n"
        for x in self.matrix:
            temp = ''
            for y in x:
                temp += y
            temp += '\n'
            res += temp
        return res

    def count(self, matrix_new):
        q_list = [matrix_new[i] for i in range(len(matrix_new))]
        s = 0
        for i in q_list:
            for j in q_list:
                if ((i[0] - j[0]) == (i[1] - j[1]) and (i[0] - j[0] != 0) and (i[1] - j[1] != 0)) or ((i[0] - j[0]) == -(i[1] - j[1]) and (i[0] - j[0] != 0) and (i[1] - j[1] != 0)) or (i[0] == j[0] and i[1] != j[1]) or (i[0] != j[0] and i[1] == j[1]):
                    s += 1
        return (int(s/2))

    def h(self, state):
        c = 0
        matrix_new = dict()
        matrix_copy = deepcopy(self.matrix)
        col = state[0]
        row = state[1]
        if matrix_copy[col, row] == "0":
            for i in range(len(matrix_copy)):
                if matrix_copy[i, row] == "Q":
                    matrix_copy[i, row] = "0"
                    matrix_copy[col, row] = "Q"
        for i in range(len(matrix_copy)):
            for j in range(len(matrix_copy)):
                if (matrix_copy[i][j] == 'Q'):
                    matrix_new.update({len(matrix_new): (i, j)})
        for i in range(len(matrix_copy)):
            for j in range(len(matrix_copy[i])):
                if matrix_copy[i][j] == "Q":
                    state = [i, j]
                    c = self.count(matrix_new)
        return c

    def print(self):
        print(str(self))

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename) as g:
                temp_map = []
                allmap = g.read().replace(' ', '').split('\n')
                row = 0
                for line in allmap:
                    arr = [x for x in line]
                    if 'Q' in arr:
                        for i in range(len(arr)):
                            if arr[i] == 'Q':
                                self.Q.update({len(self.Q): (row, i)})
                    temp_map.append(arr)
                    row += 1
                self.matrix = numpy.array(temp_map)

    def get_heuristic(self):
        heuristic = 0
        for i in range((len(self.board))):
            for j in range((len(self.board))):
                if self.board[i][j] == 1:
                    for k in range((len(self.board))):
                        if k != i and self.board[k][j] == 1:
                            heuristic += 1
                        if k != j and self.board[i][j] == 1:
                            heuristic += 1
                    for k in range((len(self.board))):
                        if i+k < (len(self.board)) and j+k < (len(self.Q)) and self.board[i+k][j+k] == 1:
                            heuristic += 1
                        if i+k < (len(self.board)) and j-k >= 0 and self.board[i+k][j-k] == 1:
                            heuristic += 1
                        if i-k >= 0 and j+k < (len(self.board)) and self.board[i-k][j+k] == 1:
                            heuristic += 1
                        if i-k >= 0 and j-k >= 0 and self.board[i-k][j-k] == 1:
                            heuristic += 1
        return heuristic

    def get_best_move(self, col):
        best_move = None
        min_heuristic = float('inf')
        for row in range(len(self.board)):
            if self.board[row][col] == 1:
                continue
            self.board[row][col] = 1
            h = self.get_heuristic()
            if h < min_heuristic:
                best_move = row
                min_heuristic = h
            self.board[row][col] = 0
        return best_move

    def check_conflict(self):
        conflict = 0
        for col in range(len(self.board)):
            for row1 in range(len(self.board)):
                if self.board[row1][col] == 1:
                    for row2 in range(row1+1, len(self.board)):
                        if self.board[row2][col] == 1:
                            conflict += 1
                    break
        return conflict

    def hill_climbing_search(self):
        while True:
            curr_heuristic = self.get_heuristic()
            if curr_heuristic == 0:
                return self.board
            for col in range(len(self.board)):
                best_move = self.get_best_move(col)
                if best_move is not None:
                    self.board[best_move][col] = 1
                    if self.check_conflict() == 0:
                        curr_heuristic = self.get_heuristic()
                        for row in range(len(self.board)):
                            if row != best_move:
                                self.board[row][col] = 0
                        if curr_heuristic == 0:
                            return self.board
                    else:
                        self.board[best_move][col] = 0

    def print_board(self):
        for row in range(8):
            for col in range(8):
                if self.board[col][row] == 1:
                    print("Q", end='')
                else:
                    print("0", end='')
            print()
