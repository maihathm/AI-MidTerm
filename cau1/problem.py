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
g = SingleFoodSearchProblem()
g.load_from_file('sample_inputs/pacman_single01.txt')
g.print()
