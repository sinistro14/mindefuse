#! usr/bin/env python3.7

import pytest
from mindefuse.problem import Secret


class TestSecretComparison:

    # comparing two different sized sequences raises an exception
    @pytest.mark.parametrize("secret, guess", [
        (
            "abcd",
            "a"
        ),
    ])
    def test_different_sizes(self, secret, guess):
        with pytest.raises(AssertionError):
            Secret.compare_sequences(secret, guess)
