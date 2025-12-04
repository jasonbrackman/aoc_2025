from helpers import Paths


def part01(paths: Paths) -> None:
    t = 0
    grid = [list(line) for line in paths.lines()]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            item = grid[y][x]
            if item == "@":
                n = 0
                for j in (-1, 0, 1):
                    for i in (-1, 0, 1):
                        yy, xx = y + j, x + i
                        if (yy, xx) != (y, x):
                            if 0 <= yy < len(grid) and 0 <= xx < len(grid[0]):
                                n += int(grid[yy][xx] == "@")
                t += int(n < 4)

    assert t == 1547


def part02(paths: Paths) -> None:
    t = 0
    grid = [list(line) for line in paths.lines()]
    found = set()
    keep_going = True
    while keep_going:
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                item = grid[y][x]
                if item == "@":
                    n = 0
                    for j in (-1, 0, 1):
                        for i in (-1, 0, 1):
                            yy, xx = y + j, x + i
                            if (yy, xx) != (y, x):
                                if 0 <= yy < len(grid) and 0 <= xx < len(grid[0]):
                                    n += int(grid[yy][xx] == "@")

                    if n < 4:
                        t += 1
                        found.add((y, x))
        if found:
            for yyy, xxx in found:
                grid[yyy][xxx] = "."
            found.clear()
        else:
            keep_going = False
    assert t == 8948


def run() -> None:
    paths = Paths("./data/04.txt")
    paths.set_option(0)
    part01(paths)
    part02(paths)


if __name__ == "__main__":
    run()
