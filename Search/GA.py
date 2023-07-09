from ABC.Abstract_class import *
from Module.Problem import *
from Module.Menu import heapq, time

class Node_GA(Node):
    #constructor
    def __init__(self, cur_state, fitness):
        super().__init__(cur_state)
        self.fitness = fitness
        
    #to string
    
    def __eq__(self, other):
        return self.cur_state == other.cur_state
    
    def __ne__(self, other):
        return self.cur_state != other.cur_state

    def __lt__(self, other):
        return (self.fitness < other.fitness)

    def __gt__(self, other):
        return (self.fitness > other.fitness)

    def __le__(self, other):
        return (self.fitness < other.fitness) or (self.fitness == other.fitness)

    def __ge__(self, other):
        return (self.fitness > other.fitness) or (self.fitness == other.fitness)
           

class Genetic_Algorithm(Search):
    def __init__(self):
        population = []
    
    @staticmethod
    def ini_population(num_queens, n):
        ls = []
        num = random.randint(2, n)
        while (num != 0):
            state = []
            for i in range(0, num_queens):
                state.append(random.randint(0, num_queens - 1))
            node = Node_GA(state, Problem.goal_test(state))
            ls.append(node)
            num = num - 1
        return ls
    
    @staticmethod
    def pick_rand(population):
        maxi = 0
        for i in population:
            maxi += i.fitness
        pick = random.randint(0, maxi)
        current = 0
        for value in population:
            current += maxi - value.fitness
            if current >= pick:
                return value
    
    @staticmethod
    def cross_over(node1, node2):
        len_state = len(node1.cur_state)
        point = random.randint(0, len_state - 1)
        state_child1 = node1.cur_state[:point] + node2.cur_state[point:len_state]
        state_child2 = node2.cur_state[:point] + node1.cur_state[point:len_state]
        return state_child1, state_child2
    
    @staticmethod
    def mutate(state):
        len_state = len(state)
        point = random.randint(0, len_state - 1)
        value_point = random.randint(0, len_state - 1)
        state[point] = value_point
        return state
    
    @staticmethod  
    def goal(population):
        for node in population:
            if node.fitness == 0:
                return node.cur_state
        return None
        
        
    def solve_problem(self, problem, measure):
        queen = len(problem.ini_state)
        self.population = Genetic_Algorithm.ini_population(queen, queen)
        heapq.heappush(self.population, Node_GA(problem.ini_state, Problem.goal_test(problem.ini_state)))
        check = Genetic_Algorithm.goal(self.population)
        while check == None:
            new_population = []  
            for i in range(0, len(self.population), 2):
                parent1 = Genetic_Algorithm.pick_rand(self.population)
                parent2 = Genetic_Algorithm.pick_rand(self.population)
                state_child1, state_child2 = Genetic_Algorithm.cross_over(parent1, parent2)
                if random.randint(1, 5) == 1:
                    state_child1 = Genetic_Algorithm.mutate(state_child1)
                    state_child2 = Genetic_Algorithm.mutate(state_child2)
                child1 = Node_GA(state_child1, Problem.goal_test(state_child1))
                child2 = Node_GA(state_child2, Problem.goal_test(state_child2))
                heapq.heappush(new_population, child1)
                heapq.heappush(new_population, child2)
            for node in self.population:
                self.population.pop()
            self.population = new_population.copy()
            check = Genetic_Algorithm.goal(self.population)
        measure.time = time.time() * 1000 - measure.time
        return heapq.heappop(self.population)   