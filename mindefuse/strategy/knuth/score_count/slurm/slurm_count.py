#!/usr/bin/env python3.7

from time import sleep
from subprocess import Popen, PIPE
from ..score_count import ScoreCount
from .slurm_config import SlurmConfig as Config


class SlurmCount(ScoreCount):

    @staticmethod
    def __chunks(l, n):
        """
        Divides a list into n of equally sized chunks, as possible
        :param l: list to divide
        :param n: number of chunks
        :return: generator of chunks
        """
        for i in range(0, len(l), n):
            yield l[i: i + n]

    @staticmethod
    def run(combinations, solutions):

        chunked = SlurmCount.__chunks(solutions, Config.AVAILABLE_WORKERS)

        workers = [
            Popen(['run_count.sh', combinations, solution], stdout=PIPE, stderr=PIPE)
            for solution in chunked
        ]

        scores = {}

        while workers:
            for proc in workers:
                retcode = proc.poll()
                if retcode:  # process finished
                    workers.remove(proc)
                    break
                else:  # No process is done, wait a bit and check again
                    sleep(Config.SLEEP_TIME)
                    continue
            # Here, 'proc' has finished with return code 'retcode'
            if retcode:
                # Error handling
                pass

            scores.update(proc.stdout)
