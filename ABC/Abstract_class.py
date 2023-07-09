from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, cur_state):
        self.cur_state = cur_state

class Search(ABC):
    @property
    @abstractmethod
    def solve_problem(self, problem, measure):
        pass