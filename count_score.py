#!/usr/bin/env python3.7

import sys
from multiprocessing import Pool
from functools import partial
from collections import defaultdict, Counter


def compare_sequences(sequence: str, proposal: str):
    """
    Compare the proposed sequence with the a sequence
    :param sequence: correct sequence
    :param proposal: sequence proposed as the correct sequence
    :return: tuple with number of whites and number of reds
    """
    assert isinstance(sequence, str) and isinstance(proposal, str) and len(sequence) == len(proposal)

    # count all reds
    reds = sum(secret_val == seq_val for secret_val, seq_val in zip(sequence, proposal))

    # count number of chars
    secret_count = Counter(sequence)
    proposal_count = Counter(proposal)

    # count all whites
    whites = sum(min(value, proposal_count.get(char, 0)) for char, value in secret_count.items()) - reds

    return whites, reds


def count_score(combination, solutions):
    """
    Provides the
    Sets in scores the score of the provided combination.
    The score of a combination is the maximum size of the solution space, in the worst case,
    if the said combination was the secret sequence.
    :param combination: combination being tested
    :param solutions: solution space
    """
    score_count = defaultdict(int)

    for solution in solutions:
        score = sum(compare_sequences(combination, solution))  # sum the two elements of the array
        score_count[score] += 1

    return combination, score_count[max(score_count, key=score_count.get)]


def count_scores(combinations, solutions):

    POOL_SIZE = 4

    pool = Pool(POOL_SIZE)
    combinations_space = list(combinations)

    scores = {
        combinations: score for combinations, score in pool.imap_unordered(
            partial(count_score, solutions=list(solutions)),
            iterable=combinations_space,
            chunksize=len(combinations_space) // POOL_SIZE,
        )
    }

    pool.close()

    return scores


def main():
    return count_scores(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
