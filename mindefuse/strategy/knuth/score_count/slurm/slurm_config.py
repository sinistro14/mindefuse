#!/usr/bin/env python3.7


class SlurmConfig:

    """number of processors on the pool"""
    POOL_SIZE = 4

    """number of available nodes"""
    AVAILABLE_WORKERS = 40

    """Time sleep between process poling check"""
    SLEEP_TIME = 1  # seconds
