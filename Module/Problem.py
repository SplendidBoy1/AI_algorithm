import random

def create_start_state(n):
    result = []
    for i in range(0, n):
        result.append(random.randint(0, n - 1))
    return result

class Problem:
    def __init__(self, n):
        self.ini_state = create_start_state(n)
        self.path_cost = 0
        
    @staticmethod
    def goal_test(state):
        num_pair = 0     
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] == state[j]) or (abs(i - j)) == abs(state[i] - state[j]):
                    num_pair += 1 
        return num_pair
        
    def actions(state):
        # the list of state that can action
        result = []
        for i in range(0, len(state)):
            for j in range(0, len(state)):
                if (state[i] != j):
                    result.append([j, i])
        return result