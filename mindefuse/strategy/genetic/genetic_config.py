#!/usr/bin/env python3.7


class GeneticConfig:
    """
    Configuration of Genetic Algorithm
    """

    """crossover probability"""
    CROSSOVER_PROB = 0.5

    """mutation probability"""
    MUTATION_PROB = 0.03

    """permutation probability"""
    PERMUTATION_PROB = 0.03

    """inversion probability"""
    INVERSION_PROB = 0.02

    """maximum initial population size"""
    MAX_POPULATION = 60

    """maximum initial offspring generation attempts"""
    MAX_GENERATIONS = 120
