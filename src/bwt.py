"""Burrows-Wheeler transform."""

from collections import Counter
from sa import prefix_doubling

# I would normally use '\x00' for the sentinel, but doctest doesn't
# like that (because it is gods damned stupid). For this example,
# using $ will be fine, but it would not be a good choice in production
# code...


def bwt(x: str) -> str:
    """
    Transform x into its Burrows-Wheeler transform.

    >>> bwt('mississippi')
    'ipssm$pissii'
    """
    sa = prefix_doubling(x)
    return ''.join([x[i - 1] if i > 0 else '$' for i in sa])


class Alphabet:
    """Remapping alphabet."""

    def __init__(self, x: str):
        """Build the alphabet from a string."""
        self._map = {a: i for i, a in enumerate(sorted(set(x)))}
        self._revmap = {b: a for a, b in self._map.items()}

    def map(self, x: str) -> list[int]:
        """Map a string to this alphabet."""
        return [self._map[a] for a in x]

    def revmap(self, y: list[int]) -> str:
        """Reverse a mapped string."""
        return "".join(self._revmap[a] for a in y)


def ctable(z: list[int]) -> list[int]:
    """
    Compute the C table for a mapped string.

    >>> ctable([1, 2, 1, 0])
    [0, 1, 3]
    """
    sigma = max(z) + 1
    counts = Counter(z)
    ctab = [0] * sigma
    acc = 0
    for i, _ in enumerate(ctab):
        ctab[i] = acc
        acc += counts[i]
    return ctab


def otable(z: list[int]) -> list[list[int]]:
    """
    Compute the O table for a mapped string.

    >>> otable([1, 2, 0, 2, 3])
    [[0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 2, 2], [0, 0, 0, 0, 0, 1]]
    """
    sigma = max(z) + 1
    otab = [
        [0] * (len(z) + 1) for _ in range(sigma)
    ]
    for a in range(sigma):
        for i, b in enumerate(z):
            otab[a][i + 1] = otab[a][i] + (a == b)
    return otab


def rbwt(y: str) -> str:
    """
    Reverse the Burrows-Wheeler transform for y.

    >>> rbwt('ipssm$pissii')
    'mississippi'
    """
    alpha = Alphabet(y)
    z = alpha.map(y)
    ctab = ctable(z)
    otab = otable(z)
    i, x = 0, [0] * (len(y) - 1)
    for j in reversed(range(len(z) - 1)):
        a = x[j] = z[i]
        i = ctab[a] + otab[a][i]
    return alpha.revmap(x)
