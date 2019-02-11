"""
This module implements local search on a sine abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@edited_by:job4
@version 11feb2019
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class SinVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x*math.sin(x))


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    initial = randrange(0, maximum)
    p = SinVariant(initial, maximum, delta=1.0)
    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    # Solve the problem using hill-climbing.
    i = 0
    highest_solution = 0
    while i < 100:
        hill_solution = hill_climbing(p)
        if p.value(hill_solution) > p.value(highest_solution):
            highest_solution = hill_solution
        i = i + 1
        p.initial = randrange(0, maximum)

    p.initial = initial
    print('Hill-climbing solution       x: ' + str(highest_solution)
          + '\tvalue: ' + str(p.value(highest_solution))
          )

    # Solve the problem using simulated annealing.
    i = 0
    highest_annealing_solution = 0
    while i < 100:
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        if p.value(annealing_solution) > p.value(highest_annealing_solution):
            highest_annealing_solution = annealing_solution
        i = i + 1
        p.initial = randrange(0, maximum)

    p.initial = initial
    print('Simulated annealing solution x: ' + str(highest_annealing_solution)
          + '\tvalue: ' + str(p.value(highest_annealing_solution))
          )
