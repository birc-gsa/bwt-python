"""Testing suffix array construction."""

import string
import random

from sa import prefix_doubling


def check_suffix_array(x: str, sa: list[int]) -> None:
    """Check that the suffix array sa is sorted."""
    for i in range(1, len(sa)):
        assert x[sa[i-1]:] < x[sa[i]:]


def random_string(n: int, alpha: str = string.ascii_uppercase) -> str:
    """Create a random string."""
    return ''.join(random.choices(alpha, k=n))


def test_prefix_doubling() -> None:
    """Tests prefix_doubling()."""
    for _ in range(10):
        x = random_string(10, "acgt")
        sa = prefix_doubling(x)
        check_suffix_array(x, sa)
