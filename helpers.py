import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Callable

RE_NUMS = re.compile(r"\d+")

Pos = tuple[int, int]


@dataclass
class Paths:
    p1: str
    _option: int = 0
    _real: Path = Path()
    _test: Path = Path()

    def __post_init__(self):
        self._real = Path(self.p1)
        self._test = self._real.with_stem(self._real.stem + "_test")

    def get(self) -> Path:
        if self._option == 0:
            return self._real

        if self._option == 1:
            return self._test

        raise ValueError(f"Unexpected value encountered: {self._option}")

    def set_option(self, value: int):
        self._option = value

    def is_real(self):
        return self._option == 0

    def lines(self):
        with open(self.get(), encoding="utf-8") as f:
            return [line.strip("\n") for line in f]

    def lines_no_strip(self):
        with open(self.get(), encoding="utf-8") as f:
            return [line for line in f]


@dataclass
class Node:
    state: Pos
    parent: Optional["Node"]
    depth: int


def bfs(start: Pos, goal: Pos, grid: list[list[int]], neighbours: Callable):
    seen = set()
    q = [Node(start, None, 0)]

    while q:
        n = q.pop()
        if n.state in seen:
            continue

        if n.state == goal:
            return n

        for item in neighbours(n.state, grid):
            if item not in seen:
                q.append(Node(item, n, n.depth + 1))

    return None


def neighbours(pos: Pos, grid: list[list[int]]):
    """
    WIll yield all legal areas of a grid surrounding the position searched.

    If x is the position, the # is what is searched.

        ###
        #x#
        ###

    """
    y, x = pos
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            yy = y + i
            xx = x + j
            if pos == (yy, xx):
                continue

            if 0 <= y + i < len(grid) and 0 <= x + j < len(grid[0]):
                yield yy, xx
