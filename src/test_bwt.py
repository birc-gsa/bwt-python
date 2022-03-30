"""Testing bwt and reverse transform."""

import string
import random

from bwt import (
    bwt, rbwt
)


def random_string(n: int, alpha: str = string.ascii_uppercase) -> str:
    """Create a random string."""
    return ''.join(random.choices(alpha, k=n))


def test_bwt() -> None:
    """Tests bwt() and rbwt()."""
    for _ in range(10):
        x = random_string(10, "acgt")
        y = bwt(x)
        z = rbwt(y)
        assert x == z
