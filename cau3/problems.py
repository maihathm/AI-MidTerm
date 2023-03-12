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
