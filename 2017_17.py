from helpers import Paths, RE_NUMS


def dfs(k: int, g: int, graph: dict[int, set[int]]):
    q = [k]
    seen = set()
    while q:
        k = q.pop()
        if k == g:
            return True

        for r in graph[k]:
            if r not in seen:
                seen.add(r)
                q.append(r)

    return False


def parse(paths: Paths):
    lines = paths.lines()
    g = dict()
    for line in lines:
        n, *children = RE_NUMS.findall(line)
        g[int(n)] = [int(i) for i in children]
    return g


def part01(graph):
    t = sum(dfs(k, 0, graph) for k in graph)
    assert t == 239


def part02(graph):
    found = set()
    t = 0
    for i in range(len(graph)):
        r = set(k for k in graph if k not in found and dfs(k, i, graph))
        if len(r) > 0:
            t += 1
        found |= r
    assert t == 215


def run() -> None:
    paths = Paths("./data/2017_17.txt")
    paths.set_option(0)
    graph = parse(paths)
    part01(graph)
    part02(graph)


if __name__ == "__main__":
    run()
