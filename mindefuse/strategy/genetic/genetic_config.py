#!/usr/bin/env python3.7


class GeneticConfig:
    """
    Configuration of Genetic Algorithm
    """

    CROSSOVER_PROBABILITY = 0.5
    CROSSOVER_THEN_MUTATION_PROBABILITY = 0.03
    PERMUTATION_PROBABILITY = 0.03
    INVERSION_PROBABILITY = 0.02

    MAX_POP_SIZE = 60
    MAX_GENERATIONS = 100