#!/usr/bin/env python3.7

from typing import Iterable
from functools import partial
from multiprocessing import Pool

from ..score_count import ScoreCount
from .parallel_config import ParallelConfig as Config


class ParallelScore(ScoreCount):

    @staticmethod
    def run(combinations: Iterable, solutions: Iterable):
        pool = Pool(Config.POOL_SIZE)
        combinations_space = list(combinations)

        scores = {
            combinations: score for combinations, score in pool.imap_unordered(
                partial(ScoreCount._count_score, solutions=list(solutions)),
                iterable=combinations_space,
                chunksize=len(combinations_space) // Config.POOL_SIZE,
            )
        }

        pool.close()

        return scores
