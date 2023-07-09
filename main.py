
from Module.Menu import Menu, Measure, tracemalloc, Problem

def main():
    n = int(input('Input the number of queen \n'))
    problem = Problem(n)
    Menu.print_menu()
    search = Menu.choices()
    tracemalloc.start()
    measure = Measure()
    Menu.executed(search, problem, measure)

if __name__ == "__main__":
    main()