"""Module for mapping strings to lists of integers."""


class Alphabet:
    """Remapping alphabet."""

    def __init__(self, x: str):
        """Build the alphabet from a string."""
        self._map = {a: i for i, a in enumerate(sorted(set(x)))}
        self._revmap = {b: a for a, b in self._map.items()}
        self.sigma = len(self._map)

    def map(self, x: str) -> list[int]:
        """Map a string to this alphabet."""
        return [self._map[a] for a in x]

    def revmap(self, y: list[int]) -> str:
        """Reverse a mapped string."""
        return "".join(self._revmap[a] for a in y)
