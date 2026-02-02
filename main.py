import argparse

from procurador_seeds.command_evaluator import CommandEvaluator, parse_command_template
from procurador_seeds.searcher import SeedSearchConfig, SeedSearcher


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Procura seeds com 3+ ferreiros usando um avaliador real externo."
        )
    )
    parser.add_argument(
        "--cmd",
        required=True,
        help=(
            "Comando do avaliador real. Use {seed} para inserir a seed. "
            "O comando deve imprimir um inteiro com a contagem de ferreiros."
        ),
    )
    parser.add_argument("--min", type=int, default=3, help="Mínimo de ferreiros.")
    parser.add_argument("--start", type=int, default=0, help="Seed inicial.")
    parser.add_argument("--end", type=int, default=10_000, help="Seed final.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    evaluator = CommandEvaluator(parse_command_template(args.cmd))
    config = SeedSearchConfig(
        minimum_blacksmiths=args.min,
        start_seed=args.start,
        end_seed=args.end,
    )
    searcher = SeedSearcher(evaluator, config)

    for seed in searcher.find_seeds():
        print(seed)


if __name__ == "__main__":
    main()
