from ABC.Abstract_class import *
from Module.Menu import heapq, time
from Module.Problem import *

class Node_UCS_Up(Node):
    #constructor
    def __init__(self, cur_state, cost):
        super().__init__(cur_state)
        
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
        child_node = Node_UCS_Up(child_state.copy(), node.cost + 1)
        return child_node
    
class UCS_Up(Search):
    def __init__(self):
        self.frontier = []
        self.explored = set()
    
    def solve_problem(self, problem, measure):
        node = Node_UCS_Up(problem.ini_state.copy(), problem.path_cost)
        heapq.heappush(self.frontier, node)
        num_pair = Problem.goal_test(node.cur_state)
        if num_pair == 0:
            measure.time = time.time() * 1000 - measure.time
            return node.cur_state
    # sort frontier
        while(len(self.frontier)):
            temp = self.frontier.pop()
            self.explored.add(tuple(temp.cur_state))
            for action in Problem.actions(temp.cur_state):
                child = Node_UCS_Up.child_node(problem, temp, action)
                if tuple(child.cur_state) not in self.explored and child not in self.frontier:
                    num_pair = Problem.goal_test(child.cur_state)
                    if num_pair == 0:
                        measure.time = time.time() * 1000 - measure.time
                        return child.cur_state
                    self.frontier.append(child)
        return 0