from ABC.Abstract_class import *
from Module.Menu import heapq, time
from Module.Problem import *

class Node_UCS(Node):
    #constructor
    def __init__(self, cur_state, cost):
        super().__init__(cur_state)
        self.cost = cost
        
    #to string
    
    def __eq__(self, other):
        return self.cur_state == other.cur_state
    
    def __ne__(self, other):
        return self.cur_state != other.cur_state

    def __lt__(self, other):
        return (self.cost < other.cost)

    def __gt__(self, other):
        return (self.cost > other.cost)

    def __le__(self, other):
        return (self.cost < other.cost) or (self.cost == other.cost)

    def __ge__(self, other):
        return (self.cost > other.cost) or (self.cost == other.cost)
    
        
    @staticmethod
    def child_node(problem, node, action):   
        child_state = node.cur_state.copy()
        child_state[action[1]] = action[0]
        child_node = Node_UCS(child_state.copy(), node.cost + 1)
        return child_node
    
class UCS(Search):
    def __init__(self):
        self.frontier = []
        self.explored = set()
    
    def solve_problem(self, problem, measure):
        node = Node_UCS(problem.ini_state.copy(), problem.path_cost)
        heapq.heappush(self.frontier, node)
    # sort frontier
        while(len(self.frontier)):
            temp = heapq.heappop(self.frontier)
            self.explored.add(tuple(temp.cur_state))
            num_pair = Problem.goal_test(temp.cur_state)
            if num_pair == 0:
                measure.time = time.time() * 1000 - measure.time
                return temp.cur_state
            for action in Problem.actions(temp.cur_state):
                child = Node_UCS.child_node(problem, temp, action)
                if tuple(child.cur_state) not in self.explored and child not in self.frontier:
                    heapq.heappush(self.frontier, child)
        return 0
    