import os
import numpy
class SingleFoodSearchProblem:
    def __init__(self):
        self.matrix = list()
        self.P = tuple()
        self.F = dict()

    def __str__(self):
        res = 'Pacman: '+str(self.P)+"\n"
        res += 'Food: '+str(self.F)+"\n"
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
                        for i in range(len(arr)):
                            if arr[i]=='.':
                                self.F.update({len(self.F): (row,i)})
                    if 'P' in arr:
                        self.P = (row, arr.index('P'))
                    temp_map.append(arr)
                    row += 1
                self.matrix = numpy.array(temp_map)
    def actions(self,state):
        actions=[]
        Map=self.matrix
        row,col=state
        if row < len(self.matrix) and col<len(self.matrix[row]):
            if len(self.matrix[row])>col+1:
                if self.matrix[row][col+1]!='%':
                    actions.append('E')
            if row-1>=0:
                if self.matrix[row-1][col]!='%':
                    actions.append('N')
            if len(self.matrix)>row+1:
                if self.matrix[row+1][col]!='%':
                    actions.append('S')
            if col-1>=0:
                if self.matrix[row][col-1]!='%':
                    actions.append('W')
        # if self.matrix[row][col]=='.':
        #     actions.append('Stop')
        return actions
    def result(self,state,action):
        if action=="E":
            new_state=(state[0],state[1]+1)
        elif action=="W":
            new_state=(state[0],state[1]-1)
        elif action=="N":
            new_state=(state[0]-1,state[1])
        else:
            new_state=(state[0]+1,state[1]+1)
        return new_state
    def path_cost(self,cost,state1,action,state2):
        return cost+1
    def goal_test(self, state):
        return state in self.F.values()
# g = SingleFoodSearchProblem()
# g.load_from_file('sample_inputs/pacman_single01.txt')
# g.print()