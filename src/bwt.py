"""Burrows-Wheeler transform."""


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
    return 'FIXME'


def rbwt(y: str) -> str:
    """
    Reverse the Burrows-Wheeler transform for y.

    >>> rbwt('ipssm$pissii')
    'mississippi'
    """
    return 'FIXME'
