from helpers import Paths, RE_NUMS


def part01(paths: Paths):
    rules = []
    fresh = []  # <-- what I care about here
    other = []
    lines = paths.lines()
    a = True
    for line in lines:
        if not line:
            a = False
            continue
        if a:
            rules.append([int(i) for i in RE_NUMS.findall(line)])
            continue
        for s, f in rules:
            num = int(line)
            if s <= num <= f:
                fresh.append(num)
                break
        other.append(num)
    assert len(fresh) == 601


def is_unique(rule, rules) -> int:
    f, e = rule
    for idx, (f2, e2) in enumerate(rules):
        if f2 <= f <= e2 or f2 <= e <= e2:
            return idx
        if f <= f2 <= e or f <= e2 <= e:
            return idx
    return -1


def merge(r1, r2):
    f, s = r1
    f2, s2 = r2

    if f <= f2:
        if s >= s2:
            return f, s
        if s <= s2:
            return f, s2

    if f >= f2:
        if s >= s2:
            return f2, s
        if s <= s2:
            return f2, s2

    raise ValueError("Impossible to get here from the inputs provided.")


def part02(paths: Paths):
    rules = list()
    lines = paths.lines()
    for line in lines:
        if not line:
            break
        rules.append(tuple(int(i) for i in RE_NUMS.findall(line)))

    keepers = set()
    while rules:
        rules = sorted(rules)
        rule = rules.pop()
        rule_idx = is_unique(rule, rules)

        if rule_idx == -1:
            keepers.add(rule)
            continue
        rule2 = rules.pop(rule_idx)
        r = merge(rule, rule2)
        rules.append(r)

    t = 0
    for a, b in sorted(keepers):
        assert b >= a, f"{b} - {a}"
        t += b - a + 1

    assert t == 367899984917516


if __name__ == "__main__":
    paths = Paths(r"./data/05.txt")
    paths.set_option(0)
    part01(paths)
    part02(paths)
