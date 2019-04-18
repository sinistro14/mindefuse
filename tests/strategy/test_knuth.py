#! usr/bin/env python3.7

import pytest


class TestKnuth:

    @pytest.mark.parametrize("secret, guess, expected", [
        (
            (),
            (),
            (),
        ),
    ])
    def test_knuth(self, helper, mindefuse, secret, guess, expected):
        pass
