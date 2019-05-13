#!/usr/bin/env python3.7

from typing import Iterable
from multiprocessing import Process, SimpleQueue

from ..score_count import ScoreCount
from .parallel_config import ParallelConfig as Config


class ParallelScore(ScoreCount):
    """
    Multiprocessing score counter
    Batches of combinations are distributed, processed and scored using a process pool
    """

    @staticmethod
    def __chunks(itr: Iterable, n: int) -> Iterable:
        """
        Divides an iterable into n of equally sized chunks, as possible
        :param itr: iterable to divide
        :param n: number of chunks
        :return: generator of chunks
        """
        itr = list(itr)
        return [itr[i::n] for i in range(n)]

    @staticmethod
    def __process_combinations(combinations: Iterable, solutions: Iterable, results: SimpleQueue):
        """
        Calculates the score for all combinations and retains only the best scored ones
        The result is placed on the results Queue
        :param combinations: combinations to score
        :param solutions: existing solutions
        :param results: queue used to commit the results
        """

        solutions = list(solutions)

        scores = {
            combination: ScoreCount._count_score(combination, solutions)[1] for combination in combinations
        }

        min_score = min(scores.values())

        results.put({k: v for k, v in scores.items() if v == min_score})

    @staticmethod
    def run(combinations: Iterable, solutions: Iterable):

        jobs = []

        results = SimpleQueue()

        for combs in ParallelScore.__chunks(combinations, Config.POOL_SIZE):
            job = Process(
                    target=ParallelScore.__process_combinations,
                    args=(combs, solutions, results),
                    daemon=True,
                )
            job.start()
            jobs.append(job)

        scores = {}

        [scores.update(results.get()) for _ in jobs]  # blocking call

        [job.join() for job in jobs]  # to ensure that all processes are completed

        return scores
