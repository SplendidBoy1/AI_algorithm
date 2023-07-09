from copy import deepcopy
import time
import heapq
import tracemalloc
from Search.UCS_Up import *
from Search.UCS import *
from Search.A_star import *
from Search.GA import *

######################

class Menu():
    @staticmethod
    def print_menu():
        print('***********MENU***********')
        print('1. UCS')
        print('2. A*')
        print('3. Genetic Algorithm')
        print("4. UCS (without path_cost)")
        print('Input the option you want to play')
    
    @staticmethod
    def choices():
        n = int(input())
        s1 = UCS()
        s2 = A_star()
        s3 = Genetic_Algorithm()
        s4 = UCS_Up()
        if n == 1:
            return s1
        elif n == 2:
            return s2
        elif n == 3:
            return s3
        elif n == 4:
            return s4
        return None
    
    @staticmethod
    def executed(search, problem, measure):
        result = search.solve_problem(problem, measure)
        measure.memory = tracemalloc.get_traced_memory()[1] / (1024**2)
        tracemalloc.stop()
        print('Result state')
        print(result)
        print('Time executed (Ms)')
        print(measure.time)
        print('Memory used (MB)')
        print(measure.memory)
        return

class Measure:
    def __init__(self):
        self.time = time.time() * 1000
        self.memory = 0
          