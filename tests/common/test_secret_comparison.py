#! usr/bin/env python3.7

import pytest
from mindefuse.problem import Secret


class TestSecretComparison:

    # wrong input types raise an exception
    @pytest.mark.parametrize("secret, guess", [
        (1, "1"),
        ("1", 1),
        (1, 1),
    ])
    def test_wrong_inputs(self, secret, guess):
        with pytest.raises(AssertionError):
            Secret.compare_sequences(secret, guess)

    # comparing two different sized sequences raises an exception
    @pytest.mark.parametrize("secret, guess", [
        ("abcd", "a"),
        ("abcd", "abcde"),
    ])
    def test_wrong_sizes(self, secret, guess):
        with pytest.raises(AssertionError):
            Secret.compare_sequences(secret, guess)

    @pytest.mark.parametrize("secret, guess, expected", [
        ("abcd", "eeee", (0, 0)),
        ("abcd", "aaaa", (0, 1)),
        ("abcd", "aeee", (0, 1)),
        ("abcd", "abcd", (0, 4)),
        ("abcd", "aaaa", (0, 1)),
        ("abcd", "acaa", (1, 1)),
        ("abcd", "dcba", (4, 0)),
        ("abcd", "cbad", (2, 2)),
        ("aaaa", "abbb", (0, 1)),
        ("abcd", "dbba", (2, 1)),
    ])
    def test_secret_comparison(self, helper, mindefuse, secret, guess, expected):
        assert Secret.compare_sequences(secret, guess) == expected
