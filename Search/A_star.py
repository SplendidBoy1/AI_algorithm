from ABC.Abstract_class import *
from Module.Menu import heapq, time
from Module.Problem import *

class Node_A_star(Node):
    #constructor
    def __init__(self, cur_state, cost, heuristic):
        super().__init__(cur_state)
        self.cost = cost
        self.heuristic = heuristic
        
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
        child_heuristic = problem.goal_test(child_state)
        child_node = Node_A_star(child_state.copy(), node.cost - node.heuristic + 1 + child_heuristic, child_heuristic)
        return child_node

class A_star(Search):
    def __init__(self):
        self.frontier = []
        self.explored = set()
    
    def solve_problem(self, problem, measure):
    #create initial node
        ini_state = problem.ini_state
        heuristic = problem.goal_test(ini_state)
        node = Node_A_star(ini_state, problem.path_cost + heuristic, heuristic)
    #create a list to store, solution is each step that can has a result and save as list
    #frontier is a queue
    #create frontier in initial node
        heapq.heappush(self.frontier, node)
    # sort frontier
        while(len(self.frontier)):
            temp = heapq.heappop(self.frontier)
            self.explored.add(tuple(temp.cur_state))
            if temp.heuristic == 0:
                measure.time = time.time() * 1000 - measure.time
                return temp.cur_state
            for action in Problem.actions(temp.cur_state):
                child = Node_A_star.child_node(problem, temp, action)
                if tuple(child.cur_state) not in self.explored and child not in self.frontier:
                    heapq.heappush(self.frontier, child)
        return 0
    