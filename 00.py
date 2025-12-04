from helpers import RE_NUMS, Paths


def parse(paths: Paths):
    lines = paths.lines()
    l1 = []
    l2 = []
    for line in lines:
        a, b = (int(i) for i in RE_NUMS.findall(line))
        l1.append(a)
        l2.append(b)

    return l1, l2


def part01(paths):
    # part 01
    l1, l2 = parse(paths)
    l1.sort()
    l2.sort()
    t = [abs(x - y) for x, y in zip(l1, l2)]
    if paths.is_real():
        assert 1765812 == sum(t)
    else:
        assert 11 == sum(t)


def part02(paths):
    # part 02
    l1, l2 = parse(paths)
    r = (x * l2.count(x) for x in l1)

    if paths.is_real():
        assert 20520794 == sum(r)
    else:
        assert 31 == sum(r)


def run() -> None:
    paths = Paths("./data/00.txt")
    paths.set_option(1)
    part01(paths)
    part02(paths)


if __name__ == "__main__":
    run()
