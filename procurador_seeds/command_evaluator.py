import shlex
import subprocess
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class CommandEvaluator:
    """Run a real external evaluator command to count blacksmiths.

    The command must print a single integer to stdout. Use `{seed}` in the
    command template to inject the seed.
    """

    command_template: Sequence[str]

    def count_blacksmiths(self, seed: int) -> int:
        command = [part.format(seed=seed) for part in self.command_template]
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )
        output = result.stdout.strip()
        if not output:
            raise ValueError("Evaluator did not return a count on stdout.")
        return int(output)


def parse_command_template(command: str) -> Sequence[str]:
    return shlex.split(command)
