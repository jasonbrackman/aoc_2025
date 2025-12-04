from helpers import Paths


def parse(paths: Paths):
    lines = paths.lines()
    return lines


def part01(paths):
    r = parse(paths)
    x = []
    start = 50
    for item in r:
        d = item[0]
        n = int(item[1:])
        if d == "L":
            start = (start - n) % 100
            x.append(start)
        else:
            start = (start + n) % 100
            x.append(start)

    return x.count(0)


def part02(paths):
    r = parse(paths)
    count = 0
    start = 50

    for item in r:
        d = item[0]
        n = int(item[1:])

        val_r = n % 100
        if (n - val_r) > 0 and (n - val_r) % 100 == 0:
            val_c = (n - val_r) // 100
            count += val_c

        if d == "L":
            new = (start - val_r) % 100
            if start <= new:
                if start != 0 and new != 0 and n % 100 != 0:
                    count += 1
        else:
            new = (start + val_r) % 100
            if start >= new:
                if start != 0 and new != 0 and n % 100 != 0:
                    count += 1
        start = new
        if start == 0:
            count += 1
    return count


def run() -> None:
    paths_ = Paths("./data/01.txt")
    assert part01(paths_) == 984
    assert part02(paths_) == 5657


if __name__ == "__main__":
    run()
