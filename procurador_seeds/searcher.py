from dataclasses import dataclass
from typing import Iterable, Iterator, Protocol


class SeedEvaluator(Protocol):
    def count_blacksmiths(self, seed: int) -> int:
        """Return how many blacksmiths exist for the given seed."""


@dataclass(frozen=True)
class SeedSearchConfig:
    minimum_blacksmiths: int = 3
    start_seed: int = 0
    end_seed: int = 10_000


class SeedSearcher:
    def __init__(self, evaluator: SeedEvaluator, config: SeedSearchConfig) -> None:
        self._evaluator = evaluator
        self._config = config

    def iter_candidate_seeds(self) -> Iterable[int]:
        return range(self._config.start_seed, self._config.end_seed + 1)

    def find_seeds(self) -> Iterator[int]:
        """Yield seeds that have at least the configured number of blacksmiths.

        This implementation is intentionally brute-force (no heuristics),
        scanning each seed in the configured interval.
        """
        for seed in self.iter_candidate_seeds():
            blacksmiths = self._evaluator.count_blacksmiths(seed)
            if blacksmiths >= self._config.minimum_blacksmiths:
                yield seed
