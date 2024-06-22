
#!/usr/bin/env python3
"""
The function should return a tuple of size two containing
a start index and an end index corresponding to the range of
indexes to return in a list for those
particular pagination parameters
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Prototype: def index_range(page:int, page_size: int)
    Returns a Tuple of size
    """
    index = page * page_size - page_size
    index_ = index + page_size
    return (index, index_)
