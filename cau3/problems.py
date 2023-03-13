import os
import numpy

class EightQueenProblem:
    def __init__(self):
        self.matrix = list()
        self.Q = dict()

    def __str__(self):
        res = 'Queen: '+str(self.Q)+"\n"
        for x in self.matrix:
            temp = ''
            for y in x:
                temp += y
            temp += '\n'
            res += temp
        return res

    def h(self):
        q_list = [self.Q[i] for i in range(len(self.Q))]
        s= 0
        for i in q_list:
            for j in q_list:
                if ((i[0] - j[0]) == (i[1]- j[1]) and (i[0] - j[0] !=0) and (i[1] - j[1] !=0)) or ((i[0] - j[0]) == -(i[1] - j[1]) and (i[0] - j[0] !=0) and (i[1] - j[1] !=0)) or (i[0] == j[0] and i[1] != j[1]) or (i[0] != j[0] and i[1] == j[1]):
                    s+=1
        print(int(s/2))
    def print(self):
        print(str(self))

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename) as g:
                temp_map = []
                allmap = g.read().replace(' ','').split('\n')
                row = 0
                for line in allmap:
                    arr = [x for x in line]
                    if 'Q' in arr:
                        for i in range(len(arr)):
                            if arr[i]=='Q':
                                self.Q.update({len(self.Q): (row,i)})
                    temp_map.append(arr)
                    row += 1
                self.matrix = numpy.array(temp_map)  

g = EightQueenProblem()
g.load_from_file('sample_inputs/eight_queens03.txt')
g.print()
g.h()
