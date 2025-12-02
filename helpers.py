import re
from dataclasses import dataclass
from pathlib import Path

RE_NUMS = re.compile(r'\d+')


@dataclass
class Paths:
    p1: str
    _option: int = 0
    _real: Path = Path()
    _test: Path = Path()

    def __post_init__(self):
        self._real = Path(self.p1)
        self._test = self._real.with_stem(self._real.stem + '_test')

    def get(self) -> Path:
        if self._option == 0:
            return self._real

        if self._option == 1:
            return self._test

        raise ValueError(f"Unexpected value encountered: {self._option}")

    def set_option(self, value: int):
        self._option = value

    def is_real(self):
        return self._option == 0

    def lines(self):
        with open(self.get(), encoding='utf-8') as f:
            return [l.strip() for l in f]



