from helpers import Paths


def parse(paths):
    lines = paths.lines()
    r = lines[0].split(",")
    yield from (item.split("-") for item in r)


def part01(paths):
    data = parse(paths)
    all_ = []
    for first, last in data:
        for i in range(int(first), int(last) + 1):
            s = str(i)
            if len(s) % 2 == 0:
                splitter = len(s) // 2
                if s[:splitter] == s[splitter:]:
                    all_.append(i)

    assert sum(all_) == 18700015741


def part02(paths):
    data = parse(paths)
    all_ = []
    for first, last in data:
        for i in range(int(first), int(last) + 1):
            ss = str(i)
            for ii in range(1, (len(ss) // 2) + 1):
                s = ss[::]
                parts = []
                while s:
                    parts.append(s[:ii])
                    s = s[ii:]

                if len(parts) >= 2 and len(set(parts)) == 1:
                    all_.append(i)
                    break

    assert sum(all_) == 20077272987


def run() -> None:
    paths = Paths("./data/02.txt")
    paths.set_option(0)
    part01(paths)
    part02(paths)


if __name__ == "__main__":
    run()
