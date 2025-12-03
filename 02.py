from dataclasses import dataclass

from helpers import Paths, RE_NUMS

def parse(paths):
    lines = paths.lines()
    r = lines[0].split(",")
    yield from (item.split('-') for item in r)

def part01(paths):
    data = parse(paths)
    all = []
    for f, l in data:
        for i in range(int(f), int(l) + 1):
            s = str(i)
            if len(s) % 2 == 0:
                splitter = len(s) // 2
                if s[:splitter] == s[splitter:]:
                    all.append(i)

    assert sum(all) == 18700015741

def part02(paths):
    data = parse(paths)
    all = []
    for f, l in data:
        for i in range(int(f), int(l) + 1):
            ss = str(i)
            for ii in range(1, (len(ss) // 2) + 1):
                s = ss[::]
                parts = []
                while s:
                    parts.append(s[:ii])
                    s = s[ii:]

                if len(parts) >= 2 and len(set(parts)) == 1:
                    all.append(i)
                    break

    assert sum(all) == 20077272987

if __name__ == "__main__":
    paths = Paths("./data/02.txt")
    paths.set_option(0)
    p1 = part01(paths)
    p2 = part02(paths)