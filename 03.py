from typing import Iterator

from helpers import Paths

def parse(paths) -> Iterator[list[int]]:
    lines = paths.lines()
    yield from (list(line) for line in lines)


def part01(paths: Paths) -> None:
    t = 0
    for nums in parse(paths):
        p1, p2 = 0, 0
        for idx, n in enumerate(nums):
            if int(n) > p2:
                p2 = int(n)
                if idx < len(nums)-1 and p2 > p1:
                    p1, p2 = p2, 0
        t += int(f'{p1}{p2}')
    assert t == 17445


def part02(paths: Paths) -> None:
    t = 0
    for nums in parse(paths):
        parts = [0] * 12
        for idx, n in enumerate(nums):
            nn = int(n)
            end = -1 if len(nums[idx:]) > 12 else 12-1 - len(nums[idx:])
            for idx2 in range(len(parts)-1, end, -1):
                if nn > parts[idx2]:
                    parts[idx2] = nn
                    if 0 < idx2 + 1 < 12:
                        parts[idx2+1] = 0

        t += int(''.join(str(p) for p in parts))
    assert t == 173229689350551

if __name__ == "__main__":
    paths = Paths('./data/03.txt')
    part02(paths)