#!/usr/bin/env python3.7

from ..score_count import ScoreCount
from .slurm_config import SlurmConfig as Config


class SlurmCount(ScoreCount):
    """
    Count method run in a Slurm cluster setup
    """

    """number of processors on the pool"""
    POOL_SIZE = 4
