import math

from helpers import Paths, RE_NUMS


def parse(paths):
    table = []
    for line in paths.lines():
        if "*" not in line:
            table.append([int(i) for i in RE_NUMS.findall(line)])
        else:
            table.append([c for c in line.split(" ") if c])
    return table


def get_value(items, op):
    if op == "*":
        return math.prod(items)
    if op == "+":
        return sum(items)
    raise ValueError


def reorg2(items):
    op = items.pop().strip()
    final = []
    for x in range(len(items[0])):
        r = "".join(item[x] for item in items).strip()
        if r:
            final.append(int(r.strip()))

    return get_value(final, op)


def part01(paths):
    table = parse(paths)
    t = 0
    for i in range(len(table[0])):
        items = [row[i] for row in table]
        op = items[-1]
        t += get_value(items[:-1], op)
    assert t == 5316572080628


def part02(paths):
    table = paths.lines()
    ops = table[-1]

    # obtain ranges based on OP positions in the last line.
    indexes = [idx for idx, c in enumerate(ops) if c in "*+"]
    mm = max([len(t) for t in table])

    # calc total
    t = 0
    indexes.append(mm)
    while len(indexes) > 1:
        s = indexes.pop(0)
        n = indexes[0]
        items = [row[s:n] for row in table]
        t += reorg2(items)

    assert t == 11299263623062


def run() -> None:
    paths = Paths("./data/06.txt")
    paths.set_option(0)
    part01(paths)
    part02(paths)


if __name__ == "__main__":
    run()
