import re

nums = re.compile(r'\d+')

def parse():
    with open('./data/00.txt', encoding='utf-8') as f:
        lines = [line for line in f]

    l1 = []
    l2 = []
    for line in lines:
        a, b = (int(i) for i in nums.findall(line))
        l1.append(a)
        l2.append(b)

    return l1, l2

def part01():
    # part 01
    l1, l2 = parse()
    l1.sort()
    l2.sort()
    t = [abs(x - y) for x, y in zip(l1, l2)]
    assert 1765812 == sum(t)

def part02():
    # part 02
    l1, l2 = parse()
    r = (x * l2.count(x) for x in l1)
    assert 20520794 == sum(r)

part01()
part02()