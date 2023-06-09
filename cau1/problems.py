import os
import numpy
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
                        self.F.update({len(self.F): (row,arr.index('.'))})
                    if 'P' in arr:
                        self.P = (row, arr.index('P'))
                    temp_map.append(arr)
                    row += 1
                self.matrix = numpy.array(temp_map)
    def get_successor(self,state):
        successor=[]
        row,col=state
        new_state=tuple()
        if self.matrix[row-1][col]!='%':
            new_state=(row-1, col)
            successor.append((new_state,'N'))
        if self.matrix[row+1][col]!='%':
            new_state=( row+1, col)
            successor.append((new_state,'S'))
        if self.matrix[row][col-1]!='%':
            new_state=(row, col-1)
            successor.append((new_state,"W"))
        if self.matrix[row][col+1]!='%':
            new_state=(row,col+1)
            successor.append((new_state,'E'))
        return successor
    def path_cost(self,cost):
        return cost+1
    def goal_test(self, state):
        return state in self.F.values()
    def animate(self,actions:list)->None:
        temp=self.matrix.copy()
        matrix=self.matrix
        current=self.P 
        os.system('cls')
        self.print()
        input("Press Enter to continue...")
        while(len(actions)>=0):
            row,col=current
            if len(actions)==0:
                self.matrix[row][col]=' '
                r,c=self.P
                self.matrix[r][c]='P'
                break
            action=actions.pop(0)
            self.matrix[row][col]=' '
            if action=='E':
                matrix[row][col+1]='P'
                current=(row,col+1)
            elif action=='N':
                matrix[row-1][col]='P'
                current=(row-1, col)
            elif action=='S':
                matrix[row+1][col]='P'
                current=(row+1, col)
            elif action=='W':
                matrix[row][col-1]='P'
                current=(row, col-1)
            else:
                break
            os.system('cls')
            self.print()
            input("Press Enter to continue...")
        self.matrix=temp
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
                            if arr[i]=='.':
                                self.F.update({len(self.F): (row,i)})
                    if 'P' in arr:
                        self.P = (row, arr.index('P'))
                    temp_map.append(arr)
                    row += 1
                self.matrix = numpy.array(temp_map)
